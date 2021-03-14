import validator as v


def identify(files_manager, c, line, symbol_table):
    error = False
    operator = c
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if v.is_arithmetic_delimiter(c) or c == ' ' or v.is_char(c) or c == '\n' or c.isdigit():
            files_manager.go_back()
            break
        else:
            operator += c
    error = check_operator(operator, error)
    if error:
        symbol_table.add_token('OpMF', operator, line)
    else:
        symbol_table.add_token('ART', operator, line)


def check_operator(op, error):
    if not op == '+' and not op == '-' and not op == '++' and not op == '--' and not op == '*' and not op == '/':
        return True
    else:
        return error
