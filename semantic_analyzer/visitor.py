from semantic_analyzer import expressions
from semantic_analyzer import statements


class Visitor:
    @staticmethod
    def visitAssignExpr(expr):
        pass

    @staticmethod
    def visitBinaryExpr(expr):
        pass

    @staticmethod
    def visitFCallExpr(expr):
        pass

    @staticmethod
    def visitStructGetExpr(expr):
        pass

    @staticmethod
    def visitStructSetExpr(expr):
        pass

    @staticmethod
    def visitGroupingExpr(expr):
        pass

    @staticmethod
    def visitLitValExpr(expr):
        return expr.value

    @staticmethod
    def visitLogicalExpr(expr):
        pass

    @staticmethod
    def visitUnaryExpr(expr):
        pass

    @staticmethod
    def visitConstVarAccessExpr(expr):
        pass

    @staticmethod
    def visitFunctionStmt(stmt):
        pass

    @staticmethod
    def visitProcedureStmt(stmt):
        pass

    @staticmethod
    def visitExpressionStmt(stmt):
        pass

    @staticmethod
    def visitIfThenElseStmt(stmt):
        pass

    @staticmethod
    def visitPrintfStmt(stmt):
        pass

    @staticmethod
    def visitReturnStmt(stmt):
        pass

    @staticmethod
    def visitVarStmt(stmt):
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
                    print('######## Entrou nesse else')
                    val.accept(Visitor)

    @staticmethod
    def visitVarBlockStmt(stmt):
        for var in stmt.var_list:
            var.accept(Visitor)

    @staticmethod
    def visitConstStmt(stmt):
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
                val.accept(Visitor)

    @staticmethod
    def visitConstBlockStmt(stmt):
        for const in stmt.const_list:
            const.accept(Visitor)

    @staticmethod
    def visitStructStmt(stmt):
        pass

    @staticmethod
    def visitWhileStmt(stmt):
        pass

    @staticmethod
    def visitTypedefStmt(stmt):
        pass

    @staticmethod
    def visitReadStmt(stmt):
        pass
