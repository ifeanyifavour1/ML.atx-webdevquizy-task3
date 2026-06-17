# CSS Flexbox
doc_id: doc_06
topic: CSS
difficulty: intermediate

## What is Flexbox?
Flexbox is a CSS layout model that arranges items in a row or column. It makes alignment and spacing easy without using floats or positioning hacks.

## Enabling Flexbox
Apply `display: flex` to the parent container:
```css
.container {
  display: flex;
}
```

## Main Axis vs Cross Axis
- Main axis — the direction items flow (row = horizontal, column = vertical)
- Cross axis — the perpendicular direction

## Key Flex Container Properties
- `flex-direction: row | column` — direction of items
- `justify-content` — alignment on main axis
- `align-items` — alignment on cross axis
- `flex-wrap: wrap` — allows items to wrap to next line
- `gap: 10px` — space between items

## justify-content Values
- `flex-start` — items at the start
- `flex-end` — items at the end
- `center` — items centered
- `space-between` — equal space between items
- `space-around` — equal space around items