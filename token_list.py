import operator
import tokens

# Classe utilizada para a manipulação da tabela de símbolos que é gerada como resultado da análise léxica


class TokenList:

    def __init__(self):
        # Método utilizado para inicializar os atributos presentes nesta classe
        self.symbol_table = dict()
        self.token_number = 0
        self.printable = ''

    def add_token(self, lexeme_type, lexeme_text, line):
        # Método utilizado para adicionar um novo token na tabela de símbolos
        self.symbol_table[self.token_number] = tokens.Token(lexeme_type, lexeme_text, line)
        self.token_number = self.token_number + 1

    def get_tokens(self):
        # Método responsável por retornar de maneira ordenada todos os tokens previamente cadastrados na tabela de
        # símbolos em forma de string, a qual será utilizada para escrever no arquivo de saída
        self.symbol_table = sorted(self.symbol_table.values(), key=operator.attrgetter('file_line'))
        for key in self.symbol_table:
            self.printable = self.printable + str(key)
        return self.printable
