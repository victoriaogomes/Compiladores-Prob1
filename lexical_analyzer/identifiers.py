from lexical_analyzer import validator as v
# Classe que identifica e manipula os lexemas do tipo indentificador e palavra reservada.


def identify(files_manager, c, line, symbol_table):
    word = c                                           # word recebe o conjunto de caracteres a serem analisados.
    error = False                                      # Flag de erro.
    if not v.is_char(c):                               # Verifica se c é realmente um char necessário para estar válido.
        error = True                                   # Caso não seja, levanta a flag de erro.
    while True:
        c = files_manager.read_char()                  # Lê próximo caractere.
        if not c:                                      # Verifica se o arquivo já acabou.
            break                                      # Se sim, ele quebra o loop while
        if v.is_delimiter(c) or v.is_logic_operator(c) or v.is_arithmetic_operator(c) or v.is_relacional_operator(
                c) or c == ' ' or c == '\n':           # Verifica se o caractere lido é um critério de parada na...
            files_manager.go_back()                    # concatenação. Caso sim, ele volta o cursor em uma posição.
            break                                      # E consequentemente quebra o loop while.
        else:                                          # Caso contrário ele pode continuar concatenando e verificando.
            word += c                                  # Concatena o caractere na palavra.
        error = check_indentifier(c, error)            # Verifica se o caractere é aceitável no lexema.
    if error:                                          # Se a flag de erro estiver levantada.
        symbol_table.add_token('SIB', word, line)      # Add word na tabela como erro.
    else:                                              # Caso contrário.
        if is_keyword(word):                           # Verifica se word é uma palavra reservada
            symbol_table.add_token('PRE', word, line)  # Se for, é adicionado na tabela como palavra reservada
        else:                                          # Se não for palavra reservada
            symbol_table.add_token('IDE', word, line)  # É adicionado como na tabela como identificador
    return error


def check_indentifier(c, error):                    # Verifica se o caractere recebebido é permitido nesses lexemas.
    if not c.isdigit() and not v.is_char(c) and not c == '_':
        return True                                 # Caso não pertença ao conjunto de caracteres aceitos, retorna true.
    else:
        return error                                # Caso contrário ele mantém o valor da flag.


def is_keyword(word):                               # Verifica se word é uma palavra reservada.
    keywords = ['var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start',
                'return', 'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean',
                'string', 'true', 'false', 'global', 'local']
    return word in keywords                         # Retorna true se conter word dentro desse conjunto de palavras.
