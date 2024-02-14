function moveLetters() {
  var table = document.getElementById("letterTable");
  var cells = table.getElementsByTagName("td");
  for (let i = 0; i < cells.length; i++) {
      cells[i].innerHTML = '';
  }
  var randomPosition = Math.floor(Math.random() * cells.length);
  cells[randomPosition].innerHTML = 'A';
}
setInterval(moveLetters, 1000);