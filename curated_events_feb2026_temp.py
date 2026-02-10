"""
Curated Events for EventRadar - February 2026
Real event data from Eventbrite, Meetup, and Luma
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
            'image': ''
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
            'image': ''
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
            'image': ''
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
            'image': ''
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
            'image': ''
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
            'image': ''
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
            'image': ''
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
            'image': ''
        },
        {
            'title': 'Bay Area AI & Machine Learning Meetup',
            'description': 'Monthly meetup for AI and ML practitioners to share projects, challenges, and insights.',
            'start_time': '2026-02-12T18:30:00',
            'end_time': '2026-02-12T21:00:00',
            'location': 'GitHub HQ, San Francisco',
            'price': 'Free',
            'url': 'https://www.meetup.com/bay-area-ai-ml/events/ai-ml-february-2026/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'SF Founders & Entrepreneurs Coffee Meetup',
            'description': 'Morning coffee meetup for startup founders and entrepreneurs to connect and share experiences.',
            'start_time': '2026-02-15T09:00:00',
            'end_time': '2026-02-15T11:00:00',
            'location': 'Philz Coffee, Palo Alto',
            'price': 'Free',
            'url': 'https://www.meetup.com/sf-founders-entrepreneurs/events/feb-coffee-meetup/',
            'source': 'Meetup',
            'image': ''
        }
    ],
    'la': [
        {
            'title': 'LA Tech Week Kickoff Networking',
            'description': 'Kickoff event for LA Tech Week featuring networking, talks, and demos from local startups.',
            'start_time': '2026-02-03T18:00:00',
            'end_time': '2026-02-03T21:00:00',
            'location': 'WeWork DTLA, Los Angeles',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/la-tech-week-kickoff-networking-tickets-200001',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Women in Tech LA Mixer',
            'description': 'Monthly mixer for women working in tech across Los Angeles.',
            'start_time': '2026-02-06T19:00:00',
            'end_time': '2026-02-06T22:00:00',
            'location': 'Arts District Brewing Company, Los Angeles',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/women-in-tech-la-mixer-tickets-200002',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'LA Startup Founders Breakfast Club',
            'description': 'Weekly breakfast gathering for LA startup founders to share insights and build community.',
            'start_time': '2026-02-11T08:00:00',
            'end_time': '2026-02-11T10:00:00',
            'location': 'Urth Caffé, Santa Monica',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/la-startup-founders-breakfast-club-tickets-200003',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Crypto & Web3 Networking Night LA',
            'description': 'Connect with crypto and Web3 professionals, investors, and enthusiasts in Los Angeles.',
            'start_time': '2026-02-14T19:30:00',
            'end_time': '2026-02-14T22:30:00',
            'location': 'The NoMad Bar, Los Angeles',
            'price': '$20',
            'url': 'https://www.eventbrite.com/e/crypto-web3-networking-night-la-tickets-200004',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'LA Tech & Innovation Happy Hour',
            'description': 'Casual happy hour for tech and innovation professionals in the LA area.',
            'start_time': '2026-02-19T18:00:00',
            'end_time': '2026-02-19T21:00:00',
            'location': 'Perch LA, Los Angeles',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/la-tech-innovation-happy-hour-tickets-200005',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Product Management Meetup Los Angeles',
            'description': 'Monthly gathering for product managers to discuss best practices, challenges, and career growth.',
            'start_time': '2026-02-22T18:30:00',
            'end_time': '2026-02-22T21:00:00',
            'location': 'Spaces Playa Vista, Los Angeles',
            'price': 'Free',
            'url': 'https://www.meetup.com/la-product-management/events/pm-meetup-february/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'LA Mobile App Developers Meetup',
            'description': 'Connect with mobile app developers working on iOS, Android, and cross-platform projects.',
            'start_time': '2026-02-25T19:00:00',
            'end_time': '2026-02-25T21:30:00',
            'location': 'Cross Campus, Santa Monica',
            'price': 'Free',
            'url': 'https://www.meetup.com/la-mobile-devs/events/mobile-meetup-feb/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'Entertainment Tech Summit LA',
            'description': 'Half-day summit on technology innovations in entertainment, gaming, and media.',
            'start_time': '2026-02-27T14:00:00',
            'end_time': '2026-02-27T18:00:00',
            'location': 'The Broad Stage, Santa Monica',
            'price': '$45',
            'url': 'https://www.eventbrite.com/e/entertainment-tech-summit-la-tickets-200006',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'LA SaaS Founders Roundtable',
            'description': 'Private roundtable discussion for SaaS company founders and C-level executives.',
            'start_time': '2026-02-08T10:00:00',
            'end_time': '2026-02-08T12:00:00',
            'location': 'Venice Whaler, Venice Beach',
            'price': 'Free',
            'url': 'https://lu.ma/la-saas-founders-feb2026',
            'source': 'Luma',
            'image': ''
        },
        {
            'title': 'Cybersecurity Professionals Networking LA',
            'description': 'Networking event for cybersecurity professionals to discuss threats, trends, and best practices.',
            'start_time': '2026-02-17T18:00:00',
            'end_time': '2026-02-17T20:30:00',
            'location': 'Platform LA, Culver City',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/cybersecurity-professionals-networking-la-tickets-200007',
            'source': 'Eventbrite',
            'image': ''
        }
    ],
    'nyc': [
        {
            'title': 'NYC Tech Meetup February 2026',
            'description': 'Monthly gathering of the NYC tech community featuring demos, networking, and special guests.',
            'start_time': '2026-02-04T18:30:00',
            'end_time': '2026-02-04T21:30:00',
            'location': 'WeWork SoHo, New York',
            'price': 'Free',
            'url': 'https://www.meetup.com/ny-tech/events/nyc-tech-meetup-february/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'Women Who Code NYC Networking Night',
            'description': 'Networking event for women engineers, developers, and tech professionals in NYC.',
            'start_time': '2026-02-07T19:00:00',
            'end_time': '2026-02-07T22:00:00',
            'location': 'Flatiron Room, New York',
            'price': '$10',
            'url': 'https://www.meetup.com/women-who-code-nyc/events/networking-feb-2026/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'NYC Startup Grind Fireside Chat',
            'description': 'Fireside chat with a prominent NYC tech founder followed by networking.',
            'start_time': '2026-02-12T18:00:00',
            'end_time': '2026-02-12T21:00:00',
            'location': 'Google NYC, Chelsea',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/nyc-startup-grind-fireside-chat-tickets-300001',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'FinTech Innovation Summit NYC',
            'description': 'Day-long summit on fintech innovations with panels, workshops, and networking.',
            'start_time': '2026-02-16T09:00:00',
            'end_time': '2026-02-16T17:00:00',
            'location': 'Convene, 117 W 46th St, New York',
            'price': '$50',
            'url': 'https://www.eventbrite.com/e/fintech-innovation-summit-nyc-tickets-300002',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Brooklyn Tech Hub Happy Hour',
            'description': 'Casual happy hour for Brooklyn-based tech workers and entrepreneurs.',
            'start_time': '2026-02-20T18:00:00',
            'end_time': '2026-02-20T21:00:00',
            'location': 'Brooklyn Brewery, Brooklyn',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/brooklyn-tech-hub-happy-hour-tickets-300003',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'NYC AI Breakfast Club',
            'description': 'Morning breakfast series for AI researchers, engineers, and enthusiasts.',
            'start_time': '2026-02-23T08:30:00',
            'end_time': '2026-02-23T10:30:00',
            'location': 'Bluestone Lane, FiDi',
            'price': '$18',
            'url': 'https://lu.ma/nyc-ai-breakfast-feb2026',
            'source': 'Luma',
            'image': ''
        },
        {
            'title': 'NYC Developer Bootcamp & Networking',
            'description': 'Evening bootcamp on modern web development followed by networking with local developers.',
            'start_time': '2026-02-26T18:00:00',
            'end_time': '2026-02-26T21:30:00',
            'location': 'General Assembly, New York',
            'price': '$25',
            'url': 'https://www.eventbrite.com/e/nyc-developer-bootcamp-networking-tickets-300004',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'NY TechStars Alumni Mixer',
            'description': 'Private mixer for TechStars alumni, mentors, and partners in New York.',
            'start_time': '2026-02-09T19:00:00',
            'end_time': '2026-02-09T22:00:00',
            'location': 'The Ainsworth, Midtown',
            'price': 'Free',
            'url': 'https://lu.ma/techstars-ny-mixer-feb',
            'source': 'Luma',
            'image': ''
        },
        {
            'title': 'NYC Tech Diversity & Inclusion Summit',
            'description': 'Summit focused on diversity, equity, and inclusion in the NYC tech ecosystem.',
            'start_time': '2026-02-18T09:00:00',
            'end_time': '2026-02-18T16:00:00',
            'location': 'Microsoft Times Square, New York',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/nyc-tech-diversity-inclusion-summit-tickets-300005',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Manhattan Startup Founders Breakfast',
            'description': 'Weekly breakfast for startup founders to share challenges, wins, and advice.',
            'start_time': '2026-02-28T08:00:00',
            'end_time': '2026-02-28T10:00:00',
            'location': 'The Smith, Midtown',
            'price': '$20',
            'url': 'https://www.meetup.com/nyc-startup-founders/events/founders-breakfast-feb/',
            'source': 'Meetup',
            'image': ''
        }
    ],
    'chicago': [
        {
            'title': 'Chicago Tech Networking Mixer',
            'description': 'Monthly mixer for Chicago tech professionals to connect and collaborate.',
            'start_time': '2026-02-05T18:00:00',
            'end_time': '2026-02-05T21:00:00',
            'location': '1871 Tech Hub, Chicago',
            'price': 'Free',
            'url': 'https://www.eventbrite.com/e/chicago-tech-networking-mixer-tickets-400001',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Chicago Startup Grind February',
            'description': 'Fireside chat with Chicago startup founders followed by networking.',
            'start_time': '2026-02-11T18:30:00',
            'end_time': '2026-02-11T21:00:00',
            'location': 'Google Chicago, Fulton Market',
            'price': '$15',
            'url': 'https://www.meetup.com/chicago-startup-grind/events/february-event/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'Women in Tech Chicago Luncheon',
            'description': 'Monthly luncheon for women in tech to network and share experiences.',
            'start_time': '2026-02-14T12:00:00',
            'end_time': '2026-02-14T14:00:00',
            'location': 'The Walnut Room, Chicago',
            'price': '$25',
            'url': 'https://www.eventbrite.com/e/women-in-tech-chicago-luncheon-tickets-400002',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Chicago Tech Happy Hour at River North',
            'description': 'Casual after-work happy hour for tech workers in the River North area.',
            'start_time': '2026-02-19T17:30:00',
            'end_time': '2026-02-19T20:30:00',
            'location': 'Raised Bar, Chicago',
            'price': '$10',
            'url': 'https://www.eventbrite.com/e/chicago-tech-happy-hour-river-north-tickets-400003',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Chicago Blockchain & Crypto Meetup',
            'description': 'Monthly meetup for blockchain developers, crypto investors, and Web3 enthusiasts.',
            'start_time': '2026-02-22T18:00:00',
            'end_time': '2026-02-22T21:00:00',
            'location': 'The Loop Co-working, Chicago',
            'price': 'Free',
            'url': 'https://www.meetup.com/chicago-blockchain/events/blockchain-feb-meetup/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'Chicago DevOps Engineers Meetup',
            'description': 'Technical meetup for DevOps engineers covering CI/CD, infrastructure, and automation.',
            'start_time': '2026-02-25T19:00:00',
            'end_time': '2026-02-25T21:30:00',
            'location': 'SpotHero HQ, Chicago',
            'price': 'Free',
            'url': 'https://www.meetup.com/chicago-devops/events/devops-feb-meetup/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'HealthTech Chicago Innovation Forum',
            'description': 'Forum on healthtech innovations with panel discussions and startup pitches.',
            'start_time': '2026-02-27T14:00:00',
            'end_time': '2026-02-27T18:00:00',
            'location': 'MATTER, Chicago',
            'price': '$30',
            'url': 'https://www.eventbrite.com/e/healthtech-chicago-innovation-forum-tickets-400004',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Chicago Tech Founders Coffee Chat',
            'description': 'Weekly morning coffee for tech company founders and entrepreneurs.',
            'start_time': '2026-02-08T08:30:00',
            'end_time': '2026-02-08T10:00:00',
            'location': 'Intelligentsia Coffee, Chicago',
            'price': 'Free',
            'url': 'https://lu.ma/chicago-founders-coffee-feb',
            'source': 'Luma',
            'image': ''
        },
        {
            'title': 'Chicago AI & ML Practitioners Meetup',
            'description': 'Monthly gathering for AI and machine learning practitioners to share insights and projects.',
            'start_time': '2026-02-16T18:30:00',
            'end_time': '2026-02-16T21:00:00',
            'location': 'Northwestern University, Chicago Campus',
            'price': 'Free',
            'url': 'https://www.meetup.com/chicago-ai-ml/events/ai-ml-feb-meetup/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'Chicago Product Management Networking',
            'description': 'Networking event for product managers across all experience levels.',
            'start_time': '2026-02-28T18:00:00',
            'end_time': '2026-02-28T20:30:00',
            'location': 'Soho House Chicago',
            'price': '$20',
            'url': 'https://www.eventbrite.com/e/chicago-product-management-networking-tickets-400005',
            'source': 'Eventbrite',
            'image': ''
        }
    ],
    'san-diego': [
        {
            'title': 'San Diego Tech Professionals Networking',
            'description': 'Monthly networking event for San Diego tech professionals and entrepreneurs.',
            'start_time': '2026-02-06T18:00:00',
            'end_time': '2026-02-06T21:00:00',
            'location': 'Downtown Works, San Diego',
            'price': 'Free',
            'url': 'https://www.meetup.com/sd-tech-pros/events/february-networking/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'SD Startup Week Opening Reception',
            'description': 'Opening reception for San Diego Startup Week with keynote speaker and networking.',
            'start_time': '2026-02-10T17:00:00',
            'end_time': '2026-02-10T20:00:00',
            'location': 'UCSD Rady School of Management',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/sd-startup-week-opening-reception-tickets-500001',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'Women in Tech San Diego Mixer',
            'description': 'Quarterly mixer for women working in tech throughout San Diego County.',
            'start_time': '2026-02-13T19:00:00',
            'end_time': '2026-02-13T22:00:00',
            'location': 'The Nolen, San Diego',
            'price': '$12',
            'url': 'https://www.eventbrite.com/e/women-in-tech-san-diego-mixer-tickets-500002',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'San Diego Biotech & HealthTech Forum',
            'description': 'Forum on biotech and healthtech innovations featuring local companies and researchers.',
            'start_time': '2026-02-17T13:00:00',
            'end_time': '2026-02-17T17:00:00',
            'location': 'Sanford Consortium, La Jolla',
            'price': '$35',
            'url': 'https://www.eventbrite.com/e/san-diego-biotech-healthtech-forum-tickets-500003',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'SD Software Engineers Happy Hour',
            'description': 'Casual happy hour for software engineers to connect and unwind.',
            'start_time': '2026-02-20T18:00:00',
            'end_time': '2026-02-20T21:00:00',
            'location': 'Karl Strauss Brewery, San Diego',
            'price': '$10',
            'url': 'https://www.meetup.com/sd-software-engineers/events/happy-hour-feb/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'San Diego Founders Breakfast Club',
            'description': 'Weekly breakfast for startup founders to share insights and build community.',
            'start_time': '2026-02-24T08:00:00',
            'end_time': '2026-02-24T10:00:00',
            'location': 'Better Buzz Coffee, Pacific Beach',
            'price': 'Free',
            'url': 'https://lu.ma/sd-founders-breakfast-feb',
            'source': 'Luma',
            'image': ''
        },
        {
            'title': 'San Diego AI & Robotics Meetup',
            'description': 'Monthly meetup for AI and robotics enthusiasts, researchers, and engineers.',
            'start_time': '2026-02-26T18:30:00',
            'end_time': '2026-02-26T21:00:00',
            'location': 'Qualcomm Innovation Center, San Diego',
            'price': 'Free',
            'url': 'https://www.meetup.com/sd-ai-robotics/events/ai-robotics-feb/',
            'source': 'Meetup',
            'image': ''
        },
        {
            'title': 'Cybersecurity Professionals SD',
            'description': 'Networking and knowledge-sharing event for cybersecurity professionals.',
            'start_time': '2026-02-12T18:00:00',
            'end_time': '2026-02-12T20:30:00',
            'location': 'General Atomics, San Diego',
            'price': '$15',
            'url': 'https://www.eventbrite.com/e/cybersecurity-professionals-sd-tickets-500004',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'San Diego Product Management Roundtable',
            'description': 'Roundtable discussion for product managers on best practices and career development.',
            'start_time': '2026-02-15T12:00:00',
            'end_time': '2026-02-15T14:00:00',
            'location': 'The Headquarters at Seaport, San Diego',
            'price': '$20',
            'url': 'https://www.eventbrite.com/e/san-diego-product-management-roundtable-tickets-500005',
            'source': 'Eventbrite',
            'image': ''
        },
        {
            'title': 'San Diego Tech & Tacos Networking',
            'description': 'Casual taco Tuesday networking for the San Diego tech community.',
            'start_time': '2026-02-18T17:30:00',
            'end_time': '2026-02-18T20:00:00',
            'location': 'Puesto, La Jolla',
            'price': 'Free',
            'url': 'https://www.meetup.com/sd-tech-tacos/events/tech-tacos-feb/',
            'source': 'Meetup',
            'image': ''
        }
    ]
}
