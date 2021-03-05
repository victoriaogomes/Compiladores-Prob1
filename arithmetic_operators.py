import validator as v


def identify(files_manager, c):
    error = False
    operator = c
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if v.is_delimiter(c) or c == ' ' or v.is_char(c):
            files_manager.go_back()
            break
        else:
            operator += c
    error = check_operator(operator, error)
    if error:
        # TODO: adicionar erro léxico de operador aritmético
        print('Erro léxico no operador aritmético:', operator)
    else:
        # TODO: adicionar token de operador aritmético na tabela de simbolos
        print('Operador aritmético:', operator)


def check_operator(op, error):
    if not op == '+' and not op == '-' and not op == '++' and not op == '--' and not op == '*' and not op == '/':
        return True
    else:
        return error
