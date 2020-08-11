let aside_open = false;

document.getElementById("one").onclick = one
document.getElementById("two").onclick = two
document.getElementById("three").onclick = three
document.getElementById("close").onclick = close

function one() {
    var one = document.getElementById("cone");
    var two = document.getElementById("ctwo");
    var three = document.getElementById("cthree");
    one.style.display = "block";
    two.style.display = "none";
    three.style.display = "none";

    if (!aside_open) {
        slide();
    }
}

function two() {
    var one = document.getElementById("cone");
    var two = document.getElementById("ctwo");
    var three = document.getElementById("cthree");
    one.style.display = "none";
    two.style.display = "block";
    three.style.display = "none";

    if (!aside_open) {
        slide();
    }
}

function three() {
    var one = document.getElementById("cone");
    var two = document.getElementById("ctwo");
    var three = document.getElementById("cthree");
    one.style.display = "none";
    two.style.display = "none";
    three.style.display = "block";
    if (!aside_open) {
        slide();
    }
}

function close() {
    if (aside_open) {
        var open = document.getElementById("open");
        var pos = 0;
        var id = setInterval(frameClose, 10);

        function frameClose() {
            if (pos == -37.5) {
                clearInterval(id);
            } else {
                pos = pos - 0.5;
                open.style.right = pos + "em";
            }
        }
        aside_open = false;
        var close = document.getElementById("close");
        close.style.display = "none";
    }
}

function slide() {
    var open = document.getElementById("open");
    var pos = -37.5;
    var id = setInterval(frame, 8);

    function frame() {
        if (pos == 0) {
            clearInterval(id);
        } else {
            pos = pos + 0.5;
            open.style.right = pos + "em";
        }
    }
    aside_open = true;
    var close = document.getElementById("close");
    close.style.display = "block";
}
