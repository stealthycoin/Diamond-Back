function getN() { return 2; }
function getSeq() { return "DDDBDDAABDDDAADAADDD"; }

function mapping(key) {
    map = {};
    map['D'] = "<object height=\"100\" width=\"100\" data=\"./resources/horse.wav\"></object>";
    map['A'] = "<img src=\"./resources/godzilla.jpg\" />";
    map['B'] = "<img src=\"./resources/george.jpg\">";
    map['C'] = "<img src=\"./resources/al.jpg\">";
    return map[key];
}