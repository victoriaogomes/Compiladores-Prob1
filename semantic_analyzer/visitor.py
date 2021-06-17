from semantic_analyzer import expressions


class Visitor:
    def __init__(self, symbol_table, tokens_list):
        self.symbol_table = symbol_table
        self.tokens_list = tokens_list

    def visitAssignExpr(self, expr):
        file_line = 0
        token_name = ''
        aux = expr.expr.accept(self)
        if isinstance(expr.expr, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    self.add_error(str(expr.token_operator.file_line) + ':Erro Semantico: ' + expr.expr.func_exp.lexeme + ' é uma procedure.'
                                                                                                                          ' Procedures nao possuem retorno para serem usados em '
                                                                                                                          'expressões de atribuiçao!')
                    return None
                else:
                    aux = aux.data_type
                    if aux not in {'int', 'string', 'real', 'boolean'}:
                        if aux.find('struct') != -1:
                            aux = aux.split('.')[1]
                        else:
                            aux = self.get_old_type(aux, -1)
        if isinstance(expr.token, expressions.ConstVarAccess):
            file_line = expr.token.token_name.file_line
            token_name = expr.token.token_name.lexeme
            if expr.token.access_type == 'global':
                expr.token.scope = -1
            var_pos = self.symbol_table.get_line(expr.token.token_name.lexeme, expr.token.scope)
            if var_pos and var_pos[0].tp == 'const':
                self.add_error(str(expr.token.token_name.file_line) + ':Erro Semantico:' + expr.token.token_name.lexeme + ' eh uma constante. O valor armazenado em uma constante nao pode ser '
                                                                                                                          'alterado!')
        elif isinstance(expr.token, expressions.StructGet):
            file_line = expr.token.struct_name.token_name.file_line
            token_name = expr.token.struct_name.token_name.lexeme
        temp = expr.token.accept(self)
        if temp is not None and aux is not None and aux != temp:
            self.add_error(str(file_line) + ':Erro Semantico:Tentativa de atribuir um valor ' +
                           aux + ' a variavel \'' + token_name + '\', que e do tipo primitivo ' + temp + '!')
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
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:' + aux.name + 'eh um procedure. Procedures nao possuem retorno para serem usados em expressões!')
                    return None
                else:
                    left_side = aux.data_type
        else:
            self.add_error(str(expr.token_operator.file_line) +
                           ':Erro Semantico:Elemento de tipo nao permitido em expressao!')
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
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:' + aux.name + 'eh um procedure. Procedures nao possuem retorno para serem usados em expressões!')
                    return None
                else:
                    right_side = aux.data_type
        else:
            self.add_error(str(expr.token_operator.file_line) +
                           ':Erro Semantico:Elemento de tipo nao permitido em expressao!')
        if not error_right and not error_left:
            if left_side == right_side:
                if left_side == 'int':
                    if expr.token_operator.lexeme == '/':
                        self.add_error(str(expr.token_operator.file_line) +
                                       ':Erro Semantico:Operações de divisao só sao permitidas com tipos reais! Recebi uma operação com ' + left_side + ' e ' + right_side)
                elif left_side == 'string':
                    if expr.token_operator.lexeme in {'/', '*'}:
                        self.add_error(str(expr.token_operator.file_line) +
                                       ':Erro Semantico:O tipo string nao pode ser utilizado com operações aritmeticas'
                                       ' do tipo divisao e multiplicaçao!')
                elif left_side == 'boolean':
                    if expr.token_operator.lexeme in {'>', '>=', '<', '<=', '+', '-', '*', '/'}:
                        self.add_error(str(expr.token_operator.file_line) +
                                       ':Erro Semantico:Os operadores informados nao podem ser utilizados com tipos booleanos!')
                if expr.token_operator.lexeme in {'>', '>=', '<', '<=', '==', '!='}:
                    return 'boolean'
                else:
                    return left_side
            elif left_side is not None and right_side is not None:
                self.add_error(str(expr.token_operator.file_line) +
                               ':Erro Semantico:Operações devem ser realizadas com tipo iguais! Recebi elementos do tipo ' + left_side + ' e ' + right_side)
        return None

    def visitFCallExpr(self, expr):
        func_pos = self.symbol_table.get_line(expr.func_exp.lexeme, -1)
        aux = []
        f_index = 0
        if not func_pos:
            self.add_error(str(expr.func_exp.file_line) +
                           ':Erro Semantico:Chamada a function/procedure \'' + expr.func_exp.lexeme + '\', o qual nao existe!')
            return None
        elif len(func_pos) > 1:
            aux = self.check_overloading(func_pos, expr.func_exp.file_line, 'Chamada')
            if aux is None:
                return None
        elif func_pos[0].tp not in {'function', 'procedure'}:
            self.add_error(str(expr.func_exp.file_line) +
                           ':Erro Semantico:O identificador ' + expr.func_exp.lexeme + ' nao corresponde a uma function ou procedure!')
            return None
        elif not expr.func_exp.file_line >= func_pos[0].program_line:
            self.add_error(str(expr.func_exp.file_line) +
                           ':Erro Semantico:Tentativa de acesso a ' + expr.func_exp.lexeme + ' , que é uma function/procedure ainda nao definida(o)!')
            return None
        base = []
        if expr.arguments is not None:
            for item in expr.arguments:
                base.append(item.accept(self))
        if len(aux) == 0 and len(base) > 0 and base[0] is not None:
            for item in func_pos[0].params:
                aux.append(item.split('.')[0])
            if set(base) != set(aux):
                self.add_error(str(expr.func_exp.file_line) +
                               ':Erro Semantico:Chamada a funçao/procedure \'' + expr.func_exp.lexeme + '\' usando parametros de tipo incorreto! Esperava ' + ','.join(
                    aux) + ', e recebi ' + ','.join(base))
                return None
        else:
            params_okay = False
            if len(aux) == 0 and len(base) == 0:
                params_okay = True
            else:
                for i in range(0, len(aux)):
                    if set(aux[i]) == set(base):
                        params_okay = True
                        f_index = i
            if not params_okay:
                self.add_error(str(expr.func_exp.file_line) +
                               ':Erro Semantico:Chamada a funçao/procedure \'' + expr.func_exp.lexeme + '\' usando parametros de tipo incorreto!')
                return None
        return func_pos[f_index]

    def visitStructGetExpr(self, expr):
        if expr.struct_name.access_type == 'global':
            expr.struct_name.scope = -1
        else:
            expr.struct_name.scope = expr.scope
        struct_pos = self.symbol_table.get_line(expr.struct_name.token_name.lexeme, expr.struct_name.scope)
        attr_ok = None
        line = ''
        line2 = ''
        if not struct_pos:
            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Acesso a variavel do tipo struct inexistente!')
            return None
        elif len(struct_pos) > 1:
            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' + expr.struct_name.token_name.lexeme +
                           ' indexa mais de um elemento!')
            return None
        elif struct_pos[0].data_type.find('struct') == -1:
            if struct_pos[0].data_type not in {'int', 'string', 'boolean', 'real'}:
                old_tp = self.get_old_type(struct_pos[0].data_type, expr.struct_name.scope)
                if old_tp is not None:
                    if old_tp in {'int', 'string', 'real', 'boolean'}:
                        self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:O identificador ' +
                                       expr.struct_name.token_name.lexeme + ' nao se refere a uma struct!')
                        return None
                    else:
                        line = self.symbol_table.get_line(old_tp, expr.struct_name.scope)
                        if expr.struct_name.scope != -1:
                            line2 = self.symbol_table.get_line(old_tp, -1)
                            if line:
                                if line[0].tp != 'struct':
                                    if not line2:
                                        self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:O identificador ' +
                                                       expr.struct_name.token_name.lexeme + ' nao se refere a uma struct!')
                                        return None
                            if line2:
                                if line2[0].tp != 'struct':
                                    if not line:
                                        self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:O identificador ' +
                                                       expr.struct_name.token_name.lexeme + ' nao se refere a uma struct!')
                                        return None
                            if not line and not line2:
                                self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Struct de tipo inexistente!')
                                return None
                        else:
                            if not line:
                                self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Struct de tipo inexistente!')
                                return None
                            elif line[0].tp != 'struct':
                                self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:O identificador ' +
                                               expr.struct_name.token_name.lexeme + ' nao se refere a uma struct!')
                                return None
            else:
                self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' + expr.struct_name.token_name.lexeme +
                               ' nao indexa uma struct!')
                return None
        elif not expr.struct_name.token_name.file_line >= struct_pos[0].program_line:
            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Tentativa de acesso a uma variavel do tipo struct ainda nao declarada!')
            return None
        if isinstance(expr.attr_name, expressions.ConstVarAccess):
            if line2 == '' and line == '':
                tp_name = struct_pos[0].data_type.split('.')[1]
                tp_pos = self.symbol_table.get_line(tp_name, expr.struct_name.scope)
                attr_ok = self.check_attr(tp_pos, expr.attr_name.token_name.lexeme)
                if expr.struct_name.scope != -1 and (attr_ok is None or not attr_ok):
                    tp_pos2 = self.symbol_table.get_line(tp_name, -1)
                    attr_ok = self.check_attr(tp_pos2, expr.attr_name.token_name.lexeme)
                if attr_ok is None:
                    self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' +
                                   expr.attr_name.token_name.lexeme + ' indexa um elemento em um tipo de struct indefinido!')
                    return None
                elif not attr_ok:
                    self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' +
                                   expr.attr_name.token_name.lexeme + 'indexa uma variavel inexistente no tipo de struct de' + expr.struct_name.token_name.lexeme + '!')
                    return None
                if expr.attr_name.index_array:
                    self.check_index(expr.attr_name.index_array, expr.attr_name.token_name.file_line)
                if expr.attr_name.index_matrix:
                    self.check_index(expr.attr_name.index_matrix, expr.attr_name.token_name.file_line)
            else:
                if line:
                    attr_ok = self.check_attr(line, expr.attr_name.token_name.lexeme)
                    if attr_ok is None:
                        if not line2:
                            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' +
                                           expr.attr_name.token_name.lexeme + ' indexa um elemento em um tipo de struct indefinido!')
                            return None
                    elif not attr_ok:
                        if not line2:
                            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' +
                                           expr.attr_name.token_name.lexeme + ' indexa uma variavel inexistente no tipo de struct de ' + expr.struct_name.token_name.lexeme + '!')
                            return None
                if line2:
                    attr_ok = self.check_attr(line2, expr.attr_name.token_name.lexeme)
                    if attr_ok is None:
                        if not line:
                            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' +
                                           expr.attr_name.token_name.lexeme + ' indexa um elemento em um tipo de struct indefinido!')
                            return None
                    elif not attr_ok:
                        if not line:
                            self.add_error(str(expr.struct_name.token_name.file_line) + ':Erro Semantico:Identificador ' +
                                           expr.attr_name.token_name.lexeme + ' indexa uma variavel inexistente no tipo de struct de ' + expr.struct_name.token_name.lexeme + '!')
                            return None
        elif isinstance(expr.attr_name, expressions.StructGet):
            return expr.attr_name.accept(self)
        return attr_ok

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
        right_side = ''
        left_side = ''
        error_left = False
        error_right = False
        if isinstance(expr.left_expr, expressions.LiteralVal) or \
                isinstance(expr.left_expr, expressions.ConstVarAccess) or \
                isinstance(expr.left_expr, expressions.Binary) or \
                isinstance(expr.left_expr, expressions.StructGet) or \
                isinstance(expr.left_expr, expressions.Grouping) or \
                isinstance(expr.left_expr, expressions.Unary) or \
                isinstance(expr.left_expr, expressions.Logical):
            left_side = expr.left_expr.accept(self)
        elif isinstance(expr.left_expr, expressions.FunctionCall):
            aux = expr.left_expr.accept(self)
            if aux is None:
                error_left = True
            else:
                if aux.tp == 'procedure':
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:Procedures nao possuem retorno para serem usados em expressões!')
                    return None
                else:
                    left_side = aux.data_type
        else:
            self.add_error(str(expr.token_operator.file_line) +
                           ':Erro Semantico:Elemento de tipo nao permitido em expressao!')
        if isinstance(expr.right_expr, expressions.LiteralVal) or \
                isinstance(expr.right_expr, expressions.ConstVarAccess) or \
                isinstance(expr.right_expr, expressions.Binary) or \
                isinstance(expr.right_expr, expressions.StructGet) or \
                isinstance(expr.right_expr, expressions.Grouping) or \
                isinstance(expr.right_expr, expressions.Unary) or \
                isinstance(expr.right_expr, expressions.Logical):
            right_side = expr.right_expr.accept(self)
        elif isinstance(expr.right_expr, expressions.FunctionCall):
            aux = expr.right_expr.accept(self)
            if aux is None:
                error_right = True
            else:
                if aux.tp == 'procedure':
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:Procedures nao possuem retorno para serem usados em expressões!')
                    return None
                else:
                    right_side = aux.data_type
        else:
            self.add_error(str(expr.token_operator.file_line) +
                           ':Erro Semantico:Elemento de tipo nao permitido em expressao!')
        if not error_right and not error_left:
            if left_side != 'boolean' or right_side != 'boolean':
                self.add_error(str(expr.token_operator.file_line) +
                               ':Erro Semantico:Expressões lógicas só podem ser usadas utilizando elementos de tipo booleano!')
            else:
                return 'boolean'
        return None

    def visitUnaryExpr(self, expr):
        aux = expr.right_expr.accept(self)
        if isinstance(expr.right_expr, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:Procedures nao possuem retorno para serem usados em expressões!')
                    return None
                else:
                    aux = aux.data_type
        if expr.token_operator.lexeme == '!':
            if aux is not None:
                if aux != 'boolean':
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:O operador ! só pode ser usado antes de elementos do tipo booleano!')
                    return None
                else:
                    return aux
        elif expr.token_operator.lexeme == '-':
            if aux is not None:
                if aux not in {'real', 'int'}:
                    self.add_error(str(expr.token_operator.file_line) +
                                   ':Erro Semantico:O operador - só pode ser usado antes de elementos do tipo real ou inteiro!')
                    return None
                else:
                    return aux
        return None

    def visitConstVarAccessExpr(self, expr):
        if expr.access_type == 'global':
            expr.scope = -1
        var_pos = self.symbol_table.get_line(expr.token_name.lexeme, expr.scope)
        if not var_pos:
            self.add_error(str(expr.token_name.file_line) +
                           ':Erro Semantico:Tentativa de acessar a variavel/constante \'' + expr.token_name.lexeme + '\', que nao existe!')
            return None
        elif len(var_pos) > 1:
            self.add_error(str(expr.token_name.file_line) +
                           ':Erro Semantico:Identificador ' + expr.token_name.lexeme + ' indexa ' + str(len(var_pos)) + ' variaveis distintas!')
            return None
        elif var_pos[0].tp not in {'var', 'const'}:
            self.add_error(str(expr.token_name.file_line) +
                           ':Erro Semantico:O identificador ' + expr.token_name.lexeme + ' nao corresponde a uma variavel ou constante!')
            return None
        elif not expr.token_name.file_line >= var_pos[0].program_line:
            self.add_error(str(expr.token_name.file_line) +
                           ':Erro Semantico:Tentativa de acesso a variavel/constante ' + expr.token_name.lexeme + ' ainda nao declarada!')
        if expr.index_array:
            if var_pos[0].indexes[0] is None:
                self.add_error(str(expr.token_name.file_line) +
                               ':Erro Semantico:Tentativa de indexar a variavel/constante ' + expr.token_name.lexeme + ' como se fosse um vetor, sendo que ela nao eh!')
            else:
                self.check_index(expr.index_array, expr.token_name.file_line)
        if expr.index_matrix:
            if var_pos[0].indexes[1] is None:
                self.add_error(str(expr.token_name.file_line) +
                               ':Erro Semantico:Tentativa de indexar a variavel/constante ' + expr.token_name.lexeme + ' como se fosse uma matriz, sendo que ela nao eh!')
            else:
                self.check_index(expr.index_matrix, expr.token_name.file_line)
        aux = var_pos[0].data_type
        if var_pos[0].data_type not in {'int', 'real', 'boolean', 'string'}:
            if aux not in {'int', 'string', 'real', 'boolean'}:
                if aux.find('struct') != -1:
                    aux = aux.split('.')[1]
                else:
                    aux = self.get_old_type(var_pos[0].data_type, expr.scope)
        return aux

    def visitFunctionStmt(self, stmt):
        func_pos = self.symbol_table.get_line(stmt.token_name.lexeme, -1)
        resp = ''
        if len(func_pos) > 1:
            resp = self.check_overloading(func_pos, stmt.token_name.file_line, 'Declaraçao')
            if resp is not None:
                for func in func_pos:
                    if func.program_line == stmt.token_name.file_line:
                        if len(set([item for item in func.params if len(self.count_itens(item, func.params)) > 1])) >= 1:
                            self.add_error(str(stmt.token_name.file_line) +
                                           ':Erro Semantico:Uma funçao nao pode ter dois parametros com o mesmo nome')
        for line in stmt.body:
            line.accept(self)
        tp = stmt.return_expr.accept(self)
        if tp is not None:
            if tp != stmt.return_tp.lexeme:
                self.add_error(str(stmt.return_expr.keyword.file_line) +
                               ':Erro Semantico:O tipo de retorno nao bate com o esperado! Esperava:' + stmt.return_tp.lexeme
                               + ', recebi:' + tp)
        else:
            self.add_error(str(stmt.return_expr.keyword.file_line) +
                           ':Erro Semantico:Retorno de tipo desconhecido!')

    def visitProcedureStmt(self, stmt):
        proc_pos = self.symbol_table.get_line(stmt.token_name.lexeme, -1)
        resp = ''
        if len(proc_pos) > 1:
            resp = self.check_overloading(proc_pos, stmt.token_name.file_line, 'Declaraçao')
        if resp is not None:
            for proc in proc_pos:
                if proc.program_line == stmt.token_name.file_line:
                    if len(set([item for item in proc.params if len(self.count_itens(item, proc.params)) > 1])) >= 1:
                        self.add_error(str(stmt.token_name.file_line) +
                                       ':Erro Semantico:Um procedure nao pode ter dois parametros com o mesmo nome')
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
                    self.add_error(str(stmt.program_line) +
                                   ':Erro Semantico:Procedures nao possuem retorno para serem usados em expressões!')
                else:
                    aux = aux.data_type
        if aux is not None:
            if aux != 'boolean':
                self.add_error(str(stmt.program_line) +
                               ':Erro Semantico:Condiçao de um if deve resultar em um booleano!')

    def visitPrintfStmt(self, stmt):
        for item in stmt.expression:
            if isinstance(item, expressions.FunctionCall):
                func_pos = self.symbol_table.get_line(item.func_exp.lexeme, -1)
                if not func_pos:
                    self.add_error(str(stmt.program_line) + ':Erro semantico:Chamada a funçao \'' + item.func_exp.lexeme + '\', a qual nao existe!')
                elif func_pos[0].data_type == '':
                    self.add_error(str(stmt.program_line) + ':Erro semantico:Nao e possível passar '
                                                            'procedimentos como argumento de prints, pois os mesmos'
                                                            ' nao retornam nada!')
            else:
                item.accept(self)

    def visitReturnfStmt(self, stmt):
        aux = stmt.value.accept(self)
        if aux is not None and aux not in {'int', 'string', 'boolean', 'real'}:
            temp = self.symbol_table.get_line(stmt.value.token_name.lexeme, stmt.value.scope)
            return temp[0].data_type
        return aux

    def visitVarStmt(self, stmt):
        var_pos = self.symbol_table.get_line(stmt.name, stmt.scope)
        if len(var_pos) > 1:
            if not var_pos[0].program_line >= stmt.program_line:
                self.add_error(str(stmt.program_line) +
                               ':Erro semantico:Ja existe outro elemento indexado com esse identificador!')
        # Verifica se o tipo dessa variavel realmente existe
        aux = stmt.tp
        if stmt.tp not in {'string', 'int', 'real', 'boolean'}:
            if stmt.tp.find('.') != -1:
                temp = stmt.tp.split('.')
                aux = temp[1]
            else:
                aux = self.get_old_type(stmt.tp, stmt.scope)
        if aux:
            # Verifica se o valor armazenado nessa variavel e compatível com seu tipo
            if stmt.init_val is not None:
                for val in stmt.init_val:
                    if isinstance(val, expressions.LiteralVal):
                        if not ((type(val.value) is str and aux == 'string') or
                                (type(val.value) is int and aux == 'int') or
                                (type(val.value) is float and aux == 'real') or
                                (type(val.value) is bool and aux == 'boolean')):
                            self.add_error(str(stmt.program_line) + ':Erro semantico:Variavel do tipo \'' + aux +
                                           '\' sendo inicializada com valor de tipo \'' + str(type(val.value)).split('\'')[1] + '\'')
                    else:
                        # Caso o valor inicial seja uma expressao
                        val.accept(self)
        else:
            self.add_error(str(stmt.program_line) + ':Erro semantico:Variavel de tipo inexistente!')
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
                self.add_error(str(stmt.program_line) +
                               ':Erro semantico:Ja existe outro elemento indexado com esse identificador!')
        aux = stmt.tp
        if stmt.tp not in {'string', 'int', 'real', 'boolean'}:
            if stmt.tp.find('.') != -1:
                temp = stmt.tp.split('.')
                aux = temp[1]
            else:
                aux = self.get_old_type(stmt.tp, stmt.scope)
        if aux:
            # Verifica se o valor armazenado nessa variavel e compatível com seu tipo
            if stmt.init_val is not None:
                for val in stmt.init_val:
                    if isinstance(val, expressions.LiteralVal):
                        if not ((type(val.value) is str and aux == 'string') or
                                (type(val.value) is int and aux == 'int') or
                                (type(val.value) is float and aux == 'real') or
                                (type(val.value) is bool and aux == 'boolean')):
                            self.add_error(str(stmt.program_line) + ':Erro semantico:Variavel do tipo \'' + aux +
                                           '\' sendo inicializada com valor de tipo \'' + str(type(val.value)).split('\'')[1] + '\'')
                    else:
                        # Caso o valor inicial seja uma expressao
                        val.accept(self)
        else:
            self.add_error(str(stmt.program_line) + ':Erro semantico:Variavel de tipo inexistente!')
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
            self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Identificador \'' + stmt.name.lexeme + '\' esta sendo utilizado para indexar mais de um elemento!')
        if stmt.extends is not None:
            extends_pos = self.symbol_table.get_line(stmt.extends.lexeme, stmt.scope)
            if not extends_pos:
                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct esta extendendo uma Struct que nao existe!')
            elif len(extends_pos) > 1:
                self.add_error(str(stmt.name.file_line) +
                               ':Erro Semantico:Struct extendendo outro elemento usando um identificador que indexa mais de um elemento!')
            elif stmt.name.file_line < extends_pos[0].program_line and extends_pos[0].tp == 'struct':
                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct esta extendendo uma Struct ainda nao definida!')
            elif extends_pos[0].tp not in {'struct', 'typedef'}:
                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct nao pode extender do tipo:' + extends_pos[0].tp + '!')
            elif extends_pos[0].tp == 'typedef':
                if stmt.name.file_line < extends_pos[0].program_line:
                    self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct extendendo tipo ainda nao definido!')
                    return
                old_tp = self.get_old_type(extends_pos[0].name, stmt.scope)
                if old_tp is not None:
                    if old_tp in {'int', 'string', 'real', 'boolean'}:
                        self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct nao pode extender do tipo:' + old_tp + '!')
                    else:
                        line = self.symbol_table.get_line(old_tp, stmt.scope)
                        if stmt.scope != -1:
                            line2 = self.symbol_table.get_line(old_tp, -1)
                            if line:
                                if line[0].tp != 'struct':
                                    if not line2:
                                        self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct nao pode extender do tipo:' + old_tp + '!')
                                elif stmt.name.file_line < line[0].program_line:
                                    self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct esta extendendo uma Struct ainda nao definida!')
                            if line2:
                                if line2[0].tp != 'struct':
                                    if not line:
                                        self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct nao pode extender do tipo:' + old_tp + '!')
                                elif stmt.name.file_line < line2[0].program_line:
                                    self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct esta extendendo uma Struct ainda nao definida!')
                            if not line and not line2:
                                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct extendendo elemento \'' + old_tp + '\', o qual e inexistente!')
                        else:
                            if not line:
                                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct extendendo elemento \'' + old_tp + '\', o qual e inexistente!')
                            elif line[0].tp != 'struct':
                                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct nao pode extender do tipo:' + old_tp + '!')
                            elif stmt.name.file_line < line[0].program_line:
                                self.add_error(str(stmt.name.file_line) + ':Erro Semantico:Struct extendendo struct \'' + old_tp + '\', a qual ainda nao foi definida!')

    def visitWhileStmt(self, stmt):
        aux = stmt.condition.accept(self)
        if isinstance(stmt.condition, expressions.FunctionCall):
            if aux is not None:
                if aux.tp == 'procedure':
                    self.add_error(str(stmt.program_line) +
                                   ':Erro Semantico:Procedures nao possuem retorno para serem usados em expressões!')
                else:
                    aux = aux.data_type
        if aux is not None:
            if aux != 'boolean':
                self.add_error(str(stmt.program_line) +
                               ':Erro Semantico:Condiçao de um while deve resultar em um booleano!')
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
                self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Uso do typedef para redefinir tipo \'' + aux + '\', sendo que esse tipo e inexistente!')
            else:
                if typedef_pos and name_pos2:
                    self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Uso do typedef idêntico em mais de um local!')
            new_type_pos = self.symbol_table.get_line(stmt.tp_name.lexeme, stmt.scope)
            new_type_pos2 = self.symbol_table.get_line(stmt.tp_name.lexeme, -1)
            if new_type_pos is not None and new_type_pos2 is not None:
                self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Ja existem outros elementos indexados com esse identificador:'
                               + stmt.tp_name.lexeme + '!')
            else:
                if new_type_pos is not None and len(new_type_pos) > 1:
                    if stmt.tp_name.file_line > new_type_pos[0].program_line:
                        self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Ja existem outros elementos indexados com esse identificador:'
                                   + stmt.tp_name.lexeme + '!')
                elif new_type_pos2 is not None and len(new_type_pos2) > 1:
                    if stmt.tp_name.file_line > new_type_pos2[0].program_line:
                        self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Ja existem outros elementos indexados com esse identificador:'
                                   + stmt.tp_name.lexeme + '!')
        else:
            typedef_pos = self.symbol_table.get_line(aux, stmt.scope)
            if not typedef_pos:
                self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Uso do typedef para redefinir tipo \'' + aux + '\', sendo que esse tipo e inexistente!')
            new_type_pos = self.symbol_table.get_line(stmt.tp_name.lexeme, stmt.scope)
            if new_type_pos is not None:
                if len(new_type_pos) > 1 and \
                        stmt.tp_name.file_line > new_type_pos[0].program_line:
                    self.add_error(str(stmt.tp_name.file_line) + ':Erro Semantico:Ja existem outros elementos indexados com esse identificador:'
                                   + stmt.tp_name.lexeme + '!')

    def visitReadStmt(self, stmt):
        for item in stmt.params:
            item.accept(self)

    def visitPrePosIncDec(self, expr):
        if isinstance(expr.variable, expressions.ConstVarAccess):
            if expr.variable.access_type == 'global':
                expr.variable.scope = -1
            inc_pos = self.symbol_table.get_line(expr.variable.token_name.lexeme, expr.variable.scope)
            if inc_pos and inc_pos[0].tp != 'var':
                self.add_error(str(expr.variable.token_name.file_line) + ':Erro Semantico:Identificador informado nao corresponde a uma'
                                                                         ' variavel, e sim a uma ' + inc_pos[0].tp + '!')
        data_type = expr.variable.accept(self)
        if data_type is not None and data_type not in {'int', 'real'}:
            self.add_error(str(expr.variable.token_name.file_line) + ':Erro Semantico:Tentativa de Inc/Dec em uma variavel de tipo primitivo ' +
                           data_type + '!')

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
        return None  # O identificador passado nao corresponde a um tipo valido

    # Um metodo para checar se o index de um vetor ou matriz e um inteiro
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
        self.add_error(str(file_line) + ':Erro Semantico:Um index de um vetor/matriz deve ser'
                                        ' um valor do tipo inteiro!')

    def check_overloading(self, func_pos, file_line, tp):
        if len(func_pos) > 1:
            if func_pos[0].name == 'start':
                self.add_error(str(file_line) + ':Erro Semantico:O procedure start nao pode sofrer sobrecarga!')
                return None
        all_func = True
        for item in func_pos:
            if item.tp not in {'function', 'procedure'}:
                all_func = False
        if not all_func:
            self.add_error(str(file_line) + ':Erro Semantico:Nome de idenficador indexa dois elementos de tipos distintos!')
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
                    self.add_error(str(file_line) + ':Erro Semantico:' + tp + ' de Funçao/Procedure duplicada -> Possível sobrecarga usada de forma errada!')
                    return None
            return all_args
        return None

    def check_attr(self, tp_pos, lexeme):
        if tp_pos:
            for param in tp_pos[0].params:
                if param.split('.')[1] == lexeme:
                    return param.split('.')[0]
        else:
            return None
        return False

    def count_itens(self, search_key, params):
        search_key = search_key.split('.')[1]
        return set([item for item in params if item.endswith('.' + search_key)])

    def add_error(self, erro):
        print(erro)
        info = erro.split(':')
        self.tokens_list.add_token(info[1] + ': ' + ''.join(info[2:]), '', int(info[0]))
