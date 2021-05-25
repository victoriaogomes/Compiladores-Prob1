class SymbolTable:

    def __init__(self, parent):
        self.children = []
        self.parent = parent
        self.lines = dict()
        self.key = 0

    def add_child(self, child):
        self.children.append(child)

    def add_line(self, line):
        self.lines[(str(self.key)+'.'+line.name)] = line
        self.key += 1

    def get_line(self, key):
        temp = self.lines.get(key)
        if temp is None:
            return self.parent.get_line(key)
        else:
            return temp


class TableLine:

    def __init__(self, name, tp, data_type, params, program_line, value, index=[-1, -1]):
        self.name = name                                           # Nome do identificador
        self.type = tp                                             # Tipo define se é variável ou função
        self.data_type = data_type                                 # O que a variavel armazena ou o que a função retorna
        self.params = params                                       # Lista de parametros de funções e procedures
        self.program_line = program_line                           # Linha do programa
        self.value = value                                         # Valor armazenado na variável
        self.indexes = index                                       # Index de vetor e matriz

    def reset_for(self, type):
        if type == 0:         # Reset Total
            self.name = ''
            self.type = ''
            self.data_type = ''
            self.params = []
            self.program_line = 0
            self.value = ''
            self.indexes = [-1, -1]
        if type == 1:         # Para Variáveis de mesmo tipo
            self.name = ''
            self.program_line = 0
            self.value = ''
            self.indexes = [-1, -1]
        if type == 2:          # Para variáveis de tipos diferentes na mesma declaração
            self.name = ''
            self.data_type = ''
            self.params = []
            self.program_line = 0
            self.value = ''
            self.indexes = [-1, -1]

