from semantic_analyzer import visitor as vt


class SemanticAnalyzer:

    def __init__(self, symbol_table, ast):
        self.symbol_table = symbol_table
        self.ast = ast
        self.visitor = vt.Visitor(self.symbol_table)

    def analyze(self):
        for statement in self.ast:
            statement.accept(self.visitor)
