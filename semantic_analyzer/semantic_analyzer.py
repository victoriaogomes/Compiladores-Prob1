from semantic_analyzer import visitor as vt


class SemanticAnalyzer:

    def __init__(self, symbol_table, ast):
        self.symbol_table = symbol_table
        self.ast = ast

    def analyze(self):
        for statement in self.ast:
            statement.accept(vt.Visitor)
