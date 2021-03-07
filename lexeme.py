class Lexeme:

    def __init__(self, lexeme_type, lexeme, file_line):
        self.lexeme_type = lexeme_type
        self.lexeme = lexeme
        self.file_line = file_line

    def __str__(self):
        return str(self.file_line) + ' ' + self.lexeme_type + ' ' + self.lexeme + '\n'
        # return "Lexeme type: " + self.lexeme_type + '\n' + "Lexeme: " + self.lexeme \
        #        + '\n' + "File line: " + str(self.file_line)
