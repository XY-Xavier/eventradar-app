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
        self.eventbrite_token = os.environ.get('EVENTBRITE_TOKEN', '')
        self.meetup_key = os.environ.get('MEETUP_KEY', '')
        
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
            print("Eventbrite token not configured - using demo data")
            return self.get_demo_events('Eventbrite', city_info)
        
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
            
            # For now, return placeholder since Meetup requires complex auth
            print("Meetup API integration requires OAuth - using mock data for MVP")
            
            # Add demo events for MVP testing
            events = self.get_demo_events('Meetup', city_info)
            
        except Exception as e:
            print(f"Meetup fetch error: {e}")
        
        return events
    
    def fetch_luma(self, city_info: Dict) -> List[Dict]:
        """Fetch events from Luma calendar"""
        events = []
        
        try:
            # Luma doesn't have a public API, we'll scrape or use RSS
            # For MVP, we'll add manual curated events or use public calendar URLs
            print("Luma integration requires calendar scraping - placeholder for MVP")
            
            # Add demo events for MVP testing
            events = self.get_demo_events('Luma', city_info)
            
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
    
    def get_demo_events(self, source: str, city_info: Dict) -> List[Dict]:
        """Generate demo events for testing and MVP"""
        from datetime import datetime, timedelta
        
        city_name = city_info['name']
        
        # City-specific venues
        venues = {
            'San Francisco / Bay Area': ['The Battery', 'Philz Coffee, Palo Alto', 'GitHub HQ'],
            'Los Angeles': ['WeWork DTLA', 'The Arts District', 'Santa Monica Pier'],
            'New York City': ['WeWork SoHo', 'Brooklyn Tech Hub', 'Madison Square Garden'],
            'Chicago': ['1871 Tech Hub', 'The Loop Co-working', 'Navy Pier']
        }
        
        city_venues = venues.get(city_name, ['Downtown', 'City Center', 'Tech Hub'])
        
        demo_events = [
            {
                'title': f'{city_name.split("/")[0].strip()} Tech Networking Mixer',
                'description': f'Join fellow tech professionals for networking and drinks in {city_name}.',
                'start_time': (datetime.now() + timedelta(days=2, hours=18)).isoformat(),
                'end_time': (datetime.now() + timedelta(days=2, hours=21)).isoformat(),
                'location': f'{city_venues[0]}, {city_name.split("/")[0].strip()}',
                'price': 'Free',
                'url': 'https://example.com/event1',
                'source': source,
                'image': ''
            },
            {
                'title': 'Startup Founders Breakfast',
                'description': f'Monthly breakfast meetup for startup founders and entrepreneurs.',
                'start_time': (datetime.now() + timedelta(days=5, hours=9)).isoformat(),
                'end_time': (datetime.now() + timedelta(days=5, hours=11)).isoformat(),
                'location': f'{city_venues[1]}, {city_name.split("/")[0].strip()}',
                'price': '$15',
                'url': 'https://example.com/event2',
                'source': source,
                'image': ''
            },
            {
                'title': 'AI & Machine Learning Workshop',
                'description': 'Hands-on workshop covering the latest in AI/ML technologies and practical applications.',
                'start_time': (datetime.now() + timedelta(days=8, hours=14)).isoformat(),
                'end_time': (datetime.now() + timedelta(days=8, hours=17)).isoformat(),
                'location': f'{city_venues[2]}, {city_name.split("/")[0].strip()}',
                'price': '$45',
                'url': 'https://example.com/event3',
                'source': source,
                'image': ''
            }
        ]
        
        # Return 3 events for demo sources, or if Eventbrite is not configured
        return demo_events[:3]

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
