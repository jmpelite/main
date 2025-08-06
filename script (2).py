# Create configuration files for deployment

# Tailwind CSS configuration
tailwind_config = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      colors: {
        gray: {
          '900': '#111827',
          '800': '#1f2937',
          '700': '#374151',
        }
      },
      animation: {
        'fadeInUp': 'fadeInUp 0.6s ease-out',
      },
      keyframes: {
        fadeInUp: {
          '0%': {
            opacity: '0',
            transform: 'translateY(30px)',
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0)',
          },
        },
      },
    },
  },
  plugins: [],
}"""

# PostCSS configuration
postcss_config = """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}"""

# Netlify configuration
netlify_toml = """[build]
  command = "npm run build"
  publish = "build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  NODE_VERSION = "18"

[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[[headers]]
  for = "/*.woff2"
  [headers.values]
    Cache-Control = "public, max-age=31536000"
"""

# Vercel configuration
vercel_json = """{
  "name": "jmp-coaching",
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        }
      ]
    }
  ]
}"""

# Public folder index.html
index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#111827" />
    <meta name="description" content="JMP Coaching - Real fitness for real life. Get fitter, boost confidence, and feel better without quitting your lifestyle." />
    <meta name="keywords" content="fitness coach, personal trainer, Scotland, Glasgow, Edinburgh, nightlife fitness, harm reduction, mental health" />
    <meta name="author" content="JMP Coaching" />
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://jmpcoaching.com/" />
    <meta property="og:title" content="JMP Coaching - Real Fitness for Real Life" />
    <meta property="og:description" content="Get fitter, boost confidence, and feel better without quitting your lifestyle. Practical guidance by a coach who gets it." />
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:title" content="JMP Coaching - Real Fitness for Real Life" />
    <meta property="twitter:description" content="Get fitter, boost confidence, and feel better without quitting your lifestyle. Practical guidance by a coach who gets it." />
    
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    
    <title>JMP Coaching - Real Fitness for Real Life</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>"""

# Deployment instructions
deployment_instructions = """# JMP Coaching Website Deployment Guide

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
"""

# Save all configuration files
with open('tailwind.config.js', 'w') as f:
    f.write(tailwind_config)

with open('postcss.config.js', 'w') as f:
    f.write(postcss_config)

with open('netlify.toml', 'w') as f:
    f.write(netlify_toml)

with open('vercel.json', 'w') as f:
    f.write(vercel_json)

with open('index.html', 'w') as f:
    f.write(index_html)

with open('DEPLOYMENT_GUIDE.md', 'w') as f:
    f.write(deployment_instructions)

print("All configuration files created!")
print("Files: tailwind.config.js, postcss.config.js, netlify.toml, vercel.json, index.html, DEPLOYMENT_GUIDE.md")