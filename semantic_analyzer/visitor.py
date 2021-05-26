from semantic_analyzer import expressions
from semantic_analyzer import statements


class Visitor:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def visitAssignExpr(self, expr):
        pass

    def visitBinaryExpr(self, expr):
        pass

    def visitFCallExpr(self, expr):
        pass

    def visitStructGetExpr(self, expr):
        pass

    def visitStructSetExpr(self, expr):
        pass

    def visitGroupingExpr(self, expr):
        pass

    def visitLitValExpr(self, expr):
        return expr.value

    def visitLogicalExpr(self, expr):
        pass

    def visitUnaryExpr(self, expr):
        pass

    def visitConstVarAccessExpr(self, expr):
        var_pos = self.symbol_table.get_line(expr.token_name.lexeme)
        if not var_pos:
            print('Erro Semântico: Tentativa de acessar uma variável que não existe!')
        elif not var_pos[0].value:
            print('Erro Semântico: Tentativa de acesso a uma variável não inicializada!')

    def visitFunctionStmt(self, stmt):
        pass

    def visitProcedureStmt(self, stmt):
        pass

    def visitExpressionStmt(self, stmt):
        pass

    def visitIfThenElseStmt(self, stmt):
        pass

    def visitPrintfStmt(self, stmt):
        pass

    def visitReturnStmt(self, stmt):
        pass

    def visitVarStmt(self, stmt):
        if stmt.init_val is not None:
            for val in stmt.init_val:
                if isinstance(val, expressions.LiteralVal):
                    if not ((type(val.value) is str and stmt.tp == 'string') or
                            (type(val.value) is int and stmt.tp == 'int') or
                            (type(val.value) is float and stmt.tp == 'real') or
                            (type(val.value) is bool and stmt.tp == 'boolean')):
                        print('Erro semântico: Variável do tipo ' + stmt.tp, 'armazenando valor de tipo:',
                              str(type(val.value)))
                else:
                    # Caso o valor inicial seja uma expressão
                    val.accept(self)

    def visitVarBlockStmt(self, stmt):
        for var in stmt.var_list:
            var.accept(self)

    def visitConstStmt(self, stmt):
        for val in stmt.init_val:
            if isinstance(val, expressions.LiteralVal):
                if not ((type(val.value) is str and stmt.tp == 'string') or
                        (type(val.value) is int and stmt.tp == 'int') or
                        (type(val.value) is float and stmt.tp == 'real') or
                        (type(val.value) is bool and stmt.tp == 'boolean')):
                    print('Erro semântico: Constante do tipo ' + stmt.tp, 'armazenando valor de tipo:',
                          str(type(val.value)))
            else:
                # Caso o valor inicial seja uma expressão
                val.accept(self)

    def visitConstBlockStmt(self, stmt):
        for const in stmt.const_list:
            const.accept(self)

    def visitStructStmt(self, stmt):
        if stmt.extends is not None:
            extends_pos = self.symbol_table.get_line(stmt.extends.lexeme)
            if not extends_pos:
                print('Struct está extendendo uma Struct que não existe!')
            elif stmt.name.file_line < extends_pos[0].program_line:
                print('Struct está extendendo uma Struct ainda não definida!')

    def visitWhileStmt(self, stmt):
        pass

    def visitTypedefStmt(self, stmt):
        pass

    def visitReadStmt(self, stmt):
        pass
