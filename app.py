"""
EventRadar - Networking Events Dashboard
Flask backend with Eventbrite, Meetup, and Luma integration
"""

from flask import Flask, render_template, jsonify, request
import requests
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict
import time

# Import curated February 2026 events
# Using verified 10-event SF dataset (100-event version has syntax issues to fix)
try:
    from curated_events_feb2026_real import CURATED_EVENTS
    print("✅ Loaded 10 real curated February 2026 SF events (verified)")
except ImportError:
    CURATED_EVENTS = None
    print("❌ No curated events found")

app = Flask(__name__)

# City configurations
CITIES = {
    'sf': {
        'name': 'San Francisco / Bay Area',
        'latitude': 37.7749,
        'longitude': -122.4194
    },
    'la': {
        'name': 'Los Angeles',
        'latitude': 34.0522,
        'longitude': -118.2437
    },
    'nyc': {
        'name': 'New York City',
        'latitude': 40.7128,
        'longitude': -74.0060
    },
    'chicago': {
        'name': 'Chicago',
        'latitude': 41.8781,
        'longitude': -87.6298
    },
    'san-diego': {
        'name': 'San Diego',
        'latitude': 32.7157,
        'longitude': -117.1611
    }
}

# Configuration
CONFIG = {
    'default_city': 'sf',
    'radius_miles': 25,
    'filters': {
        'categories': ['tech', 'business', 'networking', 'startup', 'entrepreneur'],
        'max_price': 50,
        'days_ahead': 30
    }
}

DATA_FILE = 'data/events_cache.json'
CACHE_DURATION = 86400  # 24 hours in seconds

