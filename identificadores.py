import re


def identificar(files_manager, c):
    palavra = c
    while True:
        d = files_manager.ler_char()
        if not d:
            break
        if re.search(r"[a-z]|[A-Z]|_", d):
            palavra += d
        else:
            files_manager.voltar_cursor()
            break
    match = re.search(r"var|const|typedef|struct|extends|procedure|function|start|return|if|else|"
                      r"then|while|read|print|int|real|boolean|string|true|false|global|local", palavra)
    if not match:
        match = re.search(r"^([a-z]|[A-Z])(\w)*", palavra)
        if not match:
            print("Erro léxico Encontrado")
            # fazer tratamento do erro
        else:
            print('Identificador:', palavra)
            # add na tabela como identificador
    else:
        print('Palavra reservada:', palavra)
        # add na tabela como palavra reservada
