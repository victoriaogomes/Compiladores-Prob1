# Classe utilizada para armazenar as informações necessárias referentes a um token, a saber:
#   -  O tipo de lexema que ele representa
#   -  O lexema em si que foi encontrado
#   -  A linha na qual o lexema foi encontrado

class Token:

    def __init__(self, lexeme_type, lexeme, file_line):
        # Método utilizado para inicializar os atributos presentes nesta classe
        self.lexeme_type = lexeme_type
        self.lexeme = lexeme
        self.file_line = file_line

    def __str__(self):
        # Reescrita do método str, utilizada para definir que string queremos que seja retornada quando colocamos
        # diretamente para um objeto desta classe ser impresso
        return str(self.file_line) + ' ' + self.lexeme_type + ' ' + self.lexeme + '\n'
