from token_classifier import TToken
from lexical_analyser import LexicalAnalyser

lexical_analyser = LexicalAnalyser('test_code.txt')

while True:
    token = lexical_analyser.next_token()
    print(token)
    if token == TToken.EOF:
        break

print(lexical_analyser.classifier.const_table)