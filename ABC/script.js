function moveLetters() {
  var table = document.getElementById("letterTable");
  var rows = table.getElementsByTagName("tr");
  var letterA = rows[0].getElementsByTagName("td")[0].innerHTML;
  var letterB = rows[1].getElementsByTagName("td")[0].innerHTML;
  var letterC = rows[2].getElementsByTagName("td")[0].innerHTML;
  rows[0].getElementsByTagName("td")[0].innerHTML = letterB;
  rows[1].getElementsByTagName("td")[0].innerHTML = letterC;
  rows[2].getElementsByTagName("td")[0].innerHTML = letterA;
}
setInterval(moveLetters, 2000);