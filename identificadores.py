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


# def identificar(files_manager, c):
#     palavra = c
#     while True:
#         d = files_manager.ler_char()
#         if not d:
#             break
#         if re.search(r"[a-z]|[A-Z]|_", d):
#             palavra += d
#         else:
#             files_manager.voltar_cursor()
#             break
#     match = re.search(r"var|const|typedef|struct|extends|procedure|function|start|return|if|else|"
#                       r"then|while|read|print|int|real|boolean|string|true|false|global|local", palavra)
#     if not match:
#         match = re.search(r"^([a-z]|[A-Z])(\w)*", palavra)
#         if not match:
#             print("Erro léxico Encontrado")
#             # fazer tratamento do erro
#         else:
#             print('Identificador:', palavra)
#             # add na tabela como identificador
#     else:
#         print('Palavra reservada:', palavra)
#         # add na tabela como palavra reservada
