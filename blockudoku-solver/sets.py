from copy import deepcopy
import numpy

class PieceSets:

    def __init__(self, type = 'normal') -> None:
        self.pieces = []
        
        p1 = numpy.ones((1, 1), int)
        self.pieces.append(p1)

        p2 = numpy.ones((1, 2), int)
        self.pieces.append(p2)

        p3 = numpy.ones((2, 1), int)
        self.pieces.append(p3)

        p4 = numpy.ones((2, 2), int)
        p4[0][0] = 0
        self.pieces.append(p4)

        p5 = numpy.ones((2, 2), int)
        p5[0][1] = 0
        self.pieces.append(p5)

        p6 = numpy.ones((2, 2), int)
        p6[1][0] = 0
        self.pieces.append(p6)

        p7 = numpy.ones((2, 2), int)
        p7[1][1] = 0
        self.pieces.append(p7)

        p8 = numpy.ones((2, 2), int)
        self.pieces.append(p8)
        
        p9 = numpy.ones((1, 3), int)
        self.pieces.append(p9)

        p10 = numpy.ones((3, 1), int)
        self.pieces.append(p10)

        p11 = numpy.ones((3, 2), int)
        p11[0][0] = 0
        p11[1][0] = 0
        self.pieces.append(p11)

        p12 = numpy.ones((3, 2), int)
        p12[0][1] = 0
        p12[1][1] = 0
        self.pieces.append(p12)

        p13 = numpy.ones((3, 2), int)
        p13[1][0] = 0
        p13[2][0] = 0
        self.pieces.append(p13)

        p14 = numpy.ones((3, 2), int)
        p14[1][1] = 0
        p14[2][1] = 0
        self.pieces.append(p14)
        
        p15 = numpy.ones((2, 3), int)
        p15[0][0] = 0
        p15[0][1] = 0
        self.pieces.append(p15)

        p16 = numpy.ones((2, 3), int)
        p16[0][1] = 0
        p16[0][2] = 0
        self.pieces.append(p16)

        p17 = numpy.ones((2, 3), int)
        p17[1][0] = 0
        p17[1][1] = 0
        self.pieces.append(p17)

        p18 = numpy.ones((2, 3), int)
        p18[1][1] = 0
        p18[1][2] = 0
        self.pieces.append(p18)

        p19 = numpy.ones((3, 2), int)
        p19[0][0] = 0
        p19[2][0] = 0
        self.pieces.append(p19)

        p20 = numpy.ones((3, 2), int)
        p20[0][1] = 0
        p20[2][1] = 0
        self.pieces.append(p20)

        p21 = numpy.ones((2, 3), int)
        p21[0][0] = 0
        p21[0][2] = 0
        self.pieces.append(p21)

        p22 = numpy.ones((2, 3), int)
        p22[1][0] = 0
        p22[1][2] = 0
        self.pieces.append(p22)

        p23 = numpy.ones((3, 2), int)
        p23[0][0] = 0
        p23[2][1] = 0
        self.pieces.append(p23)

        p24 = numpy.ones((3, 2), int)
        p24[0][1] = 0
        p24[2][0] = 0
        self.pieces.append(p24)

        p25 = numpy.ones((2, 3), int)
        p25[0][0] = 0
        p25[1][2] = 0
        self.pieces.append(p25)

        p26 = numpy.ones((2, 3), int)
        p26[0][2] = 0
        p26[1][0] = 0
        self.pieces.append(p26)

        p27 = numpy.ones((3, 3), int)
        p27[0][0] = 0
        p27[0][1] = 0
        p27[1][0] = 0
        p27[1][1] = 0
        self.pieces.append(p27)

        p28 = numpy.ones((3, 3), int)
        p28[0][1] = 0
        p28[0][2] = 0
        p28[1][1] = 0
        p28[1][2] = 0
        self.pieces.append(p28)

        p29 = numpy.ones((3, 3), int)
        p29[1][0] = 0
        p29[1][1] = 0
        p29[2][0] = 0
        p29[2][1] = 0
        self.pieces.append(p29)

        p30 = numpy.ones((3, 3), int)
        p30[1][1] = 0
        p30[1][2] = 0
        p30[2][1] = 0
        p30[2][2] = 0
        self.pieces.append(p30)

        p31 = numpy.ones((3, 3), int)
        p31[0][0] = 0
        p31[0][1] = 0
        p31[2][0] = 0
        p31[2][1] = 0
        self.pieces.append(p31)

        p32 = numpy.ones((3, 3), int)
        p32[0][1] = 0
        p32[0][2] = 0
        p32[2][1] = 0
        p32[2][2] = 0
        self.pieces.append(p32)

        p33 = numpy.ones((3, 3), int)
        p33[0][0] = 0
        p33[0][2] = 0
        p33[1][0] = 0
        p33[1][2] = 0
        self.pieces.append(p33)

        p34 = numpy.ones((3, 3), int)
        p34[1][0] = 0
        p34[1][2] = 0
        p34[2][0] = 0
        p34[2][2] = 0
        self.pieces.append(p34)

        p35 = numpy.ones((1, 4), int)
        self.pieces.append(p35)

        p36 = numpy.ones((4, 1), int)
        self.pieces.append(p36)

        p37 = numpy.ones((1, 5), int)
        self.pieces.append(p37)

        p38 = numpy.ones((5, 1), int)
        self.pieces.append(p38)

        if type == 'plus':
            # add other pieces
            pass

        
    def get_set(self):
        return self.pieces

    def print(self):
        for p in self.pieces:
            print(p)

