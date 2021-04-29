import filesManager
from syntactic_analyzer import syntactic_analyzer as s_analyzer
from lexical_analyzer import logic_operators
from lexical_analyzer import delimitador
from lexical_analyzer import number
from lexical_analyzer import arithmetic_operators
from lexical_analyzer import caracter_chain
from lexical_analyzer import identifiers
from lexical_analyzer import relational_operators
from lexical_analyzer import token_list as table

# Classe principal do projeto, utilizada para verificar a lista de arquivos presente no folder input, abrir cada um
# deles, remover seus comentários, analisá-los lexicamente, obtendo seus tokens correspondentes e, em seguida, armaze-
# nar o resultado nessa análise em um arquivo correspondente no folder output


print('################## Welcome to Unicorn.io ###################')
lista_arquivos = filesManager.list_files('input')  # Obtém a lista dos arquivos presentes no diretório input
lista_arquivos.sort(key=len)
filesManager.clean_folder('output')  # Remove todos os arquivos presentes no folder output
lexicalError = False  # Flag usada para verificar se algum erro léxico foi encontrado


def identify_lexemes(arquivo, symbol_table):  # Método que identifica os lexemas presentes no arquivo recebido
    error = False
    line = 1
    while True:  # Loop utilizado para ler o arquivo, caractere por caractere
        c = filesManager.read_char()
        if not c:  # Caso encontremos o fim do arquivo, saímos do loop de leitura
            break
        if c == '\n':  # Caso encontremos uma quebra de linha, incrementamos o contador line
            line = line + 1
        elif c == '\"':
            # --- Identificação de cadeia de caracteres, iniciada caso o último char lido sejam aspas
            error = True if caracter_chain.identify(filesManager, c, line, symbol_table) else error
        elif c.isdigit():
            # --- Identificação de número, iniciada caso o último char lido seja um dígito
            error = True if number.identify(filesManager, c, line, symbol_table) else error
        elif c == '+' or c == '-' or c == '*' or c == '/':
            # --- Identificação de operador aritmético, iniciada caso o último char lido seja algum dos listados acima
            error = True if arithmetic_operators.identify(filesManager, c, line, symbol_table) else error
        elif c == '!':  # Caso o último char lido seja uma !
            d = filesManager.read_char()  # Lemos o char seguinte
            filesManager.go_back()  # Damos um passo para trás com a cabeça de leitura
            if d == '=':  # Caso esse char lido na sequência seja um =
                # Identificação de operador relacional, iniciada após a leitura de um ! seguido de um =
                error = True if relational_operators.identify(filesManager, c, line, symbol_table) else error
            else:
                # Identificação de operador lógico, iniciada após a leitura de um ! seguido de qualquer outra coisa
                error = True if logic_operators.identify(filesManager, c, line, symbol_table) else error
        elif c == '&' or c == '|':
            # Identificação de operador lógico, iniciada caso o último char lido seja algum dos listados acima
            error = True if logic_operators.identify(filesManager, c, line, symbol_table) else error
        elif c == '=' or c == '>' or c == '<':
            # Identificação de operador relacional, iniciada caso o último char lido seja algum dos listados acima
            error = True if relational_operators.identify(filesManager, c, line, symbol_table) else error
        elif c == ';' or c == ',' or c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}' or c == '.':
            # Identificação de delimitador, iniciada caso o último char lido seja algum dos listados acima
            delimitador.add_table(line, c, symbol_table)
        elif not c == ' ' and not c == '\t':
            # Identificação de identificador, palavra reservada ou qualquer outro lexema que não atenda aos padrões de-
            # finidos pela linguagem que está sendo compilada
            error = True if identifiers.identify(filesManager, c, line, symbol_table) else error
    # Após finalizar a identificação de todos os lexemas presente no arquivo, os tokens levantados são escritos no ar-
    # quivo de saída
    filesManager.write_symbol_table(symbol_table.get_tokens(), arquivo)
    return error


def clear_comments(file, symbol_table):  # Método utilizado para remover os comentários presentes nos arquivos
    error = False
    line = 1
    mensagem = ''  # Mensagem que será escrita no arquivo auxiliar para extrair tokens
    while True:  # Loop utilizado para ler o arquivo, caractere por caractere
        c = filesManager.read_char()
        if not c:  # Caso encontremos o fim do arquivo, saímos do loop de leitura
            break
        if c == '\n':  # Caso encontremos uma quebra de linha, incrementamos o contador line
            line += 1
        if c == '/':  # Caso encontremos uma /, começamos a buscar por outra ou um *
            acd = c
            c = filesManager.read_char()
            if c == '/':  # Caso o caractere seguinte seja /, temos um comentário de linha
                while True:  # Continuamos lendo o arquivo até encontrarmos o fim dele ou um \n
                    if c == '\n':
                        filesManager.go_back()
                        break
                    if not c:
                        break
                    c = filesManager.read_char()
            elif c == '*':  # Caso o caractere seguinte seja *, temos um comentário de bloco
                comentario_line = line  # Salvamos a linha onde o comentário de bloco começa
                c = filesManager.read_char()
                d = filesManager.read_char()
                while c != '*' and d != '/':  # Continuamos lendo o arquivo até encontrarmos o fim dele ou um */
                    if c == '\n':
                        mensagem += '\n'
                        line += 1
                    c = d
                    d = filesManager.read_char()
                    if not d:  # Caso encontremos o fim do arquivo antes do */, indicamos um erro
                        symbol_table.add_token('CoMF', 'Fim de arquivo inesperado', comentario_line)
                        error = True
                        break
            else:
                if acd == '/':
                    mensagem += acd
                mensagem += c
        else:
            mensagem += c
    # Ao finalizar a remoção dos comentários desnecessários, reescrevemos o arquivo "limpo" em um arquivo auxiliar para
    # posterior análise dos seus lexemas
    filesManager.write(mensagem, 'auxiliar_files\\' + file)
    return error


tableList = []  # Vetor que contém a tabela de símbolos de cada um dos arquivos analisados
for i in range(len(lista_arquivos)):  # Para cada arquivo presente no folder input
    filesManager.open_file('input\\' + lista_arquivos[i])
    tableList.append(table.TokenList())
    commentsError = clear_comments(lista_arquivos[i], tableList[i])  # Removemos os comentários presentes no arquivo
    filesManager.close_file()
    filesManager.open_file('auxiliar_files\\' + lista_arquivos[i])
    lexicalError = identify_lexemes(lista_arquivos[i], tableList[i])  # Analisamos lexicamente o conteúdo do arquivo
    filesManager.close_file()
    print('--- Conclusão da análise léxica do arquivo', lista_arquivos[i])
    analyzer = s_analyzer.SyntacticAnalyzer(tableList[-1])
    analyzer.start()
    print('Foram encontrados erros lexicos\n') if (lexicalError or commentsError) else print('Não foram encontrados '
                                                                                             'erros lexicos\n')

filesManager.clean_folder('auxiliar_files')  # Limpa o folder com arquivos auxiliares que foram criados para a análise
lista_arquivos = filesManager.list_files('auxiliar_files')
