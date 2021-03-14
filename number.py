import validator as v

# Classe utilizada para as verificações e manipulações necessárias do analisador léxico no que tange o uso de números


def identify(files_manager, c, line, symbol_table):
    # Método utilizado para verificar efetivamente se o char que foi recebido por parâmetro realmente constitui um
    # número
    error = False     # Flag de erro usada para verificar se a construção do número está correta
    number = c
    dots = 0
    while True:       # Loop utilizado para fazer a leitura do número, respeitando seus delimitadores
        c = files_manager.read_char()
        if not c:     # Caso estejamos no fim do arquivo, devemos encerrar a leitura
            break
        if c == '.':  # Caso o char lido seja um ponto, incrementamos a variável que conta a presença deles no número
            dots += 1
        elif v.is_delimiter(c) or v.is_logic_operator(c) or v.is_arithmetic_operator(c) or v.is_relacional_operator(
                c) or c == ' ' or c == '\n':
            # Caso encontremos um delimitador, um operador lógico, um operador aritmético, um operador relacional, um
            # espaço em branco ou uma quebra de linha, devemos finalizar a leitura do lexema, dar um passo para trás e
            # classificar o que foi lido
            files_manager.go_back()
            break
        number += c
        error = check_number(c, dots, error)  # Verifica se o número lido está construído corretamente
    if error:         # Adiciona na tabela de símbolos um token indicando a presença de um número mal formado
        symbol_table.add_token('NMF', number, line)
    else:             # Adiciona na tabela de símbolos um token indicando a presença de um número
        symbol_table.add_token('NRO', number, line)


def check_number(c, dots, error):
    # Método utilizado para checar se o número lido se encontra no padrão definido para a linguagem que está sendo
    # compilada
    if not c.isdigit() and not c == '.' or dots > 1:
        return True
    else:
        return error
