# JavaScript ES6 Features
doc_id: doc_22
topic: JavaScript
difficulty: intermediate

## What is ES6?
ES6 (ECMAScript 2015) introduced major improvements to JavaScript. Most modern browsers support all ES6 features.

## Arrow Functions
Old way: function add(a, b) { return a + b }
ES6 way: var add = (a, b) => a + b

## Template Literals
Old way: "Hello " + name + "!"
ES6 way: "Hello ${name}!"

## Destructuring
Arrays: var [first, second] = [1, 2]
Objects: var { name, age } = student

## Spread Operator
var arr1 = [1, 2, 3]
var arr2 = [...arr1, 4, 5]

## Default Parameters
function greet(name = "stranger") {
  return "Hello " + name
}

## Modules
Export: export function add(a, b) { return a + b }
Import: import { add } from "./math.js"

## let and const
let — block scoped, can be reassigned
const — block scoped, cannot be reassigned
Avoid var in modern JavaScript.