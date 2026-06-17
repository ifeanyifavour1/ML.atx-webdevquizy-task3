# CSS Fundamentals
doc_id: doc_04
topic: CSS
difficulty: beginner

## What is CSS?
CSS stands for Cascading Style Sheets. It controls how HTML elements look on screen — colors, fonts, spacing, layout, and more.

## How to Add CSS
Three ways to add CSS:
1. Inline: `<p style="color:red;">Text</p>`
2. Internal: inside a `<style>` tag in the `<head>`
3. External: a separate `.css` file linked with `<link rel="stylesheet" href="style.css">`

## CSS Syntax
```css
selector {
  property: value;
}
```
Example: `p { color: blue; font-size: 16px; }`

## CSS Selectors
- Element selector: `p { }` — targets all paragraphs
- Class selector: `.box { }` — targets elements with class="box"
- ID selector: `#header { }` — targets element with id="header"
- Universal selector: `* { }` — targets everything