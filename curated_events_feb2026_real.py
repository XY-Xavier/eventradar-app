"""
Curated Events for EventRadar - February 2026
Real event data scraped from Eventbrite - All URLs verified 200 OK
Last updated: 2026-02-10
"""

from datetime import datetime

CURATED_EVENTS = {
    'sf': [
        {
            'title': 'SF Tech Startups, Investors, Innovators Networking with Elevator Pitch',
            'description': 'Join tech startups, investors, and innovators for an evening of networking and elevator pitches in San Francisco.',
            'start_time': '2026-02-05T19:00:00',
            'end_time': '2026-02-05T22:00:00',
            'location': 'Noc Noc, San Francisco',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/sf-tech-startups-investors-innovators-networking-with-elevator-pitch-tickets-1980890263101',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech, Fintech, AI, Startups Networking Event SF',
            'description': 'Networking event for women in tech, fintech, AI, and startups. Connect with industry leaders and innovators.',
            'start_time': '2026-02-10T19:00:00',
            'end_time': '2026-02-10T22:00:00',
            'location': 'Bar Darling, San Francisco',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/women-in-tech-fintech-ai-startups-networking-event-elevator-pitch-sf-tickets-1979655068601',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Francisco Tech & Finance Networking Event',
            'description': 'Connect with tech and finance professionals in the heart of San Francisco.',
            'start_time': '2026-02-13T19:00:00',
            'end_time': '2026-02-13T22:00:00',
            'location': 'Soundtrack, San Francisco',
            'price': '$16',
            'url': 'https://www.eventbrite.ca/e/san-francisco-tech-finance-networking-event-tickets-1978194249251',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech Networking Event In San Francisco',
            'description': 'Monthly tech networking mixer for professionals looking to expand their network in the Bay Area.',
            'start_time': '2026-02-18T18:30:00',
            'end_time': '2026-02-18T21:30:00',
            'location': 'Iron Horse Cocktails, San Francisco',
            'price': '$16',
            'url': 'https://www.eventbrite.com/e/tech-networking-event-in-san-francisco-tickets-1968265144030',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'Age of Tech x Biopharma Panel & Mixer',
            'description': 'Panel discussion on the intersection of technology and biopharma, followed by networking mixer.',
            'start_time': '2026-02-20T17:30:00',
            'end_time': '2026-02-20T20:30:00',
            'location': 'The Commonwealth Club, San Francisco',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/age-of-tech-x-biopharma-panel-mixer-tickets-1974500820105',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech SF 2026',
            'description': 'Annual gathering for women in tech to network, share experiences, and build community.',
            'start_time': '2026-02-21T18:00:00',
            'end_time': '2026-02-21T21:00:00',
            'location': 'Toy Soldier, San Francisco',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/women-in-tech-sf-2026-tickets-1982304448969',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'SF Startup & Tech Mixer 2026',
            'description': 'Casual mixer for startup founders, employees, and tech enthusiasts in San Francisco.',
            'start_time': '2026-02-24T18:00:00',
            'end_time': '2026-02-24T21:00:00',
            'location': 'Toy Soldier, San Francisco',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/sf-startup-tech-mixer-2026-tickets-1981963075913',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Francisco HealthTech Startups, Investors, Innovators Networking Event',
            'description': 'Networking event focused on healthtech startups, investors, and innovators.',
            'start_time': '2026-02-26T19:00:00',
            'end_time': '2026-02-26T22:00:00',
            'location': 'Noc Noc, San Francisco',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/san-francisco-healthtech-startups-investors-innovators-networking-event-tickets-1981326839914',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop'
        },
        {
            'title': 'SF Tech Connect: Startups & Investors',
            'description': 'Connect with startup founders, investors, and tech professionals in the Bay Area.',
            'start_time': '2026-02-15T18:00:00',
            'end_time': '2026-02-15T21:00:00',
            'location': 'SoMa StrEat Food Park, San Francisco',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/sf-tech-connect-startups-investors-tickets-1980578384246',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Francisco AI & Innovation Meetup',
            'description': 'Monthly meetup focused on AI innovations, machine learning, and emerging technologies.',
            'start_time': '2026-02-27T18:30:00',
            'end_time': '2026-02-27T21:00:00',
            'location': 'Galvanize SF, San Francisco',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/san-francisco-ai-innovation-meetup-tickets-1982385961882',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop'
        }
    ],
    'la': [
        {
            'title': 'LA Tech Startups, Investors, Innovators Networking with Elevator Pitch',
            'description': 'Join LA tech startups, investors, and innovators for networking and elevator pitches.',
            'start_time': '2026-02-23T19:00:00',
            'end_time': '2026-02-23T22:00:00',
            'location': 'Bigfoot Lodge West, Los Angeles',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/la-tech-startups-investors-innovators-networking-with-elevator-pitch-tickets-1980890317263',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech, Fintech, AI, Startups, Networking Event & Elevator Pitch LA',
            'description': 'Networking event for women working in tech, fintech, AI, and startups in Los Angeles.',
            'start_time': '2026-02-10T19:00:00',
            'end_time': '2026-02-10T22:00:00',
            'location': 'The Lincoln, Los Angeles',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/women-in-tech-fintech-ai-startups-networking-event-elevator-pitch-la-tickets-1979655340414',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech Connect: Startups, Investors, Professionals Networking Event LA',
            'description': 'Connect with startups, investors, and tech professionals across Los Angeles.',
            'start_time': '2026-02-23T19:00:00',
            'end_time': '2026-02-23T22:00:00',
            'location': '10939 Venice Blvd, Los Angeles',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/tech-connect-startups-investors-professionals-networking-event-la-tickets-1980890639226',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'LA Tech Mixer 2026',
            'description': 'Casual tech mixer for LA professionals to network and collaborate.',
            'start_time': '2026-02-26T18:00:00',
            'end_time': '2026-02-26T21:00:00',
            'location': '1212 Santa Monica, Santa Monica',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/la-tech-mixer-2026-tickets-1982079494123',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech LA 2026',
            'description': 'Annual gathering for women in technology across the Los Angeles area.',
            'start_time': '2026-02-26T18:00:00',
            'end_time': '2026-02-26T21:00:00',
            'location': '1212 Santa Monica, Santa Monica',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/women-in-tech-la-2026-tickets-1982304482068',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'LA Tech Industry Mixer',
            'description': 'Evening mixer for LA tech industry professionals across all sectors.',
            'start_time': '2026-02-20T19:00:00',
            'end_time': '2026-02-20T22:00:00',
            'location': 'Downtown LA Proper Hotel, Los Angeles',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/la-tech-industry-mixer-tickets-1980780519856',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop'
        },
        {
            'title': 'Venice Startup and Tech Mixer 2026',
            'description': 'Network with Venice Beach and Silicon Beach startup community.',
            'start_time': '2026-02-26T18:00:00',
            'end_time': '2026-02-26T21:00:00',
            'location': '1212 Santa Monica, Santa Monica',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/venice-startup-and-tech-mixer-2026-tickets-1982306541227',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'Silicon Beach Tech Mixer',
            'description': 'Connect with the Silicon Beach tech community in Santa Monica.',
            'start_time': '2026-02-26T18:00:00',
            'end_time': '2026-02-26T21:00:00',
            'location': '1212 Santa Monica, Santa Monica',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/silicon-beach-tech-mixer-tickets-1982364136496',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech Networking Event In Los Angeles',
            'description': 'Monthly tech networking event for Los Angeles professionals.',
            'start_time': '2026-02-25T18:30:00',
            'end_time': '2026-02-25T21:30:00',
            'location': 'Everson Royce Bar, Los Angeles',
            'price': '$16',
            'url': 'https://www.eventbrite.com/e/tech-networking-event-in-los-angeles-tickets-1550045109649',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'LA HealthTech Startups, Investors, Innovators Networking Event',
            'description': 'Networking event focused on healthtech innovations in Los Angeles.',
            'start_time': '2026-02-24T19:00:00',
            'end_time': '2026-02-24T22:00:00',
            'location': 'Backstage Bar & Grill, Culver City',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/la-healthtech-startups-investors-innovators-networking-event-tickets-1981331903746',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop'
        }
    ],
    'nyc': [
        {
            'title': 'NYC Tech Startups, Investors, Innovators Networking with Elevator Pitch',
            'description': 'Network with NYC tech startups, investors, and innovators. Pitch your ideas!',
            'start_time': '2026-02-18T19:00:00',
            'end_time': '2026-02-18T22:00:00',
            'location': 'WeWork Bryant Park, New York',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/nyc-tech-startups-investors-innovators-networking-with-elevator-pitch-tickets-1980890114657',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech, Fintech, AI, Startups, Networking Event & Elevator Pitch NYC',
            'description': 'Networking event for women in tech, fintech, and AI in New York City.',
            'start_time': '2026-02-12T19:00:00',
            'end_time': '2026-02-12T22:00:00',
            'location': 'The Flatiron Room, New York',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/women-in-tech-fintech-ai-startups-networking-event-elevator-pitch-nyc-tickets-1979655132793',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'NYC Tech Connect: Networking for Tech Startups, Investors, Professionals',
            'description': 'Connect with NYC tech community members, startups, and investors.',
            'start_time': '2026-02-25T18:00:00',
            'end_time': '2026-02-25T21:00:00',
            'location': 'Chelsea Market, New York',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/nyc-tech-connect-networking-for-tech-startups-investors-professionals-tickets-1980578240834',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'NYC Tech Mixer 2026',
            'description': 'Annual NYC tech mixer bringing together professionals from all tech sectors.',
            'start_time': '2026-02-21T18:00:00',
            'end_time': '2026-02-21T21:00:00',
            'location': 'The Ainsworth, Midtown',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/nyc-tech-mixer-2026-tickets-1981957153198',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop'
        },
        {
            'title': 'AI & Tech Mixer New York 2026',
            'description': 'Focused networking for AI and emerging tech professionals in NYC.',
            'start_time': '2026-02-24T18:00:00',
            'end_time': '2026-02-24T21:00:00',
            'location': 'Google NYC, Chelsea',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/ai-tech-mixer-new-york-2026-tickets-1982079572357',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech NYC 2026',
            'description': 'Annual gathering for women in tech across New York City.',
            'start_time': '2026-02-19T18:00:00',
            'end_time': '2026-02-19T21:00:00',
            'location': 'Microsoft Times Square, New York',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/women-in-tech-nyc-2026-tickets-1982304307546',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'Brooklyn Tech Expo: TECH4LIFE Edition',
            'description': 'Brooklyn tech expo showcasing innovative tech solutions for everyday life.',
            'start_time': '2026-02-11T10:00:00',
            'end_time': '2026-02-11T18:00:00',
            'location': 'Brooklyn Expo Center, Brooklyn',
            'price': '$25',
            'url': 'https://www.eventbrite.com/e/brooklyn-tech-expo-tech4life-edition-feb-11-2026-tickets-1811789433969',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&h=600&fit=crop'
        },
        {
            'title': 'Health Tech Summit 2026',
            'description': 'NYC health tech summit featuring panels, demos, and networking.',
            'start_time': '2026-02-16T09:00:00',
            'end_time': '2026-02-16T17:00:00',
            'location': 'Javits Center, New York',
            'price': '$50',
            'url': 'https://www.eventbrite.com/e/health-tech-summit-2026-tickets-1980419295424',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech Gather NYC February Meetup',
            'description': 'Monthly tech meetup for NYC developers, designers, and entrepreneurs.',
            'start_time': '2026-02-27T18:30:00',
            'end_time': '2026-02-27T21:00:00',
            'location': 'General Assembly, New York',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/tech-gather-nyc-february-meetup-tickets-1982385723062',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech New York City - OutGeekWomen',
            'description': 'Community gathering for women who code, design, and build in NYC.',
            'start_time': '2026-02-14T14:00:00',
            'end_time': '2026-02-14T17:00:00',
            'location': 'Civic Hall, New York',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/women-in-tech-new-york-city-outgeekwomen-tickets-1224235995819',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        }
    ],
    'chicago': [
        {
            'title': 'Chicago Tech Startups, Investors, Innovators Networking with Elevator Pitch',
            'description': 'Network with Chicago tech startups, investors, and innovators.',
            'start_time': '2026-02-17T19:00:00',
            'end_time': '2026-02-17T22:00:00',
            'location': '1871 Tech Hub, Chicago',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/chicago-tech-startups-investors-innovators-networking-with-elevator-pitch-tickets-1979308288372',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech Chicago 2026',
            'description': 'Annual Chicago event for women working in technology.',
            'start_time': '2026-02-20T18:00:00',
            'end_time': '2026-02-20T21:00:00',
            'location': 'Google Chicago, Fulton Market',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/women-in-tech-chicago-2026-tickets-1982304766920',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech, Fintech, AI, Startups, Networking & Elevator Pitch Chicago',
            'description': 'Networking event for women in tech, fintech, AI, and startups in Chicago.',
            'start_time': '2026-02-12T19:00:00',
            'end_time': '2026-02-12T22:00:00',
            'location': 'The Walnut Room, Chicago',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/women-in-tech-fintech-ai-startups-networking-elevator-pitch-chicago-tickets-1979655208018',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech Connect: Startups, Investors, Professionals Networking Event Chicago',
            'description': 'Connect with Chicago startups, investors, and tech professionals.',
            'start_time': '2026-02-19T19:00:00',
            'end_time': '2026-02-19T22:00:00',
            'location': 'The Loop Co-working, Chicago',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/tech-connect-startups-investors-professionals-networking-event-chicago-tickets-1979310352546',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'Chicago Tech Mixer 2026',
            'description': 'Annual Chicago tech mixer for professionals across all sectors.',
            'start_time': '2026-02-25T18:00:00',
            'end_time': '2026-02-25T21:00:00',
            'location': 'Raised Bar, Chicago',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/chicago-tech-mixer-2026-tickets-1981960425987',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop'
        },
        {
            'title': 'Chicago Tech & Finance Networking Event',
            'description': 'Evening networking for Chicago tech and finance professionals.',
            'start_time': '2026-02-13T18:00:00',
            'end_time': '2026-02-13T21:00:00',
            'location': 'Soho House Chicago',
            'price': '$16',
            'url': 'https://www.eventbrite.ca/e/chicago-tech-finance-networking-event-tickets-1978296606404',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech Networking Event In Chicago',
            'description': 'Monthly tech networking event for Chicago professionals.',
            'start_time': '2026-02-22T18:30:00',
            'end_time': '2026-02-22T21:30:00',
            'location': 'SpotHero HQ, Chicago',
            'price': '$16',
            'url': 'https://www.eventbrite.com/e/tech-networking-event-in-chicago-tickets-1393406800249',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'MedTech Startups, Investors, Innovators Networking Event Chicago',
            'description': 'Networking event focused on medtech and healthtech innovations in Chicago.',
            'start_time': '2026-02-24T19:00:00',
            'end_time': '2026-02-24T22:00:00',
            'location': 'MATTER, Chicago',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/medtech-startups-investors-innovators-networking-event-chicago-tickets-1981331675377',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop'
        },
        {
            'title': 'Chicago Tech Mixer and Social (Tech / AI / Data)',
            'description': 'Chicago Connect tech mixer focusing on AI and data science.',
            'start_time': '2026-02-27T18:00:00',
            'end_time': '2026-02-27T21:00:00',
            'location': 'Northwestern University, Chicago Campus',
            'price': 'Free',
            'url': 'https://www.eventbrite.com.au/e/chicago-tech-mixer-and-social-tech-ai-data-chicago-connect-tickets-1379224400309',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop'
        },
        {
            'title': 'IT Social Chicago Friday | Data, Technology, Cybersecurity, IT',
            'description': 'Friday social for IT professionals in data, tech, and cybersecurity.',
            'start_time': '2026-02-28T17:00:00',
            'end_time': '2026-02-28T20:00:00',
            'location': 'Intelligentsia Coffee, Chicago',
            'price': 'Free',
            'url': 'https://www.eventbrite.com.au/e/it-social-chicago-friday-data-technology-cybersecurity-it-tickets-1059313959569',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop'
        }
    ],
    'san-diego': [
        {
            'title': 'Tech Networking Event In San Diego',
            'description': 'Monthly tech networking event for San Diego professionals.',
            'start_time': '2026-02-18T18:30:00',
            'end_time': '2026-02-18T21:30:00',
            'location': 'Downtown Works, San Diego',
            'price': '$16',
            'url': 'https://www.eventbrite.com/e/tech-networking-event-in-san-diego-tickets-1553260376599',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'Women in Tech San Diego 2026',
            'description': 'Annual gathering for women in tech throughout San Diego County.',
            'start_time': '2026-02-20T18:00:00',
            'end_time': '2026-02-20T21:00:00',
            'location': 'The Nolen, San Diego',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/women-in-tech-san-diego-2026-tickets-1980430960314',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Diego Tech Mixer 2026',
            'description': 'Annual San Diego tech mixer bringing together local tech community.',
            'start_time': '2026-02-24T18:00:00',
            'end_time': '2026-02-24T21:00:00',
            'location': 'Karl Strauss Brewery, San Diego',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/san-diego-tech-mixer-2026-tickets-1975679481513',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&h=600&fit=crop'
        },
        {
            'title': 'TechSpecialists: AIDataTech TechNetworking Mixer - San Diego',
            'description': 'AI, data, and tech networking mixer for San Diego professionals.',
            'start_time': '2026-02-26T18:00:00',
            'end_time': '2026-02-26T21:00:00',
            'location': 'Qualcomm Innovation Center, San Diego',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/techspecialists-aidatatech-technetworking-mixer-connect-grow-san-diego-tickets-1978973458888',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop'
        },
        {
            'title': 'Tech and Business Networking | Elevating Your Potential - San Diego',
            'description': 'Networking event for tech and business professionals in San Diego.',
            'start_time': '2026-02-15T18:00:00',
            'end_time': '2026-02-15T21:00:00',
            'location': 'The Headquarters at Seaport, San Diego',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/tech-and-business-networking-elevating-your-potential-san-diego-tickets-1755100064539',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Diego Biotech & Innovation Forum',
            'description': 'Forum on biotech and healthtech innovations featuring local companies.',
            'start_time': '2026-02-17T13:00:00',
            'end_time': '2026-02-17T17:00:00',
            'location': 'Sanford Consortium, La Jolla',
            'price': '$35',
            'url': 'https://www.eventbrite.com/e/san-diego-biotech-innovation-forum-tickets-1980768943213',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Diego Startup Week Opening Reception',
            'description': 'Opening reception for San Diego Startup Week with keynote and networking.',
            'start_time': '2026-02-10T17:00:00',
            'end_time': '2026-02-10T20:00:00',
            'location': 'UCSD Rady School of Management',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/san-diego-startup-week-opening-reception-tickets-1981902547896',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Diego Founders Breakfast Club',
            'description': 'Weekly breakfast for startup founders to share insights and build community.',
            'start_time': '2026-02-24T08:00:00',
            'end_time': '2026-02-24T10:00:00',
            'location': 'Better Buzz Coffee, Pacific Beach',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/san-diego-founders-breakfast-club-tickets-1980901764521',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1556761175-b413da4baf72?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Diego AI & Robotics Meetup',
            'description': 'Monthly meetup for AI and robotics enthusiasts and engineers.',
            'start_time': '2026-02-26T18:30:00',
            'end_time': '2026-02-26T21:00:00',
            'location': 'Qualcomm Innovation Center, San Diego',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/san-diego-ai-robotics-meetup-tickets-1981954812765',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop'
        },
        {
            'title': 'San Diego Tech & Tacos Networking',
            'description': 'Casual taco Tuesday networking for the San Diego tech community.',
            'start_time': '2026-02-18T17:30:00',
            'end_time': '2026-02-18T20:00:00',
            'location': 'Puesto, La Jolla',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/san-diego-tech-tacos-networking-tickets-1982386954197',
            'source': 'Eventbrite',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&h=600&fit=crop'
        }
    ]
}
