# CSS Dark Mode
doc_id: doc_30
topic: CSS
difficulty: intermediate

## What is Dark Mode?
Dark mode displays light text on a dark background. It reduces eye strain and looks modern. ATX WebDevQuizy uses a dark theme with purple accents.

## System Dark Mode Detection
@media (prefers-color-scheme: dark) {
  body {
    background-color: #000000;
    color: #ffffff;
  }
}

## Manual Dark Mode with CSS Variables
:root {
  --bg: #ffffff;
  --text: #000000;
}

:root.dark {
  --bg: #000000;
  --text: #ffffff;
}

body {
  background-color: var(--bg);
  color: var(--text);
}

## Toggle with JavaScript
var root = document.documentElement
root.classList.toggle("dark")

## Dark Mode Best Practices
- Use CSS variables for all colors — makes switching easy
- Do not use pure black (#000000) for backgrounds — use #111111 or #1a1a1a
- Do not use pure white for text — use #f0f0f0 or #e0e0e0
- Keep contrast ratio above 4.5:1 for readability
- Save user preference to localStorage so it persists