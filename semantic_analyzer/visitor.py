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
        func_pos = self.symbol_table.get_line(expr.token_name.lexeme, expr.scope)
        if not func_pos:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acessar uma function/procedure que não existe!')
        elif len(func_pos) > 1:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Nome de idenficador indexa dois elementos distintos')
        elif func_pos[0].tp not in {'function', 'procedure'}:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: O identificador não corresponde a uma function ou procedure!')
        elif not expr.token_name.file_line >= func_pos[0].program_line:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma function/procedure não definido!')


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
        var_pos = self.symbol_table.get_line(expr.token_name.lexeme, expr.scope)
        if not var_pos:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acessar uma variável/constante que não existe!' )
        elif len(var_pos) > 1:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Nome de idenficador indexa duas variáveis distintas')
        elif var_pos[0].tp not in {'var', 'const'}:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: O identificador não corresponde a uma variavel ou constante!')
        elif not expr.token_name.file_line >= var_pos[0].program_line:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma variavel/constante ainda não declarada!')
        elif not var_pos[0].value:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma variável/constante não inicializada!')

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
        var_pos = self.symbol_table.get_line(stmt.name, stmt.scope)
        if len(var_pos) > 1:
            if not var_pos[0].program_line >= stmt.program_line:
                print(str(stmt.program_line) +
                      ': Erro semântico: Já existe outro elemento indexado com esse identificador')
        if stmt.init_val is not None:
            for val in stmt.init_val:
                if isinstance(val, expressions.LiteralVal):
                    if not ((type(val.value) is str and stmt.tp == 'string') or
                            (type(val.value) is int and stmt.tp == 'int') or
                            (type(val.value) is float and stmt.tp == 'real') or
                            (type(val.value) is bool and stmt.tp == 'boolean')):
                        print(str(stmt.program_line) + ': Erro semântico: Variável do tipo ' + stmt.tp, 'armazenando valor de tipo:',
                              str(type(val.value)))
                else:
                    # Caso o valor inicial seja uma expressão
                    val.accept(self)

    def visitVarBlockStmt(self, stmt):
        for var in stmt.var_list:
            var.accept(self)

    def visitConstStmt(self, stmt):
        const_pos = self.symbol_table.get_line(stmt.name, stmt.scope)
        if len(const_pos) > 1:
            if not const_pos[0].program_line >= stmt.program_line:
                print(str(stmt.program_line) +
                      ': Erro semântico: Já existe outro elemento indexado com esse identificador')
        for val in stmt.init_val:
            if isinstance(val, expressions.LiteralVal):
                if not ((type(val.value) is str and stmt.tp == 'string') or
                        (type(val.value) is int and stmt.tp == 'int') or
                        (type(val.value) is float and stmt.tp == 'real') or
                        (type(val.value) is bool and stmt.tp == 'boolean')):
                    print(str(stmt.program_line) + ': Erro semântico: Constante do tipo ' + stmt.tp, 'armazenando valor de tipo:',
                          str(type(val.value)))
            else:
                # Caso o valor inicial seja uma expressão
                val.accept(self)

    def visitConstBlockStmt(self, stmt):
        for const in stmt.const_list:
            const.accept(self)

    def visitStructStmt(self, stmt):
        if stmt.extends is not None:
            extends_pos = self.symbol_table.get_line(stmt.extends.lexeme, stmt.scope)
            if not extends_pos:
                print(str(stmt.name.file_line) + ': Struct está extendendo uma Struct que não existe!')
            elif stmt.name.file_line < extends_pos[0].program_line and extends_pos[0].tp == 'struct':
                print(str(stmt.name.file_line) + ': Struct está extendendo uma Struct ainda não definida!')

    def visitWhileStmt(self, stmt):
        pass

    def visitTypedefStmt(self, stmt):
        pass

    def visitReadStmt(self, stmt):
        pass
