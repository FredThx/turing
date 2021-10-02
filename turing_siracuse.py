from turing import *


R = 1 # Droite
L = -1 # Gauche
b = " " # blanc

codeSyracuse = [
    TEtat(1, [
        TAction(0, b, L),
        TAction(1, None, L, 2),
    ]),
    TEtat(2, [
        TAction(b,None,None,None),
        TAction(0,None,R,4),
        TAction(1,None,R,4),
    ]),
    TEtat(3, [
        TAction(0,None,L),
        TAction(1,None,L,4),
        TAction(b,None,R,6)
    ]),
    TEtat(4, [
        TAction(1,0,L,5),
        TAction(b,1,R,6),
        TAction(0,1,L,3)
    ]),
    TEtat(5,[
        TAction(1,None,L),
        TAction(b,0,L,4),
        TAction(0,None,L,4)
    ]),
    TEtat(6,[
        TAction(0,None,R),
        TAction(1,None,R),
        TAction(b,None,L,1),
    ])
]
m=Turing(codeSyracuse, f"{2673:b}", start_right = True)

if __name__ == "__main__":
    m.run()
