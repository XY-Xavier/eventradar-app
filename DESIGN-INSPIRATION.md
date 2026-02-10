# EventRadar Design Aesthetic

## Inspiration Source
**Pinterest Reference:** Plant Nursery Website Design  
**URL:** https://pin.it/4GTNLF8Bg

## Design Philosophy
EventRadar should feel like a **discovery platform** - where events are presented as curated experiences you'd want to explore, not just a functional list.

## Key Design Principles

### 1. **Image-First Cards**
- Large, prominent event images (h-64 = 256px)
- Images are the hero - text supports, doesn't dominate
- Graceful fallbacks with gradient backgrounds + icon
- Hover effect: subtle image scale (1.05x)

### 2. **Warm, Approachable Palette**
- **Primary:** Purple to Indigo gradients (`from-purple-500 to-indigo-600`)
- **Accents:** Emerald for free events, rose for errors
- **Background:** Warm neutral (`#fafaf9`) not stark white
- **Borders:** Subtle gray (`border-gray-100`)

### 3. **Clean Spacing & Breathing Room**
- Generous padding (p-5, p-6, py-8)
- 6-unit gaps between cards
- Rounded corners (rounded-2xl = 16px)
- Cards have room to "breathe"

### 4. **Typography - Inter Font**
- **Font:** Inter (clean, modern, highly readable)
- **Weights:** 300-700 range for hierarchy
- **Sizes:** Conservative - readability over flash
- **Line heights:** Generous (leading-snug for headlines)

### 5. **Card Interactions**
- **Hover:** Lift + shadow increase (`translateY(-8px)`, shadow-2xl)
- **Transitions:** Smooth cubic-bezier easing
- **Image zoom:** Subtle scale on parent card hover
- **Button:** Gradient with glow effect

### 6. **Product-Like Presentation**
- Each card is self-contained
- Clear visual hierarchy: Image → Badge → Title → Details → CTA
- Price badges overlay images (absolute positioning)
- Source tags + date at top of content area

### 7. **Mobile Optimization**
- Responsive grid: 1 → 2 → 3 → 4 columns
- Touch-friendly (48px+ tap targets)
- Sticky header with backdrop blur
- Compact stats on mobile (2-column)

## Color Palette

### Primary
- **Purple:** `#667eea` → `#5568d3` (hover)
- **Indigo:** `#764ba2` → `#63408a` (hover)

### Accents
- **Emerald (free):** `emerald-500`, `emerald-600`
- **Rose (error):** `rose-500`
- **Gray (neutral):** `gray-50` to `gray-900`

### Backgrounds
- **Page:** `#fafaf9` (warm off-white)
- **Cards:** `white`
- **Borders:** `gray-100` (almost invisible)

## Component Styling

### Cards
```css
- Border: 1px solid gray-100
- Radius: rounded-2xl (16px)
- Shadow: shadow-sm (subtle)
- Hover: shadow-2xl + translateY(-8px)
```

### Buttons
```css
- Primary: Purple/indigo gradient
- Padding: px-5 py-2.5
- Radius: rounded-xl
- Shadow: shadow-lg with color glow
- Hover: Darker gradient + larger shadow
```

### Inputs/Selects
```css
- Border: 1px solid gray-200
- Radius: rounded-xl
- Focus: ring-2 purple-500/20 + border-purple-500
```

## Typography Scale
- **Hero (h1):** 2xl (24px), bold, tracking-tight
- **Subtitle:** sm (14px), medium, gray-500
- **Card Title:** base (16px), bold, line-clamp-2
- **Body:** sm (14px), medium, gray-600
- **Labels:** xs (12px), semibold, uppercase, tracking-wide

## Grid Layout
- **Container:** max-w-[1400px] (wide, airy)
- **Padding:** px-6 lg:px-12 (generous horizontal)
- **Columns:** 
  - Mobile: 1 column
  - SM: 2 columns
  - LG: 3 columns
  - XL: 4 columns
- **Gap:** 6 units (24px)

## Animation Details
- **Hover transitions:** 0.3s cubic-bezier(0.4, 0, 0.2, 1)
- **Image scale:** 0.4s cubic-bezier(0.4, 0, 0.2, 1)
- **Notification fade:** 0.3s opacity

## Inspiration Keywords
- **Pinterest-style** discovery
- **Product photography** aesthetic
- **Curated marketplace** feel
- **Warm, inviting** tone
- **Clean, modern** execution
- **Image-driven** storytelling

## Sister Design Language
This aesthetic can extend to other Rich projects:
- Event detail pages
- User profiles
- Content galleries
- Product showcases
- Portfolio sites

**Philosophy:** Make data feel like discovery. Every card should invite exploration.
