def mensagemErro(numero):
    print('\nErro na léxico no caractere de numero:', numero)


with open('input\\teste.txt', 'r+') as file:
    c = file.read(1)
    count = 1
    if c == '\"':
        print(c, end='')
        c = file.read(1)
        count = count + 1
        stop = 1
        while stop == 1:
            if c == '\"':
                print(c, end='')
                count = count + 1
                c = file.read(1)
                if c:
                    mensagemErro(count)
                stop = 0
                break
            elif c == '\\':
                if c >= '\x7e':
                    stop = 0
                    mensagemErro(count)
                    break
                else:
                    c = file.read(1)
                    count = count + 1
                    print('\\', c, end='')
                    c = file.read(1)
                    count = count + 1
            elif c >= '\x7e':
                stop = 0
                mensagemErro(count)
                break
            else:
                print(c, end='')
                c = file.read(1)
                count = count + 1
