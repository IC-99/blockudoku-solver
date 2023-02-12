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

        p23 = numpy.ones((3, 3), int)
        p23[0][0] = 0
        p23[0][1] = 0
        p23[1][0] = 0
        p23[1][1] = 0
        self.pieces.append(p23)

        p24 = numpy.ones((3, 3), int)
        p24[0][1] = 0
        p24[0][2] = 0
        p24[1][1] = 0
        p24[1][2] = 0
        self.pieces.append(p24)

        p25 = numpy.ones((3, 3), int)
        p25[1][0] = 0
        p25[1][1] = 0
        p25[2][0] = 0
        p25[2][1] = 0
        self.pieces.append(p25)

        p26 = numpy.ones((3, 3), int)
        p26[1][1] = 0
        p26[1][2] = 0
        p26[2][1] = 0
        p26[2][2] = 0
        self.pieces.append(p26)

        p27 = numpy.ones((1, 4), int)
        self.pieces.append(p27)

        p28 = numpy.ones((4, 1), int)
        self.pieces.append(p28)

        p29 = numpy.ones((1, 5), int)
        self.pieces.append(p29)

        p30 = numpy.ones((5, 1), int)
        self.pieces.append(p30)

        if type == 'plus':
            # add other pieces
            pass

        
    def get_set(self):
        return self.pieces

    def print(self):
        for p in self.pieces:
            print(p)

