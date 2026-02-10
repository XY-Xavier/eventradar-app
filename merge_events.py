import json
import os

cities = ['sf', 'la', 'nyc', 'chicago']
all_data = {}

for city in cities:
    cache_file = f'data/events_cache_{city}.json'
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            data = json.load(f)
            all_data[city] = data.get('events', [])

# Save merged data
with open('static-site/data/events.json', 'w') as f:
    json.dump(all_data, f, indent=2)

print(f"✅ Merged {sum(len(events) for events in all_data.values())} events across {len(cities)} cities")
