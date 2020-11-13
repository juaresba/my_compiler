from syntactic_analyser import Parser
from lexical_analyser import LexicalAnalyser 


lexical_anl = LexicalAnalyser('test_code2.txt')
parser = Parser(lexical_anl)

parser.run()