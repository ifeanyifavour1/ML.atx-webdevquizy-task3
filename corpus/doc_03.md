# HTML Forms
doc_id: doc_03
topic: HTML
difficulty: beginner

## What is an HTML Form?
A form collects user input and sends it to a server. Forms use the `<form>` element as a container.

## Basic Form Structure
```html
<form action="/submit" method="POST">
  <input type="text" name="username" placeholder="Enter name">
  <input type="password" name="password">
  <button type="submit">Submit</button>
</form>
```

## Common Input Types
- `type="text"` — single line text
- `type="password"` — hidden text
- `type="email"` — email validation built in
- `type="checkbox"` — tick box
- `type="radio"` — select one option
- `type="submit"` — submit button

## Form Attributes
- `action` — where to send the form data
- `method` — GET (visible in URL) or POST (hidden in body)
- `placeholder` — hint text inside input
- `required` — makes a field mandatory