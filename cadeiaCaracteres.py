def mensagemErro(numero):
    print('\nErro na léxico no caractere de numero:', numero)


def identificar(files_manager, c):
    caracteres = c
    count = 1
    if c == '\"':
        c = files_manager.ler_char()
        count = count + 1
        while True:
            if c == '\"':
                caracteres += c
                break
            elif c == '\\':
                c = files_manager.ler_char()
                count = count + 1
                if c >= '\x7e':
                    mensagemErro(count)
                    break
                else:
                    caracteres += c
                    c = files_manager.ler_char()
                    count = count + 1
            elif c >= '\x7e':
                mensagemErro(count)
                break
            else:
                caracteres += c
                c = files_manager.ler_char()
                count = count + 1
    print(caracteres)
