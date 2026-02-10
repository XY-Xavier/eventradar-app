#!/usr/bin/env python3
"""
Add Unsplash images to EventRadar events based on keywords
"""

import re
import time

def extract_keywords(event):
    """Extract relevant keywords from event title and description"""
    title = event['title'].lower()
    description = event['description'].lower()
    
    # Define keyword mappings for different event types
    if any(word in title for word in ['ai', 'machine learning', 'ml']):
        return ['artificial-intelligence', 'technology', 'networking']
    elif any(word in title for word in ['women in tech', 'women who code']):
        return ['women-in-tech', 'technology', 'business-women']
    elif any(word in title for word in ['healthtech', 'biopharma', 'biotech']):
        return ['healthcare', 'medical', 'science']
    elif any(word in title for word in ['fintech', 'finance']):
        return ['finance', 'business', 'banking']
    elif any(word in title for word in ['crypto', 'blockchain', 'web3']):
        return ['cryptocurrency', 'blockchain', 'technology']
    elif any(word in title for word in ['startup', 'founders', 'entrepreneurs']):
        return ['startup', 'entrepreneur', 'business-meeting']
    elif any(word in title for word in ['coffee', 'breakfast']):
        return ['coffee', 'meeting', 'business']
    elif any(word in title for word in ['cybersecurity', 'security']):
        return ['cybersecurity', 'technology', 'security']
    elif any(word in title for word in ['developer', 'devops', 'coding']):
        return ['coding', 'programming', 'software']
    elif any(word in title for word in ['product management', 'product']):
        return ['product-management', 'business', 'team']
    elif any(word in title for word in ['diversity', 'inclusion']):
        return ['diversity', 'team', 'community']
    elif any(word in title for word in ['mobile', 'app']):
        return ['mobile', 'smartphone', 'technology']
    elif any(word in title for word in ['entertainment', 'media']):
        return ['entertainment', 'media', 'creative']
    elif 'networking' in title or 'mixer' in title or 'happy hour' in title:
        return ['networking', 'business-people', 'conference']
    else:
        return ['technology', 'business', 'meeting']

def get_unsplash_image_url(keywords, width=800, height=600):
    """
    Generate Unsplash image URL using their Source API
    No authentication required for this endpoint
    """
    # Use the first keyword as the primary search term
    query = keywords[0]
    # Unsplash Source API with specific dimensions
    return f"https://source.unsplash.com/{width}x{height}/?{query}"

def generate_event_images():
    """Generate image URLs for all events"""
    
    print("🎨 Generating Unsplash images for EventRadar events...")
    print("=" * 60)
    
    # Import the events
    from curated_events_feb2026_real import CURATED_EVENTS
    
    image_map = {}
    
    for city, events in CURATED_EVENTS.items():
        print(f"\n📍 {city.upper()}")
        print("-" * 60)
        
        for i, event in enumerate(events, 1):
            keywords = extract_keywords(event)
            image_url = get_unsplash_image_url(keywords)
            
            # Store in map for later use
            key = f"{city}_{i-1}"  # Use index for reliable matching
            image_map[key] = image_url
            
            print(f"{i}. {event['title'][:50]}...")
            print(f"   Keywords: {', '.join(keywords)}")
            print(f"   Image: {image_url}")
            
            # Small delay to be respectful to Unsplash
            time.sleep(0.1)
    
    print("\n" + "=" * 60)
    print(f"✅ Generated {sum(len(events) for events in CURATED_EVENTS.values())} image URLs")
    
    return image_map

if __name__ == '__main__':
    generate_event_images()
