from os import listdir
from os.path import isfile, join
import os


def lista_arquivos(path):                                        # Caminho do diretório que será analisado
    files = [f for f in listdir(path) if isfile(join(path, f))]  # Não faço idéia do que ele está fazendo aqui
    print(files)                                                 # Printa os arquivos no diretório que foi passado
    print('O directório possui:', len(files), 'arquivos')        # len() retorn o tamanho do array
    print('#############################')
    return files


def escrever_arquivos():
    file.write('Foi escrito no arquivo!!!')                     # file.write escvreve no arquivo destino,
    file.write('\nEscrevi dnv')                                 # caso não exista esse arquivo, ele cria um.
    file.seek(0, 0)                                             # Volta o cursor para o início do documento


def ler_tudo():
    print(file.read(), '\n')                                    # Lê tdo o arq passado
    print('#############################')
    file.seek(0, 0)


def ler_linha():
    return file.readline()
    # print('Linha lida:', file.readline(), end='')   # readLine lê uma linha por vez | end='' retira o \n no final


def soma(a, b):                                     # Testando o retorno de parâmetros em python
    return a+b


def remove_output():                                # Metodo de remover os arquivos do output que n funciona ainda
    arqs = lista_arquivos('output')
    if len(arqs) != 0:                               # Espero que esse if esteja certo
        for n in arqs:
            print(n)
            caminho = 'output\\' + n
            os.remove(caminho)


def ler_char():
    return file.read(1)


file = open('output\\saida01.txt', 'w+')    # Abre o arquivo com o caminho dado
lista_arquivos('input')                     # w = write, r = read, a = append,
'''
escrever_arquivos()                         # + = deixa atualizar (por algum motivo deixa ler e escrever junto)
ler_tudo()
ler_linha()
ler_linha()
file.readlines()                            # Retorna as linhas em um vetor (interessante)
print('\nSoma igual a:', soma(77, 33))
file.close()                                # Sempre fechar o arquivo quando abrir para não ter erro
'''

