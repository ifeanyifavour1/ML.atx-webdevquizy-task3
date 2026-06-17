# CSS Variables
doc_id: doc_21
topic: CSS
difficulty: intermediate

## What are CSS Variables?
CSS variables (custom properties) let you store values and reuse them throughout your stylesheet. They make it easy to update colors, fonts, and sizes in one place.

## Defining Variables
Variables are defined inside :root to make them global:
:root {
  --primary-color: #6a0dad;
  --background: #000000;
  --font-size: 16px;
}

## Using Variables
.button {
  background-color: var(--primary-color);
  font-size: var(--font-size);
}

## Fallback Values
var(--primary-color, purple) — uses purple if variable is not defined

## Updating Variables with JavaScript
document.documentElement.style.setProperty("--primary-color", "#ff0000")

## Use Cases
- Theme colors (dark mode / light mode)
- Consistent spacing and font sizes
- Brand colors used across many elements
CSS variables make your ATX WebDevQuizy dark purple theme easy to manage.