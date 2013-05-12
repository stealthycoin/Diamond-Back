var sequence = "";
var index = 0;
var content;
var n = 2; //the n in n-back
var right = 0;
var wrong = 0;
var total = 0;
var clicked = false;

//change frames or display end score
function tick() {
    index++;
    next = sequence[index];
    if (next === undefined) {
	content.innerHTML = "Right: " + right + "<br />Wrong: " + wrong + "<br />Total: " + total;
    }
    else{
	content.innerHTML = mapping(next);
	if (index - n >= 0 && sequence[index] === sequence[index-n]) {
	    total++;
	}
	clicked = false;
	setTimeout(function(){transition();}, 1500);

    }
}

//tranition between frames
function transition() {
    content.style.visibility = "hidden";
    setTimeout(function(){content.style.visibility="visible";tick();}, 200);
}

//runs after page has been loaded
function load() {
    content = document.getElementById("content");
    sequence = getSeq();
    n = getN();
    document.getElementById("n").innerHTML = "N = " + n;

    tick();
}

//when the button is pressed
function trigger() {
    if (clicked) return false;
    clicked = true;
    if (index - n < 0) {
	wrong++;
    }
    else {
	console.log(index + " " + sequence)
	console.log(sequence[index] + " " +sequence[index-n])
	if (sequence[index] === sequence[index-n]) {
	    right++;
	}
	else {
	    wrong++;
	}
    }
    return false;
}
