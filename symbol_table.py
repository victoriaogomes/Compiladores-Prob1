class SymbolTable:

    def __init__(self, parent):
        self.children = []
        self.parent = parent
        self.lines = dict()

    def add_child(self, child):
        self.children.append(child)

    def add_line(self, key, name, tp, data_type, params, program_line, value):
        self.lines[key] = TableLine(name, tp, data_type, params, program_line, value)

    def get_line(self, key):
        temp = self.lines.get(key)
        if temp is None:
            return self.parent.get_line(key)
        else:
            return temp


class TableLine:
    def __init__(self, name, tp, data_type, params, program_line, value):
        self.name = name
        self.type = tp
        self.data_type = data_type
        self.params = params
        self.program_line = program_line
        self.value = value
