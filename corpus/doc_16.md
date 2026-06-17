# JavaScript Objects
doc_id: doc_16
topic: JavaScript
difficulty: beginner

## What is an Object?
An object stores related data as key-value pairs:
var student = {
  name: "Favour",
  age: 21,
  course: "Computer Engineering"
}

## Accessing Properties
Dot notation: student.name
Bracket notation: student["name"]

## Adding and Updating Properties
student.grade = "A"
student.age = 22

## Deleting Properties
delete student.grade

## Methods in Objects
var student = {
  name: "Favour",
  greet: function() {
    return "Hello, I am " + this.name
  }
}
student.greet()

## Looping Through Objects
for (var key in student) {
  console.log(key + ": " + student[key])
}

## Object.keys and Object.values
Object.keys(student) — returns array of keys
Object.values(student) — returns array of values