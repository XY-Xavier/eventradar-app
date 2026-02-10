# 🎯 EventRadar - Bay Area Networking Events Dashboard

A clean, professional web dashboard for discovering tech and business networking events across 4 major US cities: **San Francisco, Los Angeles, New York City, and Chicago**.

![EventRadar Dashboard](https://img.shields.io/badge/Status-MVP-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey)

## ✨ Features

- **Multi-City Support**: Switch between 4 major cities (SF, LA, NYC, Chicago)
- **Multi-Source Aggregation**: Pulls events from Eventbrite, Meetup, and Luma calendars
- **Smart Filtering**: 
  - Location: 25 mile radius from city center
  - Categories: Tech, business, networking, startups
  - Price: Free or under $50
  - Timeframe: Next 30 days
- **Clean UI**: Responsive event cards with all key details
- **Auto-Refresh**: Daily cache per city with manual refresh option
- **Real-time Search**: Filter by keywords, price, or date range
- **City Preference**: Remembers your last selected city (localStorage)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/xy/.openclaw/workspace/eventradar
   ```

2. **Create virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   
   Or use the setup script:
   ```bash
   ./setup.sh
   ```

3. **Configure API keys:**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API tokens:
   - **Eventbrite Token**: Get it from [Eventbrite API](https://www.eventbrite.com/platform/api)
     1. Log in to Eventbrite
     2. Go to Account Settings → App Management
     3. Create a new app and generate a private token
   
   - **Meetup API** (optional): Requires OAuth flow - can be added later

4. **Run the application:**
   ```bash
   source venv/bin/activate  # Activate virtual environment
   python app.py
   ```

5. **Open your browser:**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
eventradar/
├── app.py                 # Flask backend with API integrations
├── templates/
│   └── index.html        # Frontend UI (Tailwind CSS)
├── data/
│   └── events_cache.json # Cached events (auto-generated)
├── requirements.txt       # Python dependencies
├── .env                  # API configuration (create from .env.example)
└── README.md             # This file
```

## 🔧 Configuration

Edit `CITIES` and `CONFIG` dictionaries in `app.py` to customize:

```python
CITIES = {
    'sf': {'name': 'San Francisco / Bay Area', 'latitude': 37.7749, 'longitude': -122.4194},
    'la': {'name': 'Los Angeles', 'latitude': 34.0522, 'longitude': -118.2437},
    'nyc': {'name': 'New York City', 'latitude': 40.7128, 'longitude': -74.0060},
    'chicago': {'name': 'Chicago', 'latitude': 41.8781, 'longitude': -87.6298}
}

CONFIG = {
    'default_city': 'sf',
    'radius_miles': 25,
    'filters': {
        'categories': ['tech', 'business', 'networking', 'startup', 'entrepreneur'],
        'max_price': 50,
        'days_ahead': 30
    }
}
```

Add more cities by adding entries to the `CITIES` dictionary!

## 🎨 Features Overview

### Dashboard Stats
- Total events count
- Free events count
- Events this week
- Last updated timestamp

### Event Cards
Each event card displays:
- Event title and description
- Date and time
- Location/venue
- Price (Free or $XX)
- Source platform (Eventbrite, Meetup, Luma)
- Direct registration link

### Filters
- **Search**: Find events by title, description, or location
- **Price**: All, Free only, or Paid events
- **Time**: All, Today, This Week, This Month

## 🔄 API Endpoints

- `GET /` - Main dashboard
- `GET /api/cities` - Get available cities
- `GET /api/events?city=CODE` - Fetch events for a city (JSON)
- `GET /api/refresh?city=CODE` - Force refresh from APIs for a city
- `GET/POST /api/config` - View or update configuration

## 📝 API Integration Status

| Source | Status | Notes |
|--------|--------|-------|
| Eventbrite | ✅ Ready | Full API integration with search |
| Meetup | 🚧 Partial | Requires OAuth flow (placeholder in MVP) |
| Luma | 🚧 Planned | No public API, needs scraping/RSS |

## 🛠️ Development

### Adding New Event Sources

1. Create a new `fetch_SOURCE()` method in the `EventAggregator` class
2. Return events in the standard format:
   ```python
   {
       'title': str,
       'description': str,
       'start_time': ISO datetime,
       'end_time': ISO datetime,
       'location': str,
       'price': 'Free' or '$XX',
       'url': str,
       'source': str,
       'image': str (optional)
   }
   ```
3. Add the source to `get_all_events()` aggregation

### Customizing Filters

Modify the filter logic in `templates/index.html` JavaScript section:
- Search: `filterEvents()` function
- Client-side filters: Update the filter dropdowns
- Server-side filters: Modify API params in `fetch_eventbrite()`

## 🐛 Troubleshooting

**Events not loading?**
- Check your `.env` file has valid API tokens
- Verify the Eventbrite token has proper permissions
- Check console logs: `tail -f` the terminal running Flask

**No events showing?**
- Eventbrite may have rate limits - wait a few minutes
- Try manually refreshing with the Refresh button
- Check if there are events matching your filters in the API response

**Port already in use?**
```bash
# Change port in app.py last line:
app.run(debug=True, port=5001)  # Use different port
```

## 📄 License

MIT License - feel free to use and modify for your projects.

## 🙏 Acknowledgments

Built with:
- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS
- [Font Awesome](https://fontawesome.com/) - Icons
- [Eventbrite API](https://www.eventbrite.com/platform/api)

---

**Built by Rich's AI Agent** | EventRadar v1.0 MVP | February 2026
