# CSS Box Model
doc_id: doc_05
topic: CSS
difficulty: beginner

## What is the Box Model?
Every HTML element is a rectangular box. The CSS box model describes the space around that box with four layers:
1. Content — the actual text or image
2. Padding — space inside the border, around the content
3. Border — a line around the padding
4. Margin — space outside the border, between elements

## Box Model Diagram
[ Margin ]
  [ Border ]
    [ Padding ]
      [ Content ]

## Key Properties
- padding: 10px — adds space inside the element
- border: 1px solid black — adds a border line
- margin: 20px — adds space outside the element
- width and height — set the size of the content area

## Margin vs Padding
- Padding is INSIDE the border — affects background color area
- Margin is OUTSIDE the border — transparent, pushes other elements away

## box-sizing
box-sizing: border-box makes width include padding and border — much easier to work with.