# EventRadar - Networking Events Dashboard

## Project Requirements (Updated 2026-02-09 16:18 PST)

### Core Functionality
Web-based dashboard showing local networking events in **4 major cities**.

### Cities (CRITICAL)
1. **Los Angeles** (34.0522, -118.2437)
2. **New York City** (40.7128, -74.0060)
3. **Chicago** (41.8781, -87.6298)
4. **San Francisco / Bay Area** (37.7749, -122.4194)

**UI:** City selector dropdown or tabs at top. Default to SF. Store preference in localStorage.

### Data Sources
- Eventbrite API
- Meetup.com API
- Luma calendar (if available)

Minimum: 2 sources working (Eventbrite + Meetup).

### Event Filters
- **Type:** Tech, startup, business networking
- **Timeframe:** Next 30 days from today
- **Radius:** 25 miles from city center
- **Price:** Free OR under $50

### UI/UX
- Clean event cards showing:
  - Event title
  - Date & time
  - Location (venue name + address)
  - Price
  - Link to register/RSVP
- Professional design (Tailwind CSS)
- Mobile-responsive
- Fast load times

### Technical Stack
- **Backend:** Python Flask
- **Frontend:** HTML + JavaScript + Tailwind CSS
- **APIs:** Eventbrite, Meetup
- **Auto-refresh:** Daily data pull (cron or scheduler)

### Deliverables
- [ ] Working web app at `localhost:5000`
- [ ] Multi-city support (LA, NYC, Chicago, SF)
- [ ] Event cards with real data from APIs
- [ ] Clean, professional UI
- [ ] README with setup instructions
- [ ] API keys documentation

### Timeline
**Target:** 2-3 hours for MVP
**Status:** In progress (sub-agent building)

### Non-Goals (for MVP)
- User accounts / authentication
- Event bookmarking / favorites
- Calendar integration
- Email notifications
- Advanced search/filters

(Can add later if needed)

---

**Working Directory:** `/Users/xy/.openclaw/workspace/eventradar/`  
**Owner:** Richard B  
**Lead:** Professor X  
**Builder:** Sub-agent (session: 98560366-faf9-4a03-a740-228629ece777)
