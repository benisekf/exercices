document.addEventListener("DOMContentLoaded", function () {
    setInterval(() => {
      mixAbc();
    }, 2000);
  });
  function mixAbc() {
    let rand = Math.floor(Math.random() * 3) + 1;
    console.log(rand);
  
    const letters = ['A', 'B', 'C'];
    for (let i = 0; i < letters.length; i++) {
      document.getElementById(rand).innerText = letters[i];
      rand = getNextElem(rand);
    }
  }
  function getNextElem(number) {
    if (number >= 3) {
      number = number - 3;
    }
    return number + 1;
  }
  