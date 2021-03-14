import re

# Classe utilizada para validar um char, onde é verificado em qual das categorias abaixo ele pertence:
#   -  Delimitador (em geral, delimitador especial ou delimitador de operador aritmético)
#   -  Letra
#   -  Operador relacional
#   -  Operador aritmético
#   -  Operador lógico


def is_delimiter_special(c):
    # Método utilizado para verificar se o char recebido por parâmetro é delimitador "especial"
    # Ou seja, qualquer delimitador exceto o ponto e vírgula, a vírgula e o ponto
    if c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']':
        return True
    else:
        return False


def is_delimiter(c):
    # Método utilizado para verificar se o char recebido por parâmetro é um delimitador
    if c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']' or c == ';' or c == ',' or c == '.':
        return True
    else:
        return False


def is_arithmetic_delimiter(c):
    # Método para verificar se o char recebido por parâmetro é delimitador de um operador aritmético
    if c == '(' or c == ')' or c == ';' or c == ',':
        return True
    else:
        return False


def is_char(c):
    # Método utilizado pra verificar se o char recebido por parâmetro é uma letra do alfabeto, seja ela maiúscula
    # ou minúsucla
    if re.search(r"[a-z]|[A-Z]", c):
        return True
    else:
        return False


def is_logic_operator(c):
    # Método utilizado para verificar se o char recebido por parâmetro é um operador lógico
    if c == '&' or c == '|' or c == '!':
        return True
    else:
        return False


def is_arithmetic_operator(c):
    # Método utilizado para verificar se o char recebido por parâmetro é um operador aritmético
    if c == '+' or c == '-' or c == '*' or c == '/':
        return True
    else:
        return False


def is_relacional_operator(c):
    # Método utilizado para verificar se o char recebido por parâmetro é um operador relacional
    if c == '!' or c == '=' or c == '>' or c == '<':
        return True
    else:
        return False
