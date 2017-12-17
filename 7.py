import numpy as np

def solve1(fname):
    co = []
    with open(fname) as f:
        co = f.readlines()
        co = [e.strip() for e in co]
    rels = []
    rd = {} # rels dict
    for c in co:
        c = c[:c.find('(')] + c[c.rfind(')')+2:]
        inter = [e.strip() for e in c.split('->')]
        if len(inter) > 1:
            inter[1] = [e.strip() for e in inter[1].split(',')]
            for e in inter[1]:
                if e in rd:
                    rd[e].append(inter[0])
                else:
                    rd[e] = [inter[0]]
        rels.append(inter)

    curnode = rels[0][0] # doesn't matter where you start
    while True:
        if curnode in rd:
            curnode = rd[curnode][0]
        else:
            return curnode

def solve2(fname):
    pass


if __name__ == '__main__':
    fname = '7.txt'
    print(solve1(fname))
    print(solve2(fname))
