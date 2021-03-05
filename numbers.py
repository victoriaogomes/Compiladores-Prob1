import validator as v


def identify(files_manager, c):
    error = False
    number = c
    dots = 0
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if c == '.':
            dots += 1
        elif v.is_delimiter(c) or v.is_logic_operator(c) or v.is_arithmetic_operator(c) or v.is_relacional_operator(
                c) or c == ' ' or c == '\n':
            files_manager.go_back()
            break
        number += c
        error = check_number(c, dots, error)
    if error:
        # TODO: adicionar erro léxico de número na tabela de simbolos
        print("Erro no token:", number)
    else:
        # TODO: adicionar número lido corretamente na tabela de simbolos
        print('Número lido corretamente:', number)


def check_number(c, dots, error):
    if not c.isdigit() and not c == '.' or dots > 1:
        return True
    else:
        return error
