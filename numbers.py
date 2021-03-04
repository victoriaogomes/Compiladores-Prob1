import validator as v


def identify(files_manager, c):
    error = False
    number = c
    count = 1
    dots = 0
    while True:
        c = files_manager.ler_char()
        count = count + 1
        if c == '.':
            dots += 1
        elif v.is_delimiter(c) or v.is_logic_operator(c) or v.is_arithmetic_operator(c) or v.is_relacional_operator(
                c) or c == ' ':
            break
        number += c
        error = check_number(c, dots)
    if error:
        # TODO: adicionar erro léxico de número na tabela de simbolos
        print("Erro no token:", number)
    else:
        # TODO: adicionar número lido corretamente na tabela de simbolos
        print('Número lido corretamente:', number)
    files_manager.go_back()


def check_number(c, dots):
    if not c.isdigit() or dots > 1:
        return True
    else:
        return False
