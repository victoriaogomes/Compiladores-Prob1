import filesManager
import cadeiaCaracteres
import identificadores
import operadores_aritmeticos
import numeros
import re

lista_arquivos = filesManager.lista_arquivos('input')

for arquivo in lista_arquivos:
    filesManager.abrir_arquivo('input\\' + arquivo)


def identificar_lexemas():
    while True:
        c = filesManager.ler_char()
        if not c:
            break
        if c == '\"':
            cadeiaCaracteres.identificar(filesManager)
        elif re.search(r"[a-z]|[A-Z]", c):
            identificadores.identificar(filesManager)
        elif re.search(r"[0-9]", c):
            numeros.identificar(filesManager)
        elif c == '+' or c == '-' or c == '*' or c == '/':   #### REVER POR CONTA DA BARRA
            operadores_aritmeticos.identificar(filesManager)
        elif c == '!':
            d = filesManager.ler_char()
            filesManager.voltar_cursor()
            if d == '=':
                # Vai pra operador relacional
            else:
                # Vai pra operador lógico
        elif c == '&' or c == '|':
            # Vai pra operador lógico
        elif c == '=' or c == '>' or c == '>':
            # Vai pra operador relacional
        elif c == ';' or c == ',' or c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}' or c == '.':
            # Vai para delimitador