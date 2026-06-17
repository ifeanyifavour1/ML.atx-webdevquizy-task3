# JavaScript Local Storage
doc_id: doc_20
topic: JavaScript
difficulty: intermediate

## What is Local Storage?
Local Storage lets you save data in the browser that persists even after the page is closed. Data is stored as key-value pairs as strings.

## Basic Operations
Save data:
localStorage.setItem("username", "Favour")

Get data:
var name = localStorage.getItem("username")

Remove one item:
localStorage.removeItem("username")

Clear everything:
localStorage.clear()

## Storing Objects
Local storage only stores strings so use JSON:
var user = { name: "Favour", score: 95 }
localStorage.setItem("user", JSON.stringify(user))

var saved = JSON.parse(localStorage.getItem("user"))

## Session Storage
sessionStorage works the same way but data is cleared when the browser tab is closed. Use it for temporary data.

## Use Cases
- Remember dark/light mode preference
- Save quiz progress
- Store user login state temporarily
- Cache API responses