# JavaScript Fundamentals
doc_id: doc_09
topic: JavaScript
difficulty: beginner

## What is JavaScript?
JavaScript is a programming language that runs in the browser. It makes web pages interactive — responding to clicks, updating content, validating forms, and more.

## Variables
Three ways to declare variables:
- `var` — old way, function-scoped, avoid in modern code
- `let` — block-scoped, can be reassigned
- `const` — block-scoped, cannot be reassigned

## Data Types
- String: `"hello"`
- Number: `42`, `3.14`
- Boolean: `true`, `false`
- Array: `[1, 2, 3]`
- Object: `{ name: "Favour", age: 21 }`
- null and undefined

## Functions
```javascript
function greet(name) {
  return "Hello " + name;
}

const greet = (name) => "Hello " + name;
```

## Conditionals
```javascript
if (score > 50) {
  console.log("Pass");
} else {
  console.log("Fail");
}
```