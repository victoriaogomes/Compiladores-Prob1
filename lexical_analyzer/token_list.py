import operator
from lexical_analyzer import tokens

# Classe utilizada para a manipulação da lista de tokens que é resultado da análise léxica
# e dos erros gerados pela análise sintática


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
        self.endFileToken.file_line = line

    def get_tokens(self):
        # Método responsável por retornar de maneira ordenada todos os tokens previamente cadastrados na tabela de
        # símbolos em forma de string, a qual será utilizada para escrever no arquivo de saída
        self.tokens_list = sorted(self.tokens_list.values(), key=operator.attrgetter('file_line'))
        for key in self.tokens_list:
            self.printable = self.printable + str(key)
        return self.printable

    def lookahead(self):
        if self.current_index + 1 < len(self.tokens_list):
            if self.tokens_list[self.current_index + 1] in {'SIB', 'NMF', 'CMF', 'OpMF'}:
                self.consume_token()
            return self.tokens_list[self.current_index + 1]
        else:
            return self.endFileToken

    def consume_token(self):
        if self.current_index + 1 < len(self.tokens_list):
            self.current_index += 1
            if self.lookahead().lexeme_type in {'SIB', 'NMF', 'CMF', 'OpMF'}:
                self.consume_token()
            else:
                return self.tokens_list[self.current_index]
        else:
            return self.endFileToken
