# EventRadar Supabase Setup

## Database Schema

### Events Table
```sql
CREATE TABLE events (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  title TEXT NOT NULL,
  description TEXT,
  location TEXT NOT NULL,
  city TEXT NOT NULL,
  start_time TIMESTAMPTZ NOT NULL,
  end_time TIMESTAMPTZ,
  price TEXT NOT NULL,
  url TEXT NOT NULL,
  image TEXT,
  source TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for fast city + time queries
CREATE INDEX idx_events_city_time ON events(city, start_time);

-- Index for text search
CREATE INDEX idx_events_search ON events USING gin(to_tsvector('english', title || ' ' || COALESCE(description, '')));
```

### Cities Table
```sql
CREATE TABLE cities (
  code TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  latitude DECIMAL(9,6) NOT NULL,
  longitude DECIMAL(9,6) NOT NULL
);

-- Seed data
INSERT INTO cities (code, name, latitude, longitude) VALUES
  ('sf', 'San Francisco / Bay Area', 37.7749, -122.4194),
  ('la', 'Los Angeles', 34.0522, -118.2437),
  ('nyc', 'New York City', 40.7128, -74.0060),
  ('chicago', 'Chicago', 41.8781, -87.6298);
```

### Event Sources Table
```sql
CREATE TABLE event_sources (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  api_type TEXT NOT NULL,
  last_sync_at TIMESTAMPTZ,
  sync_status TEXT
);
```

## Row Level Security (RLS)

```sql
-- Enable RLS
ALTER TABLE events ENABLE ROW LEVEL SECURITY;
ALTER TABLE cities ENABLE ROW LEVEL SECURITY;

-- Public read access
CREATE POLICY "Events are publicly readable"
  ON events FOR SELECT
  USING (true);

CREATE POLICY "Cities are publicly readable"
  ON cities FOR SELECT
  USING (true);

-- Only authenticated users can insert
CREATE POLICY "Authenticated users can insert events"
  ON events FOR INSERT
  WITH CHECK (auth.role() = 'authenticated');
```

## API Endpoints

### 1. Get Events by City
```javascript
const { data, error } = await supabase
  .from('events')
  .select('*')
  .eq('city', cityCode)
  .gte('start_time', new Date().toISOString())
  .order('start_time', { ascending: true })
  .limit(50);
```

### 2. Search Events
```javascript
const { data, error } = await supabase
  .from('events')
  .select('*')
  .textSearch('title', searchQuery)
  .eq('city', cityCode)
  .limit(20);
```

### 3. Filter by Price
```javascript
const { data, error } = await supabase
  .from('events')
  .select('*')
  .eq('city', cityCode)
  .eq('price', 'Free')
  .limit(50);
```

## Python Backend (Flask Integration)

```python
from supabase import create_client, Client
import os

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

@app.route('/api/events')
def get_events():
    city = request.args.get('city', 'sf')
    
    response = supabase.table('events') \\
        .select('*') \\
        .eq('city', city) \\
        .gte('start_time', datetime.now().isoformat()) \\
        .order('start_time') \\
        .limit(50) \\
        .execute()
    
    return jsonify({
        'success': True,
        'events': response.data
    })
```

## Setup Steps

1. **Create Supabase Project**
   - Go to https://supabase.com/dashboard
   - New Project → "eventradar"
   - Copy Project URL + anon key

2. **Run Schema**
   - SQL Editor → paste schema above
   - Execute

3. **Add to Render Environment**
   ```
   SUPABASE_URL=https://xxx.supabase.co
   SUPABASE_KEY=eyJhbGc...
   ```

4. **Update requirements.txt**
   ```
   supabase==2.3.0
   ```

## Advantages Over JSON Files

✅ Real-time updates (no cache staleness)
✅ Advanced filtering (full-text search, geo queries)
✅ Scalable (handle millions of events)
✅ Built-in auth & RLS
✅ Automatic REST API
✅ Real-time subscriptions (events update live)

## Next Steps

1. Set up Supabase project
2. Run schema
3. Migrate demo data → Supabase
4. Update Flask app to use Supabase client
5. Deploy to Render with env vars
