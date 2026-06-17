# JavaScript Arrays
doc_id: doc_15
topic: JavaScript
difficulty: beginner

## What is an Array?
An array stores multiple values in a single variable:
var fruits = ["apple", "banana", "mango"]

## Accessing Elements
Arrays are zero-indexed:
fruits[0] — "apple"
fruits[1] — "banana"
fruits[2] — "mango"

## Array Methods
- fruits.push("orange") — add to end
- fruits.pop() — remove from end
- fruits.shift() — remove from start
- fruits.unshift("grape") — add to start
- fruits.length — number of items
- fruits.indexOf("banana") — find index

## Looping Through Arrays
for (var i = 0; i < fruits.length; i++) {
  console.log(fruits[i])
}

## forEach
fruits.forEach(function(fruit) {
  console.log(fruit)
})

## filter and map
var longFruits = fruits.filter(function(f) { return f.length > 5 })
var upper = fruits.map(function(f) { return f.toUpperCase() })