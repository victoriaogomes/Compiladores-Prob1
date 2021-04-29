import operator
from lexical_analyzer import tokens

# Classe utilizada para a manipulação da tabela de símbolos que é gerada como resultado da análise léxica


class TokenList:

    def __init__(self):
        # Método utilizado para inicializar os atributos presentes nesta classe
        self.tokens_list = dict()
        self.token_number = 0
        self.printable = ''
        self.current_index = -1
        self.endFileToken = tokens.Token('EOF', 'endOfFile($)', 0)

    def add_token(self, lexeme_type, lexeme_text, line):
        # Método utilizado para adicionar um novo token na tabela de símbolos
        self.tokens_list[self.token_number] = tokens.Token(lexeme_type, lexeme_text, line)
        self.token_number = self.token_number + 1

    def get_tokens(self):
        # Método responsável por retornar de maneira ordenada todos os tokens previamente cadastrados na tabela de
        # símbolos em forma de string, a qual será utilizada para escrever no arquivo de saída
        self.tokens_list = sorted(self.tokens_list.values(), key=operator.attrgetter('file_line'))
        for key in self.tokens_list:
            self.printable = self.printable + str(key)
        return self.printable

    def lookahead(self):
        return self.tokens_list[self.current_index + 1]

    def consume_token(self):
        if self.current_index < len(self.tokens_list):
            self.current_index += 1
            return self.tokens_list[self.current_index]
        else:
            return self.endFileToken
