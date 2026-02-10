# 🚀 EventRadar - Quick Start Guide

Get up and running in **under 2 minutes**!

## ⚡ Fastest Path (No API Keys Needed)

```bash
cd /Users/xy/.openclaw/workspace/eventradar
./setup.sh
./run.sh
```

Then open: **http://localhost:5000** 🎉

The app will work with **demo data** immediately - no configuration needed!

---

## 📋 Step-by-Step

### 1. Setup (First Time Only)

```bash
./setup.sh
```

This will:
- Create a Python virtual environment
- Install all dependencies (Flask, requests, etc.)
- Create a `.env` configuration file

### 2. Run the App

```bash
./run.sh
```

Or manually:
```bash
source venv/bin/activate
python app.py
```

### 3. Open in Browser

Navigate to: **http://localhost:5000**

You should see:
- Event cards with demo networking events
- Filters for search, price, and time
- Stats dashboard showing event counts

---

## 🔑 Adding Real API Data (Optional)

The app works with demo data out of the box, but you can add real Eventbrite events:

### 1. Get Eventbrite API Token

1. Go to https://www.eventbrite.com/platform/api
2. Log in to your Eventbrite account
3. Go to **Account Settings → App Management**
4. Create a new app
5. Generate a **Private Token**

### 2. Configure

Edit `.env` file:
```bash
EVENTBRITE_TOKEN=YOUR_TOKEN_HERE
```

### 3. Restart the App

```bash
./run.sh
```

The app will now fetch **real events** from Eventbrite!

---

## 🎨 What You Get

### Features Working Out of the Box:
- ✅ Clean, professional UI with Tailwind CSS
- ✅ Event cards with date, location, price, registration links
- ✅ Search and filtering (price, time range)
- ✅ Stats dashboard (total, free, this week)
- ✅ Responsive design (mobile-friendly)
- ✅ Auto-refresh (24-hour cache)
- ✅ Manual refresh button

### Data Sources:
- **Demo Mode** (default): 6 curated networking events
- **Eventbrite API**: Real Bay Area tech/business events (when configured)
- **Meetup API**: Planned (requires OAuth - placeholder for now)
- **Luma Calendar**: Planned (requires scraping - placeholder for now)

---

## 🔧 Configuration

Default settings in `app.py`:

```python
CONFIG = {
    'location': {
        'city': 'San Francisco',
        'latitude': 37.7749,
        'longitude': -122.4194,
        'radius_miles': 25
    },
    'filters': {
        'max_price': 50,
        'days_ahead': 30
    }
}
```

Edit these values to customize location and filters.

---

## 🐛 Troubleshooting

**App won't start?**
```bash
# Make sure you're in the right directory
cd /Users/xy/.openclaw/workspace/eventradar

# Recreate venv if needed
rm -rf venv
./setup.sh
```

**Port 5000 already in use?**

Edit `app.py`, last line:
```python
app.run(debug=True, port=5001)  # Change to any free port
```

**Dependencies error?**
```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

---

## 📂 Project Structure

```
eventradar/
├── app.py              # Flask backend + API integration
├── templates/
│   └── index.html      # Frontend UI (Tailwind CSS)
├── data/
│   └── events_cache.json  # Cached events (auto-generated)
├── venv/               # Python virtual environment
├── .env                # API configuration
├── setup.sh            # First-time setup script
├── run.sh              # Quick start script
└── README.md           # Full documentation
```

---

## ✨ Next Steps

1. **Add real API token** to fetch live Eventbrite events
2. **Customize location** in `app.py` CONFIG
3. **Adjust filters** (price, categories, radius)
4. **Style tweaks** in `templates/index.html`
5. **Deploy** to production (see README.md for deployment options)

---

## 🎯 MVP Complete!

You now have a working networking events dashboard with:
- ✅ Professional UI
- ✅ Multi-source event aggregation (demo + Eventbrite ready)
- ✅ Smart filtering and search
- ✅ Bay Area focus with configurable location
- ✅ Clean, maintainable code

**Time to ship:** ~2 hours ⚡

Built with ❤️ by AI Agent for Rich | Feb 2026
