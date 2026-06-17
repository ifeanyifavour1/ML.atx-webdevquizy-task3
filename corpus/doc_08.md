# CSS Positioning
doc_id: doc_08
topic: CSS
difficulty: intermediate

## CSS Position Property
The position property controls how an element is placed in the document.

## Position Values
- `static` — default, normal document flow
- `relative` — positioned relative to its normal position
- `absolute` — positioned relative to nearest positioned ancestor
- `fixed` — positioned relative to the viewport, stays on scroll
- `sticky` — switches between relative and fixed based on scroll position

## Top, Right, Bottom, Left
Used with non-static positioning:
```css
.box {
  position: absolute;
  top: 20px;
  left: 50px;
}
```

## z-index
Controls stacking order of overlapping elements. Higher z-index = on top.
```css
.overlay {
  position: absolute;
  z-index: 10;
}
```

## Common Use Cases
- Fixed navbar — `position: fixed`
- Tooltip over an element — `position: absolute`
- Sticky sidebar — `position: sticky`