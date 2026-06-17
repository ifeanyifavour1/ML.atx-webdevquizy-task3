# JavaScript DOM Manipulation
doc_id: doc_10
topic: JavaScript
difficulty: beginner

## What is the DOM?
DOM stands for Document Object Model. It is a tree representation of the HTML page that JavaScript can read and change.

## Selecting Elements
```javascript
document.getElementById("myId")
document.querySelector(".myClass")
document.querySelectorAll("p")
```

## Changing Content
```javascript
element.innerHTML = "<b>New content</b>"
element.textContent = "Plain text only"
```

## Changing Styles
```javascript
element.style.color = "red"
element.style.display = "none"
```

## Adding and Removing Classes
```javascript
element.classList.add("active")
element.classList.remove("hidden")
element.classList.toggle("dark")
```

## Creating and Appending Elements
```javascript
var div = document.createElement("div")
div.textContent = "New div"
document.body.appendChild(div)
```