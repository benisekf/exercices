function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
function moveLetter() {
  for (let i = 0; i < 10; i++) {
      document.getElementById("cell" + i).innerHTML = '';
  }
  var randomPosition = getRandomInt(10);
  document.getElementById("cell" + randomPosition).innerHTML = 'A';
}
setInterval(moveLetter, 1000);
