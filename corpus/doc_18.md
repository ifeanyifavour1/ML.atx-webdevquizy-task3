# CSS Transitions and Animations
doc_id: doc_18
topic: CSS
difficulty: intermediate

## CSS Transitions
Transitions smoothly animate a property change:
.button {
  background-color: purple;
  transition: background-color 0.3s ease;
}
.button:hover {
  background-color: black;
}

## Transition Properties
- transition-property — which property to animate
- transition-duration — how long (e.g. 0.3s)
- transition-timing-function — ease, linear, ease-in, ease-out
- transition-delay — wait before starting

## CSS Animations
Animations use keyframes for more complex motion:
@keyframes slideIn {
  from { transform: translateX(-100px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.box {
  animation: slideIn 0.5s ease forwards;
}

## Animation Properties
- animation-name — name of the keyframe
- animation-duration — how long
- animation-iteration-count — how many times (infinite for looping)
- animation-direction — normal, reverse, alternate