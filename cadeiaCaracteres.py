def mensagemErro(numero):
    print('\nErro na léxico no caractere de numero:', numero)


def identificar(files_manager, c):
    count = 1
    if c == '\"':
        print(c, end='')
        c = files_manager.ler_char()
        count = count + 1
        while True:
            if c == '\"':
                print(c, end='')
                count = count + 1
                c = files_manager.ler_char()
                if c:
                    mensagemErro(count)
                break
            elif c == '\\':
                if c >= '\x7e':
                    mensagemErro(count)
                    break
                else:
                    c = files_manager.ler_char()
                    count = count + 1
                    print('\\', c, end='')
                    c = files_manager.ler_char()
                    count = count + 1
            elif c >= '\x7e':
                mensagemErro(count)
                break
            else:
                print(c, end='')
                c = files_manager.ler_char()
                count = count + 1

