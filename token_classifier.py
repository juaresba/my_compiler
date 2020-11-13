from enum import IntEnum, auto

RESERVED_WORDS = set([
    'array',
    'boolean', 
    'break', 
    'char', 
    'continue', 
    'do', 
    'else', 
    'false', 
    'function',
    'if', 
    'integer', 
    'of', 
    'string', 
    'struct', 
    'true', 
    'type', 
    'var', 
    'while',
])

class TToken(IntEnum):
    def _generate_next_value_(name, start, count, last_values):
        start = 0
        return start + count

    INTEGER = auto()
    CHAR = auto()
    BOOLEAN = auto()
    STRING = auto()
    TYPE = auto()
    EQUALS = auto()
    ARRAY = auto()
    LEFT_SQUARE = auto() 
    RIGHT_SQUARE = auto()
    OF = auto()
    STRUCT = auto()
    LEFT_BRACES = auto()
    RIGHT_BRACES = auto()
    SEMI_COLON = auto()
    COLON = auto()
    FUNCTION = auto()
    LEFT_PARENTHESIS = auto() 
    RIGHT_PARENTHESIS = auto() 
    COMMA = auto()
    VAR = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    DO = auto()
    BREAK = auto() 
    CONTINUE = auto() 
    AND = auto()
    OR = auto()
    LESS_THAN = auto() 
    GREATER_THAN = auto() 
    LESS_OR_EQUAL = auto() 
    GREATER_OR_EQUAL = auto()
    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()
    PLUS = auto()
    MINUS = auto()
    TIMES = auto()
    DIVIDE = auto()
    PLUS_PLUS = auto()  
    MINUS_MINUS = auto() 
    NOT = auto()
    DOT = auto() 
    ID = auto()
    TRUE = auto() 
    FALSE = auto()   
    CHARACTER = auto()
    STRINGVAL = auto()
    NUMERAL = auto()
    EOF = auto()
    UNKNOWN = -1
    

class Classifier:
    def __init__(self):
        self.const_table = dict()
        self.const_values = dict()

    def search_key_word(self, word):
        if word in RESERVED_WORDS:
            reserved_word_token = TToken[word.upper()]
            return reserved_word_token
        else:
            return TToken.ID
    
    def search_name(self, word):
        if word in self.const_table:
            return self.const_table[word]
        else:
            secondary_token = len(self.const_table)
            self.const_table[word] = secondary_token
            
            return self.const_table[word] 