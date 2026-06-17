# CSS Typography
doc_id: doc_27
topic: CSS
difficulty: beginner

## Font Properties
- font-family — the typeface
- font-size — size of text
- font-weight — boldness (100-900, or bold/normal)
- font-style — normal, italic, oblique
- line-height — space between lines
- letter-spacing — space between letters

## Font Families
font-family: "Arial", sans-serif;
Always provide a fallback font after the main one.

## Google Fonts
Link in HTML head:
<link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">

Use in CSS:
font-family: "Inter", sans-serif;

## Text Properties
- text-align: left, center, right, justify
- text-decoration: none, underline, line-through
- text-transform: uppercase, lowercase, capitalize
- text-shadow: 2px 2px 4px rgba(0,0,0,0.5)

## Responsive Typography
Use rem for font sizes so they scale with user preferences:
body { font-size: 16px; }
h1 { font-size: 2rem; }
p { font-size: 1rem; }