class EventAggregator:
    def __init__(self):
        token = os.environ.get('EVENTBRITE_TOKEN', '')
        self.eventbrite_token = token if token and 'your_' not in token else ''
        key = os.environ.get('MEETUP_KEY', '')
        self.meetup_key = key if key and 'your_' not in key else ''
        
    def get_all_events(self, city_code: str = 'sf') -> List[Dict]:
        """Aggregate events from all sources"""
        events = []
        
        # Validate city code
        if city_code not in CITIES:
            city_code = CONFIG['default_city']
        
        # Try to load from cache first
        cached = self.load_cache(city_code)
        if cached:
            return cached
        
        # Fetch from APIs
        city_info = CITIES[city_code]
        events.extend(self.fetch_eventbrite(city_info))
        events.extend(self.fetch_meetup(city_info))
        events.extend(self.fetch_luma(city_info))
        
        # Sort by date
        events.sort(key=lambda x: x.get('start_time', ''))
        
        # Save to cache
        self.save_cache(events, city_code)
        
        return events
    
    def load_cache(self, city_code: str) -> List[Dict]:
        """Load events from cache if recent enough"""
        try:
            cache_file = f'data/events_cache_{city_code}.json'
            if os.path.exists(cache_file):
                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    cache_time = data.get('cached_at', 0)
                    if time.time() - cache_time < CACHE_DURATION:
                        return data.get('events', [])
        except Exception as e:
            print(f"Cache load error: {e}")
        return None
    
    def save_cache(self, events: List[Dict], city_code: str):
        """Save events to cache"""
        try:
            cache_file = f'data/events_cache_{city_code}.json'
            os.makedirs('data', exist_ok=True)
            with open(cache_file, 'w') as f:
                json.dump({
                    'cached_at': time.time(),
                    'events': events
                }, f, indent=2)
        except Exception as e:
            print(f"Cache save error: {e}")
    
    def fetch_eventbrite(self, city_info: Dict) -> List[Dict]:
        """Fetch events from Eventbrite API"""
        events = []
        
        if not self.eventbrite_token:
            print("Eventbrite token not configured - using curated February 2026 events")
            return self.get_curated_events(city_info)
        
        try:
            end_date = datetime.now() + timedelta(days=CONFIG['filters']['days_ahead'])
            
            params = {
                'location.latitude': city_info['latitude'],
                'location.longitude': city_info['longitude'],
                'location.within': f"{CONFIG['radius_miles']}mi",
                'start_date.range_start': datetime.now().isoformat(),
                'start_date.range_end': end_date.isoformat(),
                'expand': 'venue',
                'categories': '102,101',  # Tech & Business categories
            }
            
            headers = {
                'Authorization': f'Bearer {self.eventbrite_token}'
            }
            
            response = requests.get(
                'https://www.eventbriteapi.com/v3/events/search/',
                params=params,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                for event in data.get('events', []):
                    # Filter by price
                    is_free = event.get('is_free', True)
                    ticket_availability = event.get('ticket_availability', {})
                    
                    price = 0
                    if not is_free and ticket_availability:
                        price = float(ticket_availability.get('minimum_ticket_price', {}).get('major_value', 0))
                    
                    if is_free or price <= CONFIG['filters']['max_price']:
                        events.append({
                            'title': event['name']['text'],
                            'description': event.get('description', {}).get('text', '')[:200],
                            'start_time': event['start']['local'],
                            'end_time': event.get('end', {}).get('local', ''),
                            'location': self.format_venue(event.get('venue')),
                            'price': 'Free' if is_free else f'${price:.0f}',
                            'url': event['url'],
                            'source': 'Eventbrite',
                            'image': event.get('logo', {}).get('url', '')
                        })
            else:
                print(f"Eventbrite API error: {response.status_code}")
                
        except Exception as e:
            print(f"Eventbrite fetch error: {e}")
        
        return events
    
    def fetch_meetup(self, city_info: Dict) -> List[Dict]:
        """Fetch events from Meetup API"""
        events = []
        
        # Note: Meetup API requires OAuth now, this is a simplified version
        # You may need to use GraphQL API or implement OAuth flow
        
        try:
            # Using the GraphQL API endpoint
            url = "https://api.meetup.com/gql"
            
            # For now, return empty since Meetup requires complex auth
            # Real curated events are returned via Eventbrite
            print("Meetup API integration requires OAuth - skipping (using curated events)")
            
        except Exception as e:
            print(f"Meetup fetch error: {e}")
        
        return events
    
    def fetch_luma(self, city_info: Dict) -> List[Dict]:
        """Fetch events from Luma calendar"""
        events = []
        
        try:
            # Luma doesn't have a public API, we'll scrape or use RSS
            # For MVP, we'll add manual curated events or use public calendar URLs
            print("Luma integration requires calendar scraping - skipping (using curated events)")
            
        except Exception as e:
            print(f"Luma fetch error: {e}")
        
        return events
    
    def format_venue(self, venue):
        """Format venue information"""
        if not venue:
            return "Online Event"
        
        parts = []
        if venue.get('name'):
            parts.append(venue['name'])
        if venue.get('address', {}).get('city'):
            parts.append(venue['address']['city'])
        
        return ', '.join(parts) if parts else "Location TBA"
    
    def get_curated_events(self, city_info: Dict) -> List[Dict]:
        """Return curated real events from February 2026"""
        
        # Use curated real events if available
        if CURATED_EVENTS:
            city_name = city_info['name']
            
            # Map city names to curated event keys
            city_map = {
                'San Francisco / Bay Area': 'sf',
                'Los Angeles': 'la',
                'New York City': 'nyc',
                'Chicago': 'chicago',
                'San Diego': 'san-diego'
            }
            
            city_key = city_map.get(city_name)
            if city_key and city_key in CURATED_EVENTS:
                return CURATED_EVENTS[city_key]
        
        # Fallback to empty list if no curated events
        return []

aggregator = EventAggregator()

@app.route('/')
def index():
    """Render main dashboard"""
    return render_template('index.html')

@app.route('/api/cities')
def get_cities():
    """API endpoint to get available cities"""
    return jsonify({
        'success': True,
        'cities': [
            {'code': code, 'name': info['name']}
            for code, info in CITIES.items()
        ],
        'default': CONFIG['default_city']
    })

@app.route('/api/events')
def get_events():
    """API endpoint to get all events"""
    try:
        city_code = request.args.get('city', CONFIG['default_city'])
        events = aggregator.get_all_events(city_code)
        return jsonify({
            'success': True,
            'count': len(events),
            'events': events
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/refresh')
def refresh_events():
    """Force refresh events from APIs"""
    try:
        city_code = request.args.get('city', CONFIG['default_city'])
        
        # Delete cache to force refresh
        cache_file = f'data/events_cache_{city_code}.json'
        if os.path.exists(cache_file):
            os.remove(cache_file)
        
        events = aggregator.get_all_events(city_code)
        return jsonify({
            'success': True,
            'count': len(events),
            'message': 'Events refreshed successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/config', methods=['GET', 'POST'])
def config():
    """Get or update configuration"""
    if request.method == 'POST':
        # Update config
        new_config = request.json
        CONFIG.update(new_config)
        return jsonify({'success': True, 'config': CONFIG})
    else:
        return jsonify(CONFIG)

if __name__ == '__main__':
    print("🎯 EventRadar starting...")
    print(f"📍 Cities: {', '.join([info['name'] for info in CITIES.values()])}")
    print(f"💰 Max price: ${CONFIG['filters']['max_price']}")
    print(f"📅 Next {CONFIG['filters']['days_ahead']} days")
    print(f"📏 Radius: {CONFIG['radius_miles']} miles")
    
    # Use PORT from environment (Render/production) or default to 5000 (local)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    print(f"\n🚀 Dashboard: http://localhost:{port}\n")
    app.run(debug=debug, host='0.0.0.0', port=port)
