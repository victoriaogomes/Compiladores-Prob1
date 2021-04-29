from lexical_analyzer import validator as v
# Classe usada para verificar e manipular os lexemas do tipo operador aritmético.


def identify(files_manager, c, line, symbol_table):
    # Método de identificação, recebe o gerenciador de arquivo,
    # caractere inicial e a tabela de lexemas.
    error = False                                            # Flag de erro levantada pelo método de checagem.
    operator = c                                             # Variável recebe todos os caracteres do operador.
    while True:
        c = files_manager.read_char()                        # Recebe próximo caractere.
        if not c:                                            # Verifica se é final do arquivo.
            break                                            # Saí do while.
        if v.is_arithmetic_delimiter(c) or c == ' ' or v.is_char(c) or c == '\n' or c.isdigit():
            # Verifica se é um critério de parada de leitura.
            files_manager.go_back()                          # Volta o cursor em uma posição no arquivo.
            break
        else:                                                # Caso seja um caractere aceito para ser concatenado.
            operator += c                                    # Concatena o caractere.
    error = check_operator(operator, error)                  # verifica se o operador é aceito pela linguagem.
    if error:                                                # Se retornou erro True.
        symbol_table.add_token('OpMF', operator, line)       # Add na tabela como operador mal formado.
    else:                                                    # Caso contrário.
        symbol_table.add_token('ART', operator, line)        # Add na tabela como operador aritimético.
    return error


def check_operator(op, error):                               # Verifica se o operador é aceito pela linguagem.
    if not op == '+' and not op == '-' and not op == '++' and not op == '--' and not op == '*' and not op == '/':
        return True                                          # Se não for nenhum desses caracteres, retorna erro True.
    else:
        return error                                         # Caso contrário mantém a variável com mesmo valor.
