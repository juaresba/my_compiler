from char_classifier import is_alnum, is_alpha, is_digit, is_space
from token_classifier.classifier import Classifier, TToken
import os

class LexicalAnalyser:
    def __init__(self, code):
        self.next_char = '\x20'
        self.classifier = Classifier()
        try:
            print(code)
            self.code_file = open(code, 'r')
            print(self.code_file)
        except:
            print('Failed to read code file')

    def read_char(self):
        try:
            char = self.code_file.read(1)
        except:
            print("Failed to read char")
        
        return char
    
    def next_token(self):
        token = TToken.UNKNOWN

        # spaces
        while is_space(self.next_char):
            self.next_char = self.read_char()

        # Ids and constants
        if is_alpha(self.next_char):
            token = self.handle_alpha()

        elif is_digit(self.next_char):
            token = self.handle_digit()
        
        elif self.next_char == '"':
            token = self.handle_str()

        elif self.next_char == '\'':
            token = self.handle_char()

        # simbols
        elif self.next_char == ':':
            self.next_char = self.read_char()
            token = TToken.COLON

        elif self.next_char == ';':
            self.next_char = self.read_char()
            token = TToken.SEMI_COLON            

        elif self.next_char == ',':
            self.next_char = self.read_char()
            token = TToken.COMMA

        elif self.next_char == '=':
            self.next_char = self.read_char()
            if self.next_char == '=':
                self.next_char = self.read_char()
                token = TToken.EQUAL_EQUAL      
            else:
                token = TToken.EQUALS                 

        elif self.next_char == '[':
            self.next_char = self.read_char()
            token = TToken.LEFT_SQUARE              

        elif self.next_char == ']':
            self.next_char = self.read_char()
            token = TToken.RIGHT_SQUARE      

        elif self.next_char == '(':
            self.next_char = self.read_char()
            token = TToken.LEFT_PARENTHESIS  

        elif self.next_char == ')':
            self.next_char = self.read_char()
            token = TToken.RIGHT_PARENTHESIS    

        elif self.next_char == '&':
            self.next_char = self.read_char()
            if self.next_char == '&':
                self.next_char = self.read_char()
                token = TToken.AND

        elif self.next_char == '|':
            self.next_char = self.read_char()
            if self.next_char == '|':
                self.next_char = self.read_char()
                token = TToken.OR

        elif self.next_char == '>':
            self.next_char = self.read_char()
            if self.next_char == '=':
                self.next_char = self.read_char()
                token = TToken.GREATER_OR_EQUAL      
            else:
                token = TToken.GREATER_THAN   

        elif self.next_char == '<':
            self.next_char = self.read_char()
            if self.next_char == '=':
                self.next_char = self.read_char()
                token = TToken.LESS_OR_EQUAL      
            else:
                token = TToken.LESS_THAN       
                
        elif self.next_char == '!':
            self.next_char = self.read_char()
            if self.next_char == '=':
                self.next_char = self.read_char()
                token = TToken.NOT_EQUAL      
            else:
                token = TToken.NOT   

        elif self.next_char == '+':
            self.next_char = self.read_char()
            if self.next_char == '+':
                self.next_char = self.read_char()
                token = TToken.PLUS_PLUS      
            else:
                token = TToken.PLUS

        elif self.next_char == '-':
            self.next_char = self.read_char()
            if self.next_char == '-':
                self.next_char = self.read_char()
                token = TToken.MINUS_MINUS      
            else:
                token = TToken.MINUS    

        elif self.next_char == '*':
            self.next_char = self.read_char()
            token = TToken.TIMES

        elif self.next_char == '/':
            self.next_char = self.read_char()
            token = TToken.DIVIDE     

        elif self.next_char == '.':
            self.next_char = self.read_char()
            token = TToken.DOT                

                                                                


        # end of file
        elif self.next_char == '':
            token = TToken.EOF
        
        return token
    
    def handle_alpha(self):
        text = str()
        while True:
            text += self.next_char
            self.next_char = self.read_char()
            if not (is_alnum(self.next_char) or self.next_char == '_'):
                break
        
        token = self.classifier.search_key_word(text)

        # if token == TToken.ID:
        #     secondary_token = self.classifier.search_name(text)

        return token

    def handle_digit(self):
        numeral = str()
        while True:
            numeral += self.next_char
            self.next_char = self.read_char()
            if not is_digit(self.next_char):
                break
        token = TToken.NUMERAL
        # secondary_token =  addIntConst(atoi(numeral))
        return token

    def handle_str(self):
        text = str()
        while True:
            text += self.next_char
            self.next_char = self.read_char()
            if self.next_char == '"':
                break
        text += '"'
        self.next_char = self.read_char()

        token = TToken.STRINGVAL
        # secondary_token = addStringConst(text)
        return token
    
    # question: consider characters with \ before like \n?
    def handle_char(self):
        self.next_char = self.read_char()
        token = TToken.CHARACTER
        # secondary_token = addCharConst(self.next_char)
        self.read_char() # jump the ' character
        self.next_char = self.read_char()

        return token

#example = 'if(2 == 2) { do_something(); }'