# JavaScript Events
doc_id: doc_11
topic: JavaScript
difficulty: beginner

## What are Events?
Events are actions that happen in the browser — a user clicks a button, moves the mouse, presses a key, or a page finishes loading. JavaScript can listen for these events and respond to them.

## Adding Event Listeners
document.getElementById("btn").addEventListener("click", function() {
  console.log("Button clicked!")
})

## Common Event Types
- click — user clicks an element
- mouseover — user hovers over an element
- mouseout — user moves mouse away
- keydown — user presses a key
- keyup — user releases a key
- submit — user submits a form
- load — page finishes loading
- change — input value changes

## Event Object
The event listener receives an event object with useful info:
function handleClick(event) {
  console.log(event.target)
  event.preventDefault()
}

## removeEventListener
To stop listening for an event:
element.removeEventListener("click", handleClick)