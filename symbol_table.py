import lexeme


class SymbolTable:

    def __init__(self):
        self.symbol_table = dict()
        self.token_number = 0
        self.printable = ''

    def add_lexeme(self, lexeme_type, lexeme_text, line):
        self.symbol_table[self.token_number] = lexeme.Lexeme(lexeme_type, lexeme_text, line)
        print(self.symbol_table[self.token_number])
        self.printable = self.printable + str(self.symbol_table[self.token_number])
        self.token_number = self.token_number + 1

