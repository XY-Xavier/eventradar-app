#!/usr/bin/env python3
"""
Update curated_events_feb2026_real.py with Unsplash images
Uses curated, high-quality images from Unsplash collections
"""

import re

# Curated Unsplash images for different event categories
# These are all from Unsplash's free-to-use library
IMAGE_CATEGORIES = {
    'ai_ml': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop',  # AI/ML visualization
    'women_tech': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop',  # Professional women in tech
    'healthcare': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop',  # Healthcare/medical
    'finance': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=600&fit=crop',  # Finance/business
    'crypto': 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800&h=600&fit=crop',  # Cryptocurrency/blockchain
    'startup': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop',  # Startup/teamwork
    'coffee': 'https://images.unsplash.com/photo-1511920170033-f8396924c348?w=800&h=600&fit=crop',  # Coffee meeting
    'cybersecurity': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop',  # Cybersecurity
    'coding': 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=800&h=600&fit=crop',  # Coding/development
    'product': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&h=600&fit=crop',  # Product management/strategy
    'diversity': 'https://images.unsplash.com/photo-1529070538774-1843cb3265df?w=800&h=600&fit=crop',  # Diversity/team
    'mobile': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop',  # Mobile/app development
    'entertainment': 'https://images.unsplash.com/photo-1574267432644-f74e6a8b43f2?w=800&h=600&fit=crop',  # Entertainment/media
    'networking': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop',  # Business networking
    'tech_general': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&h=600&fit=crop',  # General tech/business
}

def get_image_for_event(event):
    """Determine the best image category for an event"""
    title = event['title'].lower()
    
    if any(word in title for word in ['ai', 'machine learning', 'ml']):
        return IMAGE_CATEGORIES['ai_ml']
    elif any(word in title for word in ['women in tech', 'women who code']):
        return IMAGE_CATEGORIES['women_tech']
    elif any(word in title for word in ['healthtech', 'biopharma', 'biotech']):
        return IMAGE_CATEGORIES['healthcare']
    elif any(word in title for word in ['fintech', 'finance']):
        return IMAGE_CATEGORIES['finance']
    elif any(word in title for word in ['crypto', 'blockchain', 'web3']):
        return IMAGE_CATEGORIES['crypto']
    elif any(word in title for word in ['startup', 'founders', 'entrepreneurs']):
        return IMAGE_CATEGORIES['startup']
    elif any(word in title for word in ['coffee', 'breakfast']):
        return IMAGE_CATEGORIES['coffee']
    elif any(word in title for word in ['cybersecurity', 'security']):
        return IMAGE_CATEGORIES['cybersecurity']
    elif any(word in title for word in ['developer', 'devops', 'coding']):
        return IMAGE_CATEGORIES['coding']
    elif any(word in title for word in ['product management', 'product']):
        return IMAGE_CATEGORIES['product']
    elif any(word in title for word in ['diversity', 'inclusion']):
        return IMAGE_CATEGORIES['diversity']
    elif any(word in title for word in ['mobile', 'app']):
        return IMAGE_CATEGORIES['mobile']
    elif any(word in title for word in ['entertainment', 'media']):
        return IMAGE_CATEGORIES['entertainment']
    elif 'networking' in title or 'mixer' in title or 'happy hour' in title:
        return IMAGE_CATEGORIES['networking']
    else:
        return IMAGE_CATEGORIES['tech_general']

def update_file():
    """Read the file, update images, and write back"""
    
    file_path = '/Users/xy/.openclaw/workspace/eventradar/curated_events_feb2026_real.py'
    
    # Read the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Import to get the event structure
    from curated_events_feb2026_real import CURATED_EVENTS
    
    # Build replacement map
    updates = []
    for city, events in CURATED_EVENTS.items():
        for event in events:
            image_url = get_image_for_event(event)
            # Find and replace the empty image field for this event
            # We'll match on the title to make sure we get the right event
            title_escaped = re.escape(event['title'])
            updates.append((event['title'], image_url))
    
    # Update the content
    new_content = content
    for title, image_url in updates:
        # Find the event block and replace 'image': ''
        title_escaped = re.escape(title)
        pattern = f"('{title_escaped}'.*?'image':\\s*)''"
        replacement = f"\\1'{image_url}'"
        new_content = re.sub(pattern, replacement, new_content, flags=re.DOTALL, count=1)
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print("✅ Successfully updated all event images!")
    print(f"📝 Updated {len(updates)} events with curated Unsplash images")
    print("\nSample updates:")
    for i, (title, url) in enumerate(updates[:5], 1):
        print(f"{i}. {title[:60]}...")
        print(f"   → {url}\n")

if __name__ == '__main__':
    update_file()
