function getDelay() { return 2000; }
function getN() { return 2; }
function getSeq() { return "CDADBDCCCB"; }

function mapping(key) {
    map = {};
    map['A'] = "<img src=\"./resources/godzilla.jpg\" />";
    map['B'] = "<img src=\"./resources/george.jpg\">";
    map['C'] = "<img src=\"./resources/al.jpg\">";
    map['D'] = "<object height=\"0\" width=\"0\" data=\"./resources/horse.wav\"></object>";
    return map[key];
}