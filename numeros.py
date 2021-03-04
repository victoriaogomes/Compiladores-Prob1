import filesManager
import validator as v

def identificar(files_manager, c):
    numero = c
    count = 1
    pontos = 0
    while True:
        c = files_manager.ler_char()
        count + count + 1
        if(c == '.'):
            numero += c
            pontos += 1
        elif v.is_delimiter(c) or v.is_logic_operator(c) or v.is_arithmetic_operator(c) or v.is_relacional_operator(c) or c == ' ':
            # TODO: adicionar tokens na tabela de simbolos
            files_manager.go_back()
            print('Numero lido:', numero)
            break
        else:
            numero += c




