# CSS Responsive Design
doc_id: doc_13
topic: CSS
difficulty: intermediate

## What is Responsive Design?
Responsive design makes web pages look good on all screen sizes — desktop, tablet, and mobile. The layout adjusts automatically based on the screen width.

## Viewport Meta Tag
Always add this to the HTML head:
<meta name="viewport" content="width=device-width, initial-scale=1.0">

## Media Queries
Media queries apply CSS only when certain conditions are met:
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}

## Common Breakpoints
- Mobile: max-width 480px
- Tablet: max-width 768px
- Desktop: min-width 1024px

## Mobile First Approach
Write CSS for mobile first, then add media queries for larger screens. This is better for performance.

## Responsive Units
- % — percentage of parent element
- vw — percentage of viewport width
- vh — percentage of viewport height
- rem — relative to root font size
- em — relative to parent font size