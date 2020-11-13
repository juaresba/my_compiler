from scope import Object

class Attribute:
    def __init__(self):
        self.type = 0
        self.size = 0
        self.attribute = None

class ID:
    def __init__(self):
        self.object = None
        self.name = 0

class T:
    def __init__(self):
        self.type = None

class E:
    def __init__(self):
        self.type = None

class L:
    def __init__(self):
        self.type = None

class R:
    def __init__(self):
        self.type = None

class Y:
    def __init__(self):
        self.type = None

class F:
    def __init__(self):
        self.type = None

class LV:
    def __init__(self):
        self.type = None
    
class MC:
    def __init__(self):
        self.type = None
        self.param = None
        self.err = 0
    
class MT:
    def __init__(self):
        self.label = 0

class ME:
    def __init__(self):
        self.label = 0

class MW:
    def __init__(self):
        self.label = 0

class MA:
    def __init__(self):
        self.label = 0

class LE:
    def __init__(self):
        self.type = None
        self.param = None
        self.err = 0
        self.n = 0

class LI:
    def __init__(self):
        self.list = None

class DC:
    def __init__(self):
        self.list = None

class LP:
    def __init__(self):
        self.list = None

class TRUE:
    def __init__(self):
        self.type = None
        self.val = 0

class FALSE:
    def __init__(self):
        self.type = None
        self.val = 0

class CHR:
    def __init__(self):
        self.type = None
        self.pos = 0
        self.val = ''

class STR:
    def __init__(self):
        self.type = None
        self.pos = 0
        self.val = ''

class NUM:
    def __init__(self):
        self.type = None
        self.pos = 0
        self.val = 0

IDDStatic = Attribute()
IDDStatic.attribute = ID()

IDUStatic = Attribute()
IDUStatic.attribute = ID()

IDStatic = Attribute()
IDStatic.attribute = ID()

TStatic = Attribute()
TStatic.attribute = T()

LIStatic = Attribute()
LIStatic.attribute = LI()

LI0Static = Attribute()
LI0Static.attribute = LI()

LI1Static = Attribute()
LI1Static.attribute = LI()

TRUStatic = Attribute()
TRUStatic.attribute = TRUE()

FALSStatic = Attribute()
FALSStatic.attribute = FALSE()

STRStatic = Attribute()
STRStatic.attribute = STR()

CHRStatic = Attribute()
CHRStatic.attribute = CHR()

NUMStatic = Attribute()
NUMStatic.attribute = NUM()

DCStatic = Attribute()
DCStatic.attribute = DC()

DC0Static = Attribute()
DC0Static.attribute = DC()

DC1Static = Attribute()
DC1Static.attribute = DC()

LPStatic = Attribute()
LPStatic.attribute = LP()

LP0Static = Attribute()
LP0Static.attribute = LP()

LP1Static = Attribute()
LP1Static.attribute = LP()

EStatic = Attribute()
EStatic.attribute = E()

E0Static = Attribute()
E0Static.attribute = E0Static

E1Static = Attribute()
E1Static.attribute = E()

LStatic = Attribute()
LStatic.attribute = L()

L0Static = Attribute()
L0Static.attribute = L()

L1Static = Attribute()
L1Static.attribute = L()

RStatic = Attribute()
RStatic.attribute = R()

R0Static = Attribute()
R0Static.attribute = R()

R1Static = Attribute()
R1Static.attribute = R()

YStatic = Attribute()
YStatic.attribute = Y()

Y0Static = Attribute()
Y0Static.attribute = Y()

Y1Static = Attribute()
Y1Static.attribute = Y()

FStatic = Attribute()
FStatic.attribute = F()

F0Static = Attribute()
F0Static.attribute = F()

F1Static = Attribute()
F1Static.attribute = F()

LVStatic = Attribute()
LVStatic.attribute = LV()

LV0Static = Attribute()
LV0Static.attribute = LV()

LV1Static = Attribute()
LV1Static.attribute = LV()

MCStatic = Attribute()
MCStatic.attribute = MC()

LEStatic = Attribute()
LEStatic.attribute = LE()

LE0Static = Attribute()
LE0Static.attribute = LE()

LE1Static = Attribute()
LE1Static.attribute = LE()

MTStatic = Attribute()
MTStatic.attribute = MT()

MEStatic = Attribute()
MEStatic.attribute = ME()

MWStatic = Attribute()
MWStatic.attribute = MW()

NBStatic = Attribute()

p = Object()
t = Object()
f = Object()
 
name = 0
n = 0
l = 0
l1 = 0
l2 = 0


functionVarPos = 0
curFunction = Object()