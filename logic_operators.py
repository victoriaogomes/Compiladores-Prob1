import validator as v


def identify(files_manager, c):
    operator = c
    error = False
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if v.is_delimiter_special(c) or v.is_char(c) or c == ' ' or c == '\n':
            files_manager.go_back()
            break
        else:
            operator += c + 1
    error = check_logic(operator, error)
    if error:
        # TODO: Colocar na tabela de erros
        print('Erro léxico no operador lógico:', operator)
    else:
        # TODO: Colocar na tabela de simbolos
        print('Operador lógico lido corretamente:', operator)


def check_logic(op, error):
    if not op == '&&' and op == '||' and op == '!':
        return True
    else:
        return error
