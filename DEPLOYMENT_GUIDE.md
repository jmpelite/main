# JMP Coaching Website Deployment Guide

## Quick Start
1. Clone or download the project files
2. Install dependencies: `npm install`
3. Start development server: `npm start`
4. Build for production: `npm run build`

## File Structure
```
jmp-coaching/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Hero.js
│   │   ├── About.js
│   │   ├── Credentials.js
│   │   ├── Tips.js
│   │   ├── Testimonials.js
│   │   ├── Contact.js
│   │   └── Footer.js
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
├── tailwind.config.js
├── postcss.config.js
├── netlify.toml (for Netlify)
└── vercel.json (for Vercel)
```

## Deployment Options

### Option 1: Netlify (Recommended for beginners)
1. Push your code to GitHub/GitLab
2. Connect your repo to Netlify
3. Build settings: 
   - Build command: `npm run build`
   - Publish directory: `build`
4. Deploy automatically on git push

### Option 2: Vercel (Recommended for React apps)
1. Push your code to GitHub/GitLab
2. Import project to Vercel
3. Vercel auto-detects React settings
4. Deploy automatically on git push

### Option 3: Manual Static Deployment
1. Run `npm run build`
2. Upload the `build` folder contents to any web host
3. Ensure your host redirects all routes to index.html

## Environment Setup
1. Node.js 16+ required
2. Install dependencies: `npm install`
3. Development: `npm start` (runs on localhost:3000)
4. Production build: `npm run build`

## Customization
- Update contact links in Contact.js
- Modify testimonials in Testimonials.js  
- Change colors in tailwind.config.js
- Add your own images to public folder
- Update meta tags in public/index.html

## Important Notes
- Replace placeholder links (Instagram, WhatsApp) with your actual accounts
- Update email address in Contact.js
- Add your own favicon and logo images
- Consider adding Google Analytics or other tracking
