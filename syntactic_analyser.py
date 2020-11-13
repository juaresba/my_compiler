from token_classifier import TToken
from non_terminals import NonTerminal, RuleLeftTokens, RuleNumberOfTokens
from action_table import ACTION_TABLE
# from semantics import Analyser

class Parser:
    def __init__(self, lexical_analyser):
        self.action_table = ACTION_TABLE
        self.state_stack = [0]
        self.lexical_analyser = lexical_analyser
        # self.sem = Analyser(lexical_analyser)

    def run(self):
        state = 0
        current_token = self.lexical_analyser.next_token()
        action = self.action_table[state][current_token]
        
        while (action!="acc"):
            print(state, current_token, int(current_token), action)
            if (action[0]=="s"):
                state = int(action[1:])
                self.state_stack.append(state)
                
                current_token=self.lexical_analyser.next_token()
                action = self.action_table[state][current_token]
                
            elif (action[0]=="r"):
                rule = int(action[1:])
                amount_to_pop = RuleNumberOfTokens[rule-1]
                self.state_stack = self.state_stack[:len(self.state_stack) - amount_to_pop]

                temporary_state = self.state_stack[-1]

                left_token = RuleLeftTokens[rule-1]
                state_string = self.action_table[temporary_state][left_token]
                
                state = int(state_string)
                self.state_stack.append(state)

                action = self.action_table[state][current_token]
                
                #self.sem.parse(rule)

            else:
                print("Erro de sintaxe", state, current_token)
                break
        print("No syntactic error!")