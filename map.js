function getN() { return 2; }
function getSeq() { return "BCBBBAABBCBCCAAABBACAAACCABBABCCACBCBCAC"; }

function mapping(key) {
    map = {};
    map['B'] = "<img src=\"./resources/george.jpg\">";
    map['C'] = "<img src=\"./resources/al.jpg\">";
    map['A'] = "<img src=\"./resources/godzilla.jpg\" />";
    return map[key];
}