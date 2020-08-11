
document.getElementById("openone").onclick = one

document.getElementById("opentwo").onclick = two

document.getElementById("openthree").onclick = three

document.getElementById("close").onclick = myMove

function one() {

    var one = document.getElementById("cone");
    var two = document.getElementById("ctwo");
    var three = document.getElementById("cthree");
    one.style.display = "block";
    two.style.display = "none";
    three.style.display = "none";

    var open = document.getElementById("open");
    var pos = -30;
    var id = setInterval(frame, 30);
    function frame() {
      if (pos == 0) {
        clearInterval(id);
      } else {
        pos++;
        open.style.right = pos + "em";
      }
    }
}

function two() {
    var open = document.getElementById("open");
    var closed = document.getElementById("closed");

    closed.style.display = "none";
    open.style.display = "block";

    var one = document.getElementById("cone");
    var two = document.getElementById("ctwo");
    var three = document.getElementById("cthree");
    one.style.display = "none";
    two.style.display = "block";
    three.style.display = "none";
}

function three() {
    var open = document.getElementById("open");
    var closed = document.getElementById("closed");

    closed.style.display = "none";
    open.style.display = "block";

    var one = document.getElementById("cone");
    var two = document.getElementById("ctwo");
    var three = document.getElementById("cthree");
    one.style.display = "none";
    two.style.display = "none";
    three.style.display = "block";
}

function close() {
    var open = document.getElementById("open");
    var closed = document.getElementById("closed");

    open.style.display = "none";
    closed.style.display = "block";
}

function myMove() {
  var elem = document.getElementById("open");
  var pos = 0;
  var id = setInterval(frame, 5);
  function frame() {
    if (pos == 150) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.right = pos + "px";
    }
  }
}
