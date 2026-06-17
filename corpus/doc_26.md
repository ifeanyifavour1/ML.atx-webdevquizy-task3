# Web Accessibility Basics
doc_id: doc_26
topic: HTML
difficulty: intermediate

## What is Web Accessibility?
Web accessibility means building websites that everyone can use, including people with disabilities who use screen readers, keyboard navigation, or other assistive technologies.

## Alt Text for Images
Always add descriptive alt text:
<img src="logo.png" alt="ATX WebDevQuizy logo">
Empty alt for decorative images: <img src="divider.png" alt="">

## Semantic HTML Helps Accessibility
Screen readers understand semantic tags like header, nav, main, footer better than divs.

## ARIA Labels
Use aria-label when there is no visible text label:
<button aria-label="Close menu">X</button>

## Keyboard Navigation
All interactive elements must be reachable by Tab key. Links and buttons work by default. Custom elements need tabindex="0".

## Color Contrast
Text must have enough contrast against background. Minimum ratio is 4.5:1 for normal text. Dark background with white text usually passes.

## Focus Styles
Never remove focus outline completely:
button:focus { outline: 2px solid purple; }