# 🚀 EventRadar - Launch Instructions

## Instant Start (2 commands)

```bash
cd /Users/xy/.openclaw/workspace/eventradar
./run.sh
```

Then open: **http://localhost:5000**

## What You'll See

1. **City Selector** at the top (SF, LA, NYC, Chicago)
2. **Stats Dashboard** showing event counts
3. **Event Cards** with networking events (demo data)
4. **Search & Filters** to refine results

## Demo Mode

- App works **immediately** without API keys
- Shows **9 curated events per city** (36 total)
- City-specific venues and locations
- All features fully functional

## Adding Real Data

1. Get Eventbrite API token: https://www.eventbrite.com/platform/api
2. Edit `.env`:
   ```
   EVENTBRITE_TOKEN=YOUR_TOKEN_HERE
   ```
3. Restart: `./run.sh`

## First Time Setup

If `venv/` doesn't exist:
```bash
./setup.sh
./run.sh
```

## Features to Try

- 🌆 **Switch cities** - Select different cities from dropdown
- 🔍 **Search** - Type keywords in search bar
- 💰 **Filter by price** - Free only / Paid events
- 📅 **Filter by time** - Today / This Week / This Month
- 🔄 **Refresh** - Click refresh button for latest data

## Troubleshooting

**Port 5000 in use?**
- Edit `app.py`, line 331: change `port=5000` to `port=5001`

**Dependencies error?**
```bash
rm -rf venv
./setup.sh
```

**App won't start?**
```bash
source venv/bin/activate
python app.py
```

---

**Ready to launch!** The MVP is complete and professional. 🎉
