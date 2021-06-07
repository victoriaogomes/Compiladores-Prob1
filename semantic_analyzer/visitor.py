from semantic_analyzer import expressions
from semantic_analyzer import statements


class Visitor:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def visitAssignExpr(self, expr):
        var_pos = self.symbol_table.get_line(expr.token.lexeme, expr.scope)
        if not var_pos:
            print(str(expr.token.file_line) + ': Erro Semântico: Tentativa de atribuir valor uma variável que '
                                              'não existe!')
        elif var_pos[0].tp != 'var':
            print(str(expr.token.file_line) + ': Erro Semântico: Identificador informado não corresponde a '
                                              'uma variável, e sim a uma', var_pos[0].tp)

    def visitBinaryExpr(self, expr):
        right_side = ''
        left_side = ''
        inner_error = False
        if isinstance(expr.left_expr, expressions.LiteralVal):
            left_side = str(type(expr.value))
        elif isinstance(expr.left_expr, expressions.ConstVarAccess):
            left_side = expr.left_expr.accept(self)
        elif isinstance(expr.left_expr, expressions.FunctionCall):
            aux = expr.left_expr.accept(self)
            if aux is None:
                inner_error = True
            else:
                left_side = aux.data_type
        if isinstance(expr.right_expr, expressions.LiteralVal):
            right_side = str(type(expr.value))
        elif isinstance(expr.right_expr, expressions.ConstVarAccess):
            right_side = expr.right_expr.accept(self)
        elif isinstance(expr.right_expr, expressions.FunctionCall):
            aux = expr.right_expr.accept(self)
            if aux is None:
                inner_error = True
            else:
                right_side = aux.data_type


    def visitFCallExpr(self, expr):
        func_pos = self.symbol_table.get_line(expr.func_exp.lexeme, -1)
        if not func_pos:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: Tentativa de acessar uma function/procedure que não existe!')
            return None
        elif len(func_pos) > 1:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: Nome de idenficador indexa dois elementos distintos')
            return None
        elif func_pos[0].tp not in {'function', 'procedure'}:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: O identificador não corresponde a uma function ou procedure!')
            return None
        elif not expr.func_exp.file_line >= func_pos[0].program_line:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma function/procedure ainda não definido!')
            return None
        return func_pos[0]


    def visitStructGetExpr(self, expr):
        pass

    def visitGroupingExpr(self, expr):
        return expr.expr.accept(self)

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
            return var_pos[0].data_type
        elif expr.index_array is not None:
            if isinstance(expr.index_array, expressions.LiteralVal):
                aux = expr.index_array.accept(self)
                if not isinstance(aux, int):
                    print(str(expr.token_name.file_line) + ': Erro Semântico: Um index de um vetor/matriz deve ser'
                                                           'um valor do tipo inteiro!')
            elif isinstance(expr.index_array, expressions.FunctionCall):
                aux = expr.index_array.accept(self)
                if aux is not None:
                    if aux.data_type != 'int':
                        print(str(expr.token_name.file_line) + ': Erro Semântico: Um index de um vetor/matriz deve ser'
                                                               'um valor do tipo inteiro!')
            elif isinstance(expr.index_array, expressions.StructGet) or isinstance(expr.index_array, expressions.ConstVarAccess):
                aux = expr.index_array.accept(self)
                if aux != 'int':
                    print(str(expr.token_name.file_line) + ': Erro Semântico: Um index de um vetor/matriz deve ser'
                                                           'um valor do tipo inteiro!')
        elif not var_pos[0].value:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma variável/constante não inicializada!')
            return var_pos[0].data_type
        return None

    # TODO: VERIFICAR SE JA EXISTE OUTRO PROCEDURE COM O MESMO NOME (OVERLOADING)
    # TODO: VERIFICAR SE O RETORNO É DO MESMO TIPO QUE ESPERADO
    def visitFunctionStmt(self, stmt):
        for line in stmt.body:
            line.accept(self)

    #TODO: VERIFICAR SE JA EXISTE OUTRO PROCEDURE COM O MESMO NOME (OVERLOADING)
    def visitProcedureStmt(self, stmt):
        for line in stmt.body:
            line.accept(self)

    def visitExpressionStmt(self, stmt):
        pass

    # TODO: VERIFICAR SE A CONDIÇÂO È UM BOOLEANO
    def visitIfThenElseStmt(self, stmt):
        for item in stmt.then_branch:
            item.accept(self)
        if stmt.else_branch is not None:
            for item in stmt.else_branch:
                item.accept(self)

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
                        print(str(stmt.program_line) + ': Erro semântico: Variável do tipo ' + stmt.tp,
                              'armazenando valor de tipo:', str(type(val.value)))
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
                    print(str(stmt.program_line) + ': Erro semântico: Constante do tipo ' + stmt.tp,
                          'armazenando valor de tipo:', str(type(val.value)))
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
                print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct que não existe!')
            elif stmt.name.file_line < extends_pos[0].program_line and extends_pos[0].tp == 'struct':
                print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct ainda não definida!')
            elif extends_pos[0].tp == 'typedef':
                pass

    def visitWhileStmt(self, stmt):
        pass

    def visitTypedefStmt(self, stmt):
        if stmt.old_tp in {'int', 'string', 'real', 'boolean'}:
            return stmt.old_tp
        elif stmt.old_tp.find('.') != -1:
            aux = stmt.old_tp.split('.')
            typedef_pos = self.symbol_table.get_line(stmt.old_tp)
            if not typedef_pos:
                print(str(stmt.name.file_line) + ': Erro Semântico: Uso do typedef para redefinir tipo inexistente!')

            return aux[1]
        else:
            typedef_pos = self.symbol_table.get_line(stmt.old_tp)
            if not typedef_pos:
                print(str(stmt.name.file_line) + ': Erro Semântico: Uso do typedef para redefinir tipo inexistente!')
                

    def visitReadStmt(self, stmt):
        pass

    def visitPrePosIncDec(self, expr):
        inc_pos = self.symbol_table.get_line(expr.variable.lexeme, expr.scope)
        if not inc_pos:
            print(str(expr.variable.file_line) + ': Erro Semântico: Tentativa de Inc/Dec uma variável que não existe!')
        elif len(inc_pos) > 1:
            print(str(expr.variable.file_line) + ': Erro Semântico: Nome de identificador indexando dois '
                                                'elementos distintos!')
        elif inc_pos[0].tp != 'var':
            print(str(expr.variable.file_line) + ': Erro Semântico: Identificador informado não corresponde a uma'
                                                ' variável, e sim a uma', inc_pos[0].tp)
        elif inc_pos[0].data_type not in {'int', 'real'}:
            print(str(expr.variable.file_line) + ': Erro Semântico: Tentativa de Inc/Dec em uma variavel de tipo ',
                  inc_pos[0].data_type)
        elif len(inc_pos[0].value) == 0:
            print(str(expr.variable.file_line) + ': Erro Semântico: Tentativa de Inc/Dec uma variavel não inicializada!')
