from token_classifier.classifier import TToken
from main import LexicalAnalyser

lexical_analyser = LexicalAnalyser('test_code.txt')

while True:
    token = lexical_analyser.next_token()
    print(token)
    if token == TToken.EOF:
        break

# for word in TToken:
#     print(word)