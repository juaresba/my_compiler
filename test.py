from token_classifier import TToken
from lexical_analyser import LexicalAnalyser
from action_table import ACTION_TABLE

# lexical_analyser = LexicalAnalyser('test_code.txt')

# while True:
#     token = lexical_analyser.next_token()
#     print(token)
#     if token == TToken.EOF:
#         break

# print(lexical_analyser.classifier.const_table)

table = ACTION_TABLE

print(table[0], '\n', table[0][41], table[0][42], table[0][43])