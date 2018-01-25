function playIt(x) {
  var audio = document.getElementById(x);
  audio.volume = 0.3;
  audio.play();
}

function StopIt(x) {
  var audio = document.getElementById(x);
  audio.pause();
  audio.currentTime = 0;
}
