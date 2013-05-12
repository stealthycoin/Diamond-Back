from random import randint as ri
from random import random as r
import sys
import re

class Alphabet:
    def __init__(self):
        self.symbolSet = []
        self.total = 0.0
        
    def addSymbol(self, symbol, prob, HTML):
        self.symbolSet.append((symbol,float(prob),HTML))
        self.total += float(prob)
        
    def pack(self):
        if self.total > 1.1:
            return False
        self.symbolSet = sorted(self.symbolSet, key=lambda x:x[1], reverse=True)
        return True

    def makeUniformSequence(self, length):
        s = ""
        while length > 0:
            s += self.getUniform()
            length -= 1
        return s

    def makeSequence(self, length):
        s = ""
        while length > 0:
            s += self.getSymbol()
            length -= 1
        return s

    def getUniform(self):
        return self.symbolSet[ri(0, len(self.symbolSet)-1)][0]

    def getSymbol(self):
        def tryGet(k, i):
            if k <= self.symbolSet[i][1]:
                return self.symbolSet[i][0]
            return tryGet(k - self.symbolSet[i][1], i+1)
        return tryGet(r(),0)

class Settings:
    def __init__(self, filepath, debug=False):
        f = open(filepath, 'r')
        self.alph = Alphabet()
        self.n = 1
        for line in f:
            if debug:
                print("Processing '%s'" % line[:-1])
            #check if it is a symbol definition
            m = re.search('^[Ss]ymbol: ?([\w\+\?!@#\$%\^&\*\(\)]) (\.\d+)(?:$| (.*))', line)
            if m:
                if debug:
                    print("Adding %s to alphabet with probability of %s" % (m.group(1), m.group(2)))
                try:
                    HTML = re.sub("\"","\\\"",m.group(3))
                except IndexError:
                    HTML = None
                self.alph.addSymbol(m.group(1), m.group(2), HTML)
            #check if it is the number of lines
            m = re.search("[Nn]: ?(\d+)", line)
            if m:
                if debug:
                    print("N = " + m.group(1))
                self.n = int(m.group(1))
                
        if not self.alph.pack():
            print("Probabilities must sum to 1")
            sys.exit()


def buildJS(alph, seq, n):
    print(seq)
    numback = "function getN() { return %d; }" % n
    getseq = "function getSeq() { return \"%s\"; }" % seq

    mappings = """function mapping(key) {
%s
    return map[key];
}"""
    

    m = "    map = {};"
    for s in alph.symbolSet:
        try:
            transform = s[2]
        except IndexError:
            transform = s[0]
        m += "\n    map['" + s[0] + "'] = \""+transform+"\";"

    mappings = mappings % m
    f = open("map.js", 'w')
    f.write("%s\n%s\n\n%s" %(numback, getseq,  mappings))
    f.close()

def main():
    
    if len(sys.argv) < 3:
        print("Usage: python nback-gen.py file [seqs]")
        print("file is the alphabet file to load")
        print("each seq is either a number ie or u followed by a numbere (ie 10 u39)")
        print("10 will give a sequence of 10 symbols chosen using the distribution in the file.")
        print("u93 will give a sequence of 93 symbols uniformly distributed")
        print("\nExample python nback-gen.py alph.txt 10 u20")
        print("Gives 1 sequence of length 10 with the file distribution, and one uniform distribution with 20 symbols.")
    else:
        settings = Settings(sys.argv[1])
        out = ""
        for a in sys.argv[2:]:
            if a.startswith('u'):
                out += settings.alph.makeUniformSequence(int(a[1:]))
            else:
                out += settings.alph.makeSequence(int(a))
        buildJS(settings.alph, out, settings.n)

if __name__ == "__main__":
    main()
