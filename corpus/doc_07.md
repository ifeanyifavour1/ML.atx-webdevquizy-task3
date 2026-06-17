# CSS Grid
doc_id: doc_07
topic: CSS
difficulty: intermediate

## What is CSS Grid?
CSS Grid is a two-dimensional layout system. Unlike Flexbox which works in one direction, Grid works in both rows and columns at the same time.

## Enabling Grid
```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto;
  gap: 10px;
}
```

## Key Grid Properties
- `grid-template-columns` — defines column sizes
- `grid-template-rows` — defines row sizes
- `gap` — space between grid cells
- `grid-column` — how many columns an item spans
- `grid-row` — how many rows an item spans

## fr Unit
`fr` means fraction of available space. `1fr 1fr 1fr` creates 3 equal columns.

## Grid vs Flexbox
- Use Flexbox for one-dimensional layouts (row OR column)
- Use Grid for two-dimensional layouts (rows AND columns)
- They can be combined — a grid item can also be a flex container