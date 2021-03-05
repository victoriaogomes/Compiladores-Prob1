import filesManager
import caracter_chain
import validator as v
import identifiers
import numbers
import arithmetic_operators

lista_arquivos = filesManager.list_files('input')


def identify_lexemes():
    while True:
        c = filesManager.read_char()
        if not c:
            print('Fim de arquivo main')
            break
        if c == '\"':
            print('--- Entrou na identificação de cadeia de caracteres')
            caracter_chain.identify(filesManager, c)
        elif v.is_char(c):
            print('--- Entrou na identificação de identificador')
            identifiers.identify(filesManager, c)
        elif c.isdigit():
            print('--- Entrou na identificação de número')
            numbers.identify(filesManager, c)
        elif c == '+' or c == '-' or c == '*' or c == '/':
            print('--- Entrou na identificação de operador aritmético')
            arithmetic_operators.identify(filesManager, c)
        # elif c == '!':
        #     d = filesManager.ler_char()
        #     filesManager.voltar_cursor()
        #     if d == '=':
        #         # Vai pra operador relacional
        #     else:
        #         # Vai pra operador lógico
        # elif c == '&' or c == '|':
        #     # Vai pra operador lógico
        # elif c == '=' or c == '>' or c == '>':
        #     # Vai pra operador relacional
        # elif c == ';' or c == ',' or c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}' or c == '.':
        #     # Vai para delimitador


for arquivo in lista_arquivos:
    filesManager.open_file('input\\' + arquivo)
    identify_lexemes()
