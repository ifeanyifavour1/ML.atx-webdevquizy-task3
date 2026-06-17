# CSS Colors and Backgrounds
doc_id: doc_14
topic: CSS
difficulty: beginner

## CSS Color Formats
- Named: color: red
- Hex: color: #ff0000
- RGB: color: rgb(255, 0, 0)
- RGBA: color: rgba(255, 0, 0, 0.5) — last value is opacity
- HSL: color: hsl(0, 100%, 50%)

## Text Color vs Background Color
- color — changes text color
- background-color — changes background color

## CSS Gradients
Linear gradient:
background: linear-gradient(to right, #6a0dad, #000000);

Radial gradient:
background: radial-gradient(circle, purple, black);

## Background Properties
- background-image: url("image.jpg")
- background-size: cover — fills the whole area
- background-position: center
- background-repeat: no-repeat
- background-attachment: fixed — parallax effect

## Opacity
opacity: 0.5 makes the whole element 50% transparent.
Use rgba for just the color transparency without affecting child elements.