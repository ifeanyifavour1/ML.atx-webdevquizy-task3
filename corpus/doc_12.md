# JavaScript Fetch API
doc_id: doc_12
topic: JavaScript
difficulty: intermediate

## What is the Fetch API?
The Fetch API lets JavaScript make HTTP requests to servers without reloading the page. It replaces the older XMLHttpRequest method.

## Basic Fetch Request
fetch("https://api.example.com/data")
  .then(function(response) { return response.json() })
  .then(function(data) { console.log(data) })
  .catch(function(error) { console.log(error) })

## Fetch with async/await
async function getData() {
  var response = await fetch("https://api.example.com/data")
  var data = await response.json()
  console.log(data)
}

## POST Request with Fetch
fetch("https://api.example.com/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Favour", age: 21 })
})

## Response Methods
- response.json() — parse JSON response
- response.text() — get plain text
- response.status — HTTP status code (200, 404, 500)
- response.ok — true if status is 200-299