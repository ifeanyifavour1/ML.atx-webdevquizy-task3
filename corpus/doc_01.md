# HTML Fundamentals
doc_id: doc_01
topic: HTML
difficulty: beginner

## What is HTML?
HTML stands for HyperText Markup Language. It is the standard language for creating web pages. HTML describes the structure of a web page using elements represented by tags.

## Basic HTML Structure
Every HTML document follows this structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

## Common HTML Tags
- `<h1>` to `<h6>` — headings from largest to smallest
- `<p>` — paragraph
- `<a href="">` — hyperlink
- `<img src="">` — image
- `<div>` — block container
- `<span>` — inline container
- `<ul>`, `<ol>`, `<li>` — lists

## DOCTYPE Declaration
`<!DOCTYPE html>` tells the browser this is an HTML5 document. It must be the very first line of every HTML file.

## HTML Attributes
Attributes provide extra information about elements. They are written inside the opening tag as name="value" pairs. Example: `<a href="https://example.com">Click here</a>`