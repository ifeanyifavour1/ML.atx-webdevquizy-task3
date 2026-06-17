# CSS Pseudo-classes and Pseudo-elements
doc_id: doc_24
topic: CSS
difficulty: intermediate

## What are Pseudo-classes?
Pseudo-classes style elements based on their state or position.

## Common Pseudo-classes
- :hover — when mouse is over element
- :focus — when element is focused (clicked or tabbed)
- :active — when element is being clicked
- :visited — for links already visited
- :first-child — first child of its parent
- :last-child — last child of its parent
- :nth-child(n) — every nth child

## Examples
a:hover { color: purple; }
input:focus { border-color: purple; outline: none; }
li:first-child { font-weight: bold; }
tr:nth-child(even) { background-color: #111; }

## What are Pseudo-elements?
Pseudo-elements style a specific part of an element.

## Common Pseudo-elements
- ::before — inserts content before element
- ::after — inserts content after element
- ::first-letter — styles first letter
- ::placeholder — styles input placeholder text

## Examples
.button::after {
  content: " →";
}
input::placeholder { color: gray; }