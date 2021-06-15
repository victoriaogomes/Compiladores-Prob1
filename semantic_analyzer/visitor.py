from semantic_analyzer import expressions
from semantic_analyzer import statements


class Visitor:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def visitAssignExpr(self, expr):
        aux = expr.expr.accept(self)
        if isinstance(expr.expr, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    print(str(expr.token_operator.file_line) +
                          ': Erro Semântico: Procedures não possuem retorno para serem usados em expressões de atribuição!')
                    return None
                else:
                    aux = aux.data_type
                    if aux not in {'int', 'string', 'real', 'boolean'}:
                        aux = self.get_old_type(aux, -1)
        if isinstance(expr.token, expressions.StructGet):
            pass
        elif isinstance(expr.token, expressions.ConstVarAccess):
            if not isinstance(expr.token.token_name, expressions.StructGet) and not isinstance(expr.token.token_name, expressions.ConstVarAccess):
                var_pos = self.symbol_table.get_line(expr.token.token_name.lexeme, expr.scope)
                if not var_pos:
                    print(str(expr.token.token_name.file_line) + ': Erro Semântico: Tentativa de atribuir valor uma variável que '
                                                                 'não existe!')
                    return None
                elif var_pos[0].tp != 'var':
                    print(str(expr.token.token_name.file_line) + ': Erro Semântico: Identificador informado não corresponde a '
                                                                 'uma variável, e sim a uma', var_pos[0].tp + '!')
                    return None
                if expr.token.index_array:
                    self.check_index(expr.token.index_array, expr.token.token_name.file_line)
                if expr.token.index_matrix:
                    self.check_index(expr.token.index_matrix, expr.token.token_name.file_line)
                if var_pos[0].data_type not in {'int', 'string', 'real', 'boolean'}:
                    temp = self.get_old_type(var_pos[0].data_type, expr.scope)
                else:
                    temp = var_pos[0].data_type
                if aux != temp:
                    print(str(expr.token.token_name.file_line) + ': Erro Semântico: Tentativa de atribuir um valor',
                          aux, 'a uma variável de tipo primitivo', temp + '!')
                    return None

    def visitBinaryExpr(self, expr):
        right_side = ''
        left_side = ''
        error_left = False
        error_right = False
        if isinstance(expr.left_expr, expressions.LiteralVal):
            left_side = expr.left_expr.accept(self)
        elif isinstance(expr.left_expr, expressions.ConstVarAccess) or \
                isinstance(expr.left_expr, expressions.Binary) or \
                isinstance(expr.left_expr, expressions.StructGet) or \
                isinstance(expr.left_expr, expressions.Grouping) or \
                isinstance(expr.left_expr, expressions.Unary):
            left_side = expr.left_expr.accept(self)
        elif isinstance(expr.left_expr, expressions.FunctionCall):
            aux = expr.left_expr.accept(self)
            if aux is None:
                error_left = True
            else:
                if aux.tp == 'procedure':
                    print(str(expr.token_operator.file_line) +
                          ': Erro Semântico: Procedures não possuem retorno para serem usados em expressões!')
                    return None
                else:
                    left_side = aux.data_type
        if isinstance(expr.right_expr, expressions.LiteralVal):
            right_side = expr.right_expr.accept(self)
        elif isinstance(expr.right_expr, expressions.ConstVarAccess) or \
                isinstance(expr.right_expr, expressions.Binary) or \
                isinstance(expr.right_expr, expressions.StructGet) or \
                isinstance(expr.right_expr, expressions.Grouping) or \
                isinstance(expr.right_expr, expressions.Unary):
            right_side = expr.right_expr.accept(self)
        elif isinstance(expr.right_expr, expressions.FunctionCall):
            aux = expr.right_expr.accept(self)
            if aux is None:
                error_right = True
            else:
                if aux.tp == 'procedure':
                    print(str(expr.token_operator.file_line) +
                          ': Erro Semântico: Procedures não possuem retorno para serem usados em expressões!')
                    return None
                else:
                    right_side = aux.data_type
        if not error_right and not error_left:
            if left_side == right_side:
                if left_side == 'int':
                    if expr.token_operator.lexeme == '/':
                        print(str(expr.token_operator.file_line) +
                              ': Erro Semântico: Operações de divisão só são permitidas com tipos reais!')
                elif left_side == 'string':
                    if expr.token_operator.lexeme in {'/', '*'}:
                        print(str(expr.token_operator.file_line) +
                              ': Erro Semântico: O tipo string não pode ser utilizado com operações aritméticas'
                              ' do tipo divisão e multiplicação!')
                elif left_side == 'boolean':
                    if expr.token_operator.lexeme in {'>', '>=', '<', '<=', '+', '-', '*', '/'}:
                        print(str(expr.token_operator.file_line) +
                              ': Erro Semântico: Os operadores informados não podem ser utilizados com tipos booleanos!')
                if expr.token_operator.lexeme in {'>', '>=', '<', '<=', '==', '!='}:
                    return 'boolean'
                else:
                    return left_side
            elif left_side is not None and right_side is not None:
                print(str(expr.token_operator.file_line) +
                      ': Erro Semântico: Operações devem ser realizadas com tipo iguais!')
        return None

    def visitFCallExpr(self, expr):
        func_pos = self.symbol_table.get_line(expr.func_exp.lexeme, -1)
        aux = []
        if not func_pos:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: Tentativa de acessar uma function/procedure que não existe!')
            return None
        elif len(func_pos) > 1:
            aux = self.check_overloading(func_pos, expr.func_exp.file_line, 'Chamada')
            return None
        elif func_pos[0].tp not in {'function', 'procedure'}:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: O identificador não corresponde a uma function ou procedure!')
            return None
        elif not expr.func_exp.file_line >= func_pos[0].program_line:
            print(str(expr.func_exp.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma function/procedure ainda não definido!')
            return None
        if aux is not None:
            base = []
            if expr.arguments is not None:
                for item in expr.arguments:
                    base.append(item.accept(self))

            if len(aux) == 0:
                for item in func_pos[0].params:
                    aux.append(item.split('.')[0])
                if set(base) != set(aux):
                    print(str(expr.func_exp.file_line) +
                          ': Erro Semântico: Chamada de função usando parâmetros de tipo incorreto!')
            else:
                params_okay = False
                for item in aux:
                    if set(item) == set(aux):
                        params_okay = True
                if not params_okay:
                    print(str(expr.func_exp.file_line) +
                          ': Erro Semântico: Chamada de função usando parâmetros de tipo incorreto!')
        return func_pos[0]

    def visitStructGetExpr(self, expr):
        if expr.struct_name.access_type == 'global':
            expr.struct_name.scope = -1
        else:
            expr.struct_name.scope = expr.scope
        struct_pos = self.symbol_table.get_line(expr.struct_name.token_name.lexeme, expr.struct_name.scope)
        old_tp = ''
        line = ''
        line2 = ''
        if not struct_pos:
            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Acesso a variavel do tipo struct inexistente!')
            return None
        elif len(struct_pos) > 1:
            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador', expr.struct_name.token_name.lexeme,
                  'indexa mais de um elemento!')
            return None
        elif struct_pos[0].data_type.find('struct') == -1:
            if struct_pos[0].data_type not in {'int', 'string', 'boolean', 'real'}:
                old_tp = self.get_old_type(struct_pos[0].data_type, expr.struct_name.scope)
                if old_tp is not None:
                    if old_tp in {'int', 'string', 'real', 'boolean'}:
                        print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: O identificador',
                              expr.struct_name.token_name.lexeme + ' não se refere a uma struct!')
                        return None
                    else:
                        line = self.symbol_table.get_line(old_tp, expr.struct_name.scope)
                        if expr.struct_name.scope != -1:
                            line2 = self.symbol_table.get_line(old_tp, -1)
                            if line:
                                if line[0].tp != 'struct':
                                    if not line2:
                                        print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: O identificador',
                                              expr.struct_name.token_name.lexeme + ' não se refere a uma struct!')
                                        return None
                            if line2:
                                if line2[0].tp != 'struct':
                                    if not line:
                                        print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: O identificador',
                                              expr.struct_name.token_name.lexeme + ' não se refere a uma struct!')
                                        return None
                            if not line and not line2:
                                print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Struct de tipo inexistente!')
                                return None
                        else:
                            if line[0].tp != 'struct':
                                print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: O identificador',
                                      expr.struct_name.token_name.lexeme + ' não se refere a uma struct!')
                                return None
            else:
                print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador', expr.struct_name.token_name.lexeme,
                      'não indexa uma struct!')
                return None
        elif not expr.struct_name.token_name.file_line >= struct_pos[0].program_line:
            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Tentativa de acesso a uma variável do tipo struct ainda não declarada!')
            return None
        if isinstance(expr.att_name, expressions.ConstVarAccess):
            if line2 == '' and line == '':
                tp_name = struct_pos[0].data_type.split('.')[1]
                tp_pos = self.symbol_table.get_line(tp_name, expr.struct_name.scope)
                attr_ok = self.check_attr(tp_pos, expr.struct_name.token_name.file_line, expr.attr_name.token_name.lexeme)
                if expr.struct_name.scope != -1 and (attr_ok is None or not attr_ok):
                    tp_pos2 = self.symbol_table.get_line(tp_name, -1)
                    attr_ok = self.check_attr(tp_pos2, expr.struct_name.token_name.file_line, expr.attr_name.token_name.lexeme)
                if attr_ok is None:
                    print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador',
                          expr.attr_name.token_name.lexeme, 'indexa um tipo de struct indefinido!')
                elif not attr_ok:
                    print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador',
                          expr.attr_name.token_name.lexeme, 'indexa uma variavel inexistente no tipo de struct', expr.struct_name.token_name.lexeme + '!')
            else:
                if line:
                    attr_ok = self.check_attr(line, expr.struct_name.token_name.file_line, expr.struct_name.token_name.lexeme)
                    if attr_ok is None:
                        if not line2:
                            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador',
                                  expr.attr_name.token_name.lexeme, 'indexa um tipo de struct indefinido!')
                    elif not attr_ok:
                        if not line2:
                            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador',
                                  expr.attr_name.token_name.lexeme, 'indexa uma variavel inexistente no tipo de struct', expr.struct_name.token_name.lexeme + '!')
                if line2:
                    attr_ok = self.check_attr(line2, expr.struct_name.token_name.file_line, expr.struct_name.token_name.lexeme)
                    if attr_ok is None:
                        if not line:
                            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador',
                                  expr.attr_name.token_name.lexeme, 'indexa um tipo de struct indefinido!')
                    elif not attr_ok:
                        if not line:
                            print(str(expr.struct_name.token_name.file_line) + ': Erro Semântico: Identificador',
                                  expr.attr_name.token_name.lexeme, 'indexa uma variavel inexistente no tipo de struct', expr.struct_name.token_name.lexeme + '!')


    def visitGroupingExpr(self, expr):
        return expr.expr.accept(self)

    def visitLitValExpr(self, expr):
        aux = str(type(expr.value))
        aux = aux.split('\'')[1]
        if aux == 'float':
            aux = 'real'
        elif aux == 'str':
            aux = 'string'
        elif aux == 'bool':
            aux = 'boolean'
        return aux

    def visitLogicalExpr(self, expr):
        pass

    def visitUnaryExpr(self, expr):
        aux = expr.right_expr.accept(self)
        if isinstance(expr.right_expr, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    print(str(expr.token_operator.file_line) +
                          ': Erro Semântico: Procedures não possuem retorno para serem usados em expressões!')
                    return None
                else:
                    aux = aux.data_type
        if expr.token_operator.lexeme == '!':
            if aux is not None:
                if aux != 'boolean':
                    print(str(expr.token_operator.file_line) +
                          ': Erro Semântico: O operador ! só pode ser usado antes de elementos do tipo booleano!')
                    return None
                else:
                    return aux
        elif expr.token_operator.lexeme == '-':
            if aux is not None:
                if aux not in {'real', 'int'}:
                    print(str(expr.token_operator.file_line) +
                          ': Erro Semântico: O operador - só pode ser usado antes de elementos do tipo real ou inteiro!')
                    return None
                else:
                    return aux
        return None

    def visitConstVarAccessExpr(self, expr):
        if expr.access_type == 'global':
            expr.scope = -1
        var_pos = self.symbol_table.get_line(expr.token_name.lexeme, expr.scope)
        if not var_pos:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acessar uma variável/constante que não existe!')
            return None
        elif len(var_pos) > 1:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Nome de idenficador indexa duas variáveis distintas')
            return None
        elif var_pos[0].tp not in {'var', 'const'}:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: O identificador não corresponde a uma variavel ou constante!')
            return None
        elif not expr.token_name.file_line >= var_pos[0].program_line:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma variavel/constante ainda não declarada!')
        elif not var_pos[0].value:
            print(str(expr.token_name.file_line) +
                  ': Erro Semântico: Tentativa de acesso a uma variável/constante não inicializada!')
        if expr.index_array:
            self.check_index(expr.index_array, expr.token_name.file_line)
        if expr.index_matrix:
            self.check_index(expr.index_matrix, expr.token_name.file_line)
        aux = var_pos[0].data_type
        if var_pos[0].data_type not in {'int', 'real', 'boolean', 'string'}:
            aux = self.get_old_type(var_pos[0].data_type, expr.scope)
        return aux

    def visitFunctionStmt(self, stmt):
        func_pos = self.symbol_table.get_line(stmt.token_name.lexeme, -1)
        if len(func_pos) > 1:
            self.check_overloading(func_pos, stmt.token_name.file_line, 'Declaração')
        for line in stmt.body:
            line.accept(self)
        tp = stmt.return_expr.accept(self)
        if tp is not None:
            if tp != stmt.return_tp.lexeme:
                print(str(stmt.return_expr.keyword.file_line) +
                      ': Erro Semântico: O tipo de retorno não bate com o esperado! Esperava:', stmt.return_tp.lexeme
                      + ', recebi:', tp)

    def visitProcedureStmt(self, stmt):
        proc_pos = self.symbol_table.get_line(stmt.token_name.lexeme, -1)
        if len(proc_pos) > 1:
            self.check_overloading(proc_pos, stmt.token_name.file_line, 'Declaração')
        for line in stmt.body:
            line.accept(self)

    def visitExpressionStmt(self, stmt):
        pass

    def visitIfThenElseStmt(self, stmt):
        for item in stmt.then_branch:
            item.accept(self)
        if stmt.else_branch is not None:
            for item in stmt.else_branch:
                item.accept(self)
        aux = stmt.cond_expr.accept(self)
        if isinstance(stmt.cond_expr, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    print(str(stmt.program_line) +
                          ': Erro Semântico: Procedures não possuem retorno para serem usados em expressões!')
                else:
                    aux = aux.data_type
        if aux is not None:
            if aux != 'boolean':
                print(str(stmt.program_line) +
                      ': Erro Semântico: Condição de um if deve resultar em um booleano!')

    def visitPrintfStmt(self, stmt):
        for item in stmt.expression:
            if isinstance(item, expressions.FunctionCall):
                func_pos = self.symbol_table.get_line(item.func_exp.lexeme, -1)
                if not func_pos:
                    print(str(stmt.program_line) + ': Erro semântico: Chamada a função inexistente!')
                elif func_pos[0].data_type == '':
                    print(str(stmt.program_line) + ': Erro semântico: Não é possível passar '
                                                   'procedimentos como argumento de prints, pois os mesmos'
                                                   ' não retornam nada!')
            else:
                item.accept(self)

    def visitReturnfStmt(self, stmt):
        return stmt.value.accept(self)

    def visitVarStmt(self, stmt):
        var_pos = self.symbol_table.get_line(stmt.name, stmt.scope)
        if len(var_pos) > 1:
            if not var_pos[0].program_line >= stmt.program_line:
                print(str(stmt.program_line) +
                      ': Erro semântico: Já existe outro elemento indexado com esse identificador!')
        # Verifica se o tipo dessa variável realmente existe
        aux = stmt.tp
        if stmt.tp not in {'string', 'int', 'real', 'boolean'}:
            if stmt.tp.find('.') != -1:
                temp = stmt.tp.split('.')
                aux = temp[1]
            else:
                aux = self.get_old_type(stmt.tp, stmt.scope)
        if aux:
            # Verifica se o valor armazenado nessa variável é compatível com seu tipo
            if stmt.init_val is not None:
                for val in stmt.init_val:
                    if isinstance(val, expressions.LiteralVal):
                        if not ((type(val.value) is str and aux == 'string') or
                                (type(val.value) is int and aux == 'int') or
                                (type(val.value) is float and aux == 'real') or
                                (type(val.value) is bool and aux == 'boolean')):
                            print(str(stmt.program_line) + ': Erro semântico: Variável do tipo ' + aux,
                                  'armazenando valor de tipo:', str(type(val.value)))
                    else:
                        # Caso o valor inicial seja uma expressão
                        val.accept(self)
        else:
            print(str(stmt.program_line) + ': Erro semântico: Variável de tipo inexistente!')
        if stmt.index_array is not None:
            self.check_index(stmt.index_array, stmt.program_line)
        if stmt.index_matrix is not None:
            self.check_index(stmt.index_matrix, stmt.program_line)

    def visitVarBlockStmt(self, stmt):
        for var in stmt.var_list:
            var.accept(self)

    def visitConstStmt(self, stmt):
        const_pos = self.symbol_table.get_line(stmt.name, stmt.scope)
        if len(const_pos) > 1:
            if not const_pos[0].program_line >= stmt.program_line:
                print(str(stmt.program_line) +
                      ': Erro semântico: Já existe outro elemento indexado com esse identificador!')
        aux = stmt.tp
        if stmt.tp not in {'string', 'int', 'real', 'boolean'}:
            if stmt.tp.find('.') != -1:
                temp = stmt.tp.split('.')
                aux = temp[1]
            else:
                aux = self.get_old_type(stmt.tp, stmt.scope)
        if aux:
            # Verifica se o valor armazenado nessa variável é compatível com seu tipo
            if stmt.init_val is not None:
                for val in stmt.init_val:
                    if isinstance(val, expressions.LiteralVal):
                        if not ((type(val.value) is str and aux == 'string') or
                                (type(val.value) is int and aux == 'int') or
                                (type(val.value) is float and aux == 'real') or
                                (type(val.value) is bool and aux == 'boolean')):
                            print(str(stmt.program_line) + ': Erro semântico: Variável do tipo ' + aux,
                                  'armazenando valor de tipo:', str(type(val.value)))
                    else:
                        # Caso o valor inicial seja uma expressão
                        val.accept(self)
        else:
            print(str(stmt.program_line) + ': Erro semântico: Variável de tipo inexistente!')
        if stmt.index_array is not None:
            self.check_index(stmt.index_array, stmt.program_line)
        if stmt.index_matrix is not None:
            self.check_index(stmt.index_matrix, stmt.program_line)

    def visitConstBlockStmt(self, stmt):
        for const in stmt.const_list:
            const.accept(self)

    def visitStructStmt(self, stmt):
        struct_pos = self.symbol_table.get_line(stmt.name.lexeme, stmt.scope)
        if len(struct_pos) > 1 and stmt.name.file_line != struct_pos[0].program_line:
            print(str(stmt.name.file_line) + ': Erro Semântico: Identificador', stmt.name.lexeme, 'está sendo utilizado para indexar mais de um elemento!')
        if stmt.extends is not None:
            extends_pos = self.symbol_table.get_line(stmt.extends.lexeme, stmt.scope)
            if not extends_pos:
                print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct que não existe!')
            elif len(extends_pos) > 1:
                print(str(stmt.name.file_line) +
                      ': Erro Semântico: Struct extendendo outro elemento usando um identificador que indexa mais de um elemento!')
            elif stmt.name.file_line < extends_pos[0].program_line and extends_pos[0].tp == 'struct':
                print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct ainda não definida!')
            elif extends_pos[0].tp not in {'struct', 'typedef'}:
                print(str(stmt.name.file_line) + ': Erro Semântico: Struct não pode extender do tipo:', extends_pos[0].tp + '!')
            elif extends_pos[0].tp == 'typedef':
                if stmt.name.file_line < extends_pos[0].program_line:
                    print(str(stmt.name.file_line) + ': Erro Semântico: Struct extendendo tipo ainda não definido!')
                    return
                old_tp = self.get_old_type(extends_pos[0].name, stmt.scope)
                if old_tp is not None:
                    if old_tp in {'int', 'string', 'real', 'boolean'}:
                        print(str(stmt.name.file_line) + ': Erro Semântico: Struct não pode extender do tipo:', old_tp + '!')
                    else:
                        line = self.symbol_table.get_line(old_tp, stmt.scope)
                        if stmt.scope != -1:
                            line2 = self.symbol_table.get_line(old_tp, -1)
                            if line:
                                if line[0].tp != 'struct':
                                    if not line2:
                                        print(str(stmt.name.file_line) + ': Erro Semântico: Struct não pode extender do tipo:', old_tp + '!')
                                elif stmt.name.file_line < line[0].program_line:
                                    print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct ainda não definida!')
                            if line2:
                                if line2[0].tp != 'struct':
                                    if not line:
                                        print(str(stmt.name.file_line) + ': Erro Semântico: Struct não pode extender do tipo:', old_tp + '!')
                                elif stmt.name.file_line < line2[0].program_line:
                                    print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct ainda não definida!')
                            if not line and not line2:
                                print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo um elemento inexistente!')
                        else:
                            if line[0].tp != 'struct':
                                print(str(stmt.name.file_line) + ': Erro Semântico: Struct não pode extender do tipo:', old_tp + '!')
                            elif stmt.name.file_line < line[0].program_line:
                                print(str(stmt.name.file_line) + ': Erro Semântico: Struct está extendendo uma Struct ainda não definida!')

    def visitWhileStmt(self, stmt):
        aux = stmt.condition.accept(self)
        if isinstance(stmt.condition, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    print(str(stmt.program_line) +
                          ': Erro Semântico: Procedures não possuem retorno para serem usados em expressões!')
                else:
                    aux = aux.data_type
        if aux is not None:
            if aux != 'boolean':
                print(str(stmt.program_line) +
                      ': Erro Semântico: Condição de um while deve resultar em um booleano!')
        for item in stmt.body:
            item.accept(self)

    def visitTypedefStmt(self, stmt):
        aux = stmt.old_tp
        if aux in {'int', 'string', 'real', 'boolean'}:
            return aux
        elif aux.find('.') != -1:
            aux = aux.split('.')[1]
        if stmt.scope != -1:
            typedef_pos = self.symbol_table.get_line(aux, stmt.scope)
            name_pos2 = self.symbol_table.get_line(aux, -1)
            if not typedef_pos and not name_pos2:
                print(str(stmt.tp_name.file_line) + ': Erro Semântico: Uso do typedef para redefinir tipo inexistente!')
            else:
                if typedef_pos and name_pos2:
                    print(str(stmt.tp_name.file_line) + ': Erro Semântico: Uso do typedef idêntico em mais de um local!')
            new_type_pos = self.symbol_table.get_line(stmt.tp_name.lexeme, stmt.scope)
            new_type_pos2 = self.symbol_table.get_line(stmt.tp_name.lexeme, -1)
            if new_type_pos is not None and new_type_pos2 is not None:
                print(str(stmt.tp_name.file_line) + ': Erro Semântico: Já existem outros elementos indexados com esse identificador: '
                      + stmt.tp_name.lexeme + '!')
            else:
                if new_type_pos is not None and len(new_type_pos) > 1 and \
                        stmt.tp_name.file_line > new_type_pos[0].program_line:
                    print(str(stmt.tp_name.file_line) + ': Erro Semântico: Já existem outros elementos indexados com esse identificador:'
                          + stmt.tp_name.lexeme + '!')
                elif new_type_pos2 is not None and len(new_type_pos2) > 1 and \
                        stmt.tp_name.file_line > new_type_pos2[0].program_line:
                    print(str(stmt.tp_name.file_line) + ': Erro Semântico: Já existem outros elementos indexados com esse identificador:'
                          + stmt.tp_name.lexeme + '!')
        else:
            typedef_pos = self.symbol_table.get_line(aux, stmt.scope)
            if not typedef_pos:
                print(str(stmt.tp_name.file_line) + ': Erro Semântico: Uso do typedef para redefinir tipo inexistente!')
            new_type_pos = self.symbol_table.get_line(stmt.tp_name.lexeme, stmt.scope)
            if new_type_pos is not None:
                if len(new_type_pos) > 1 and \
                        stmt.tp_name.file_line > new_type_pos[0].program_line:
                    print(str(stmt.tp_name.file_line) + ': Erro Semântico: Já existem outros elementos indexados com esse identificador: '
                          + stmt.tp_name.lexeme + '!')

    def visitReadStmt(self, stmt):
        pass

    def visitPrePosIncDec(self, expr):
        if isinstance(expr.variable, expressions.StructGet):
            pass
        elif isinstance(expr.variable, expressions.ConstVarAccess):
            inc_pos = self.symbol_table.get_line(expr.variable.lexeme, expr.scope)
            if not inc_pos:
                print(str(expr.variable.file_line) + ': Erro Semântico: Tentativa de Inc/Dec uma variável que não existe!')
            elif len(inc_pos) > 1:
                print(str(expr.variable.file_line) + ': Erro Semântico: Nome de identificador indexando dois '
                                                     'elementos distintos!')
            elif inc_pos[0].tp != 'var':
                print(str(expr.variable.file_line) + ': Erro Semântico: Identificador informado não corresponde a uma'
                                                     ' variável, e sim a uma', inc_pos[0].tp + '!')
            elif inc_pos[0].data_type not in {'int', 'real'}:
                aux = inc_pos[0].data_type
                if inc_pos[0].data_type not in {'string', 'boolean'}:
                    aux = self.get_old_type(inc_pos[0].data_type, expr.scope)
                    if aux and aux in {'int', 'real'}:
                        return
                print(str(expr.variable.file_line) + ': Erro Semântico: Tentativa de Inc/Dec em uma variavel de tipo primitivo',
                      aux + '!')
            elif len(inc_pos[0].value) == 0:
                print(str(expr.variable.file_line) + ': Erro Semântico: Tentativa de Inc/Dec uma variavel não inicializada!')

    def get_old_type(self, name, scope):
        name_pos1 = self.symbol_table.get_line(name, scope)
        if scope != -1:
            name_pos2 = self.symbol_table.get_line(name, -1)
            if name_pos1 and name_pos2:
                return None
            elif name_pos1 and len(name_pos1) == 1:
                return self.check_pos(name_pos1[0], scope)
            elif name_pos2 and len(name_pos2) == 1:
                return self.check_pos(name_pos2[0], -1)
        elif name_pos1 and len(name_pos1) == 1:
            return self.check_pos(name_pos1[0], scope)
        return None

    def check_pos(self, name_pos, scope):
        if name_pos:
            if name_pos.tp == 'typedef':
                if name_pos.data_type in {'int', 'string', 'real', 'boolean'}:
                    return name_pos.data_type
                elif name_pos.data_type.find('.') != -1:
                    aux = name_pos.data_type.split('.')
                    return aux[1]
                else:
                    return self.get_old_type(name_pos.data_type, scope)
        return None  # O identificador passado não corresponde a um tipo válido

    # Um método para checar se o index de um vetor ou matriz é um inteiro
    def check_index(self, index, file_line):
        if isinstance(index, expressions.LiteralVal):
            aux = index.accept(self)
            if aux == 'int':
                return
        elif isinstance(index, expressions.FunctionCall):
            aux = index.accept(self)
            if aux is not None:
                if aux.data_type == 'int':
                    return
        elif isinstance(index, expressions.StructGet) or isinstance(index, expressions.ConstVarAccess):
            aux = index.accept(self)
            if aux == 'int':
                return
        elif isinstance(index, expressions.Binary):
            aux = index.accept(self)
            if aux == 'int':
                return
        print(str(file_line) + ': Erro Semântico: Um index de um vetor/matriz deve ser'
                               ' um valor do tipo inteiro!')

    def check_overloading(self, func_pos, file_line, tp):
        all_func = True
        for item in func_pos:
            if item.tp not in {'function', 'procedure'}:
                all_func = False
        if not all_func:
            print(str(file_line) + ': Erro Semântico: Nome de idenficador indexa dois elementos distintos!')
        else:
            base = []
            all_args = []
            all_eq = False
            for item in func_pos[0].params:
                base.append(item.split('.')[0])
            all_args.append(base)
            for item in func_pos[1:]:
                actual = []
                for sub_item in item.params:
                    actual.append(sub_item.split('.')[0])
                all_args.append(actual)
                if set(base) == set(actual):
                    all_eq = True
            if all_eq:
                if file_line > func_pos[0].program_line or tp == 'Chamada':
                    print(str(file_line) + ': Erro Semântico: ' + tp + ' de Função/Procedure duplicada -> Possível sobrecarga usada de forma errada!')
                    return None
                return all_args
        return None

    def check_attr(self, tp_pos, file_line, lexeme):
        attr_ok = False
        if tp_pos:
            for param in tp_pos[0].params:
                if param.split('.')[1] == lexeme:
                    attr_ok = True
        else:
            return None
        return attr_ok