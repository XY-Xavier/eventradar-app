# EventRadar Deployment

## Production URL
**https://eventradar-app.onrender.com**

## Deployment Details

- **Platform:** Render.com
- **Service ID:** srv-d659q3er433s73et18h0
- **Region:** Oregon
- **Plan:** Free
- **Status:** ✅ Live

## Repository
- **GitHub:** https://github.com/XY-Xavier/eventradar-app
- **Branch:** main
- **Auto-deploy:** Enabled (on commit)

## Build Configuration
- **Environment:** Python
- **Runtime:** Python 3.11.0
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Plan:** starter (free tier)

## Environment Variables
The following environment variables need to be configured in Render Dashboard:
- `EVENTBRITE_TOKEN` - Eventbrite API token
- `MEETUP_KEY` - Meetup API key (optional)

## Deployment History
- **Initial Deploy:** 2026-02-10T02:50:54Z
- **Deploy ID:** dep-d659q3mr433s73et18og
- **Commit:** cecc156344e89b7b2fd6352a58d45dfaef11054a
- **Status:** Live ✅
- **Finished:** 2026-02-10T02:52:29Z

## Access
- **Dashboard:** https://dashboard.render.com/web/srv-d659q3er433s73et18h0
- **SSH:** srv-d659q3er433s73et18h0@ssh.oregon.render.com

## Verification
✅ Tested on 2026-02-10T03:48:24Z - Status 200 OK
✅ Page title: "EventRadar - Bay Area Networking Events"

---
**Deployed by:** Forge (OpenClaw Agent)
**Date:** 2026-02-09 19:48 PST
