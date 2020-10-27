import csv
from token_classifier import TToken

P = 50
LDE = 51
DE = 52
DF = 53
DT = 54
T = 55
DC = 56
LI = 57
LP = 58
B = 59
LDV = 60
LS = 61
DV = 62
S = 63
E = 64
LV = 65
L = 66
R = 67
Y = 68
F = 69
LE = 70
ID = 71
TRUE = 72
FALSE = 73
CHR = 74
STR = 75
NUM = 76
PLINHA = 77
M = 78
U = 79
IDD = 80
IDU = 81
NB = 82
MF = 83
MC = 84
NF = 85
MT = 86
ME = 87
MW = 88

TOKEN_TAB_ACTION=[TToken.INTEGER,TToken.CHAR,TToken.BOOLEAN,TToken.STRING,TToken.TYPE,TToken.EQUALS,TToken.ARRAY,TToken.LEFT_SQUARE,TToken.RIGHT_SQUARE,TToken.OF,TToken.STRUCT,TToken.LEFT_BRACES,TToken.RIGHT_BRACES,TToken.SEMI_COLON,TToken.COLON,TToken.FUNCTION,TToken.LEFT_PARENTHESIS,TToken.RIGHT_PARENTHESIS,TToken.COMMA,TToken.VAR,TToken.IF,TToken.ELSE,TToken.WHILE,TToken.DO,TToken.BREAK,TToken.CONTINUE,TToken.AND,TToken.OR,TToken.LESS_THAN,TToken.GREATER_THAN,TToken.LESS_OR_EQUAL,TToken.GREATER_OR_EQUAL,TToken.EQUAL_EQUAL,TToken.NOT_EQUAL,TToken.PLUS,TToken.MINUS,TToken.TIMES,TToken.DIVIDE,TToken.PLUS_PLUS,TToken.MINUS_MINUS,TToken.NOT,TToken.DOT,TToken.ID,TToken.TRUE,TToken.FALSE,TToken.CHARACTER,TToken.STRINGVAL,TToken.NUMERAL,TToken.EOF,PLINHA,P,LDE,DE,T,DT,DC,DF,LP,B,LDV,LS,DV,LI,S,U,M,E,L,R,Y,F,LE,LV,IDD,IDU,ID,TRUE,FALSE,CHR,STR,NUM,NB,MF,MC,NF,MT,ME,MW]
def tokentab(a):
    return TOKEN_TAB_ACTION.index(a)+1

class Parser:
    def __init__(self, lexical_analyser):
        self.action_table = list(csv.reader(open("./syntactic_analyser/action_table.csv","r"),delimiter="\t"))
        print(self.action_table[0])
        self.state_stack = []
        self.lexical_analyser = lexical_analyser

        self.RIGHT = [1,		2,		1,		1,		1,		1,		1,		1,		1,		1,		9,		8,		4,		5,		3,		10,		5,		3,		4,		2,		1,		2,		1,		5,		3,		1,		1,		1,		6,		9,		9,		7,		8,		2,		4,		2,		2,		3,		3,		1,		3,		3,		3,		3,		3,		3,		1,		3,		3,		1,		3,		3,		1,		1,		2,		2,		2,		2,		3,		5,		2,		2,		1,		1,		1,		1,		1,		3,		1,		3,		4,		1,		1,		1,		1,		1,			1,			1,		1,		1,		0,		0,		0,		0,		0,		0,		0]
        self.LEFT =  [P,     LDE,	LDE,	DE,	    DE,	    T,	    T,	    T,      T,  	T,  	DT, 	DT, 	DT, 	DC, 	DC, 	DF, 	LP, 	LP, 	B,  	LDV,	LDV,	LS, 	LS, 	DV, 	LI, 	LI, 	S,  	S,  	U,  	U,  	M,	    M,  	M,  	M,  	M,  	M,  	M,  	E,  	E,  	E,  	L,  	L,  	L,  	L,	    L,  	L,  	L,  	R,  	R,	    R,  	Y,  	Y,  	Y,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,  	F,	    LE, 	LE, 	LV,	    LV, 	LV,	    IDD,	IDU,	ID, 	TRUE,   	FALSE,  	CHR,    STR,	NUM,     NB,   	MF,	    MC,	    NF,	    MT, 	ME,	    MW]
        self.TOKEN_TAB_ACTION=[TToken.INTEGER,TToken.CHAR,TToken.BOOLEAN,TToken.STRING,TToken.TYPE,TToken.EQUALS,TToken.ARRAY,TToken.LEFT_SQUARE,TToken.RIGHT_SQUARE,TToken.OF,TToken.STRUCT,TToken.LEFT_BRACES,TToken.RIGHT_BRACES,TToken.SEMI_COLON,TToken.COLON,TToken.FUNCTION,TToken.LEFT_PARENTHESIS,TToken.RIGHT_PARENTHESIS,TToken.COMMA,TToken.VAR,TToken.IF,TToken.ELSE,TToken.WHILE,TToken.DO,TToken.BREAK,TToken.CONTINUE,TToken.AND,TToken.OR,TToken.LESS_THAN,TToken.GREATER_THAN,TToken.LESS_OR_EQUAL,TToken.GREATER_OR_EQUAL,TToken.EQUAL_EQUAL,TToken.NOT_EQUAL,TToken.PLUS,TToken.MINUS,TToken.TIMES,TToken.DIVIDE,TToken.PLUS_PLUS,TToken.MINUS_MINUS,TToken.NOT,TToken.DOT,TToken.ID,TToken.TRUE,TToken.FALSE,TToken.CHARACTER,TToken.STRINGVAL,TToken.NUMERAL,TToken.EOF,PLINHA,P,LDE,DE,T,DT,DC,DF,LP,B,LDV,LS,DV,LI,S,U,M,E,L,R,Y,F,LE,LV,IDD,IDU,ID,TRUE,FALSE,CHR,STR,NUM,NB,MF,MC,NF,MT,ME,MW]

    def run(self):
        state = 0
        self.state_stack.append(state)
        current_token = self.lexical_analyser.next_token()
        action = self.action_table[state+1][self.tokentab(current_token)]
        
        cont=0
        while (action!="acc"):
            #print(state, current_token, action)
            if (action[0]=="s"):
                state=int(action[1:])
                self.state_stack.append(state)
                current_token=self.lexical_analyser.next_token()
                action = self.action_table[state+1][self.tokentab(current_token)]
                cont+=1
            elif (action[0]=="r"):
                rule=int(action[1:])
                for i in range(self.RIGHT[rule-1]):
                    self.state_stack.pop()
                try:
                    state=int(self.action_table[self.state_stack[-1]+1][self.tokentab(LEFT[rule-1])])
                except:
                    print("Erro de sintaxe", state, current_token)
                    break
                self.state_stack.append(state)
                action=self.action_table[state+1][self.tokentab(current_token)]
                cont+=1
                
            else:
                print("Erro de sintaxe", state, current_token)
                break

    def tokentab(self, a):
        return TOKEN_TAB_ACTION.index(a)+1