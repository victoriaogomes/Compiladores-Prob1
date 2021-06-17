from semantic_analyzer import visitor as vt


class SemanticAnalyzer:

    def __init__(self, symbol_table, ast, tokens_list):
        self.symbol_table = symbol_table
        self.ast = ast
        self.tokens_list = tokens_list
        self.visitor = vt.Visitor(self.symbol_table, tokens_list)

    def analyze(self):
        for statement in self.ast:
            statement.accept(self.visitor)
        return self.visitor.tokens_list
