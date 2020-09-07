from enum import Enum, auto

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

class TToken(Enum):
    # reserved words -> ok
    ARRAY = auto()
    BOOLEAN = auto() 
    BREAK = auto() 
    CHAR = auto() 
    CONTINUE = auto() 
    DO = auto() 
    ELSE = auto() 
    FALSE = auto() 
    FUNCTION = auto()
    IF = auto() 
    INTEGER = auto() 
    OF = auto() 
    STRING = auto() 
    STRUCT = auto() 
    TRUE = auto() 
    TYPE = auto() 
    VAR = auto() 
    WHILE = auto()

    # simbols
    # Parte Faltando
    COLON = auto() 
    SEMI_COLON = auto() 
    COMMA = auto() 
    EQUALS = auto() 
    LEFT_SQUARE = auto() 
    RIGHT_SQUARE = auto() 
    LEFT_BRACES = auto()
    RIGHT_BRACES = auto() 
    LEFT_PARENTHESIS = auto() 
    RIGHT_PARENTHESIS = auto() 
    AND = auto()
    OR = auto() 
    LESS_THAN = auto() 
    GREATER_THAN = auto() 
    LESS_OR_EQUAL = auto() 
    GREATER_OR_EQUAL = auto()
    NOT_EQUAL = auto() 
    EQUAL_EQUAL = auto() 
    PLUS = auto() 
    PLUS_PLUS = auto() 
    MINUS = auto() 
    MINUS_MINUS = auto() 
    TIMES = auto()
    DIVIDE = auto() 
    DOT = auto() 
    NOT = auto()
    
    # regular tokens -> ok
    CHARACTER = auto()
    NUMERAL = auto()
    STRINGVAL = auto()
    ID = auto()
    
    # end of file -> ok
    EOF = auto()

    # unknown token -> ok
    UNKNOWN = auto()

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