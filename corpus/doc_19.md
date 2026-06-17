# HTML Tables
doc_id: doc_19
topic: HTML
difficulty: beginner

## What is an HTML Table?
Tables display data in rows and columns. Use tables for tabular data only — not for page layout.

## Basic Table Structure
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Favour</td>
      <td>95</td>
    </tr>
  </tbody>
</table>

## Table Tags
- table — the container
- thead — table header section
- tbody — table body section
- tr — table row
- th — header cell (bold by default)
- td — data cell

## Table Attributes
- colspan — cell spans multiple columns
- rowspan — cell spans multiple rows
- border — adds border (use CSS instead)

## Styling Tables with CSS
table { width: 100%; border-collapse: collapse; }
td, th { border: 1px solid black; padding: 8px; }
tr:nth-child(even) { background-color: #f2f2f2; }