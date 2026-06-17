# HTML Media Elements
doc_id: doc_23
topic: HTML
difficulty: beginner

## HTML Video
<video width="640" height="360" controls>
  <source src="video.mp4" type="video/mp4">
  Your browser does not support video.
</video>

## Video Attributes
- controls — show play/pause/volume buttons
- autoplay — start playing automatically
- loop — repeat the video
- muted — start with no sound
- poster — image shown before video plays

## HTML Audio
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>

## HTML iframe
Embeds another webpage inside your page:
<iframe src="https://www.youtube.com/embed/VIDEO_ID" width="560" height="315"></iframe>

## HTML Canvas
The canvas element is used for drawing graphics with JavaScript:
<canvas id="myCanvas" width="400" height="200"></canvas>

var ctx = document.getElementById("myCanvas").getContext("2d")
ctx.fillStyle = "purple"
ctx.fillRect(10, 10, 100, 50)