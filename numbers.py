import validator as v


def identify(files_manager, c, line, symbol_table):
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
            print('Recebi: ', c)
            files_manager.go_back()
            break
        number += c
        error = check_number(c, dots, error)
    if error:
        symbol_table.add_lexeme('NMF', number, line)
    else:
        symbol_table.add_lexeme('NRO', number, line)


def check_number(c, dots, error):
    if not c.isdigit() and not c == '.' or dots > 1:
        return True
    else:
        return error
