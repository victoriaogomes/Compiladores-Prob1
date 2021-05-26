import abc


class Stmt:
    @abc.abstractmethod
    def accept(self, visitor):
        raise NotImplementedError


class Function(Stmt):
    # function int ano(){}
    # body é uma lista de stmt
    # params é uma lista de tokens
    def __init__(self, token_name, params, body, return_tp):
        self.token_name = token_name
        self.params = params
        self.body = body
        self.return_tp = return_tp

    def accept(self, visitor):
        return visitor.visitFunctionStmt(self)


class Procedure(Stmt):
    # procedure ano(){}
    # body é uma lista de stmt
    # params é uma lista de tokens
    def __init__(self, token_name, params, body):
        self.token_name = token_name
        self.params = params
        self.body = body

    def accept(self, visitor):
        return visitor.visitProcedureStmt(self)


class Expression(Stmt):

    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitExpressionStmt(self)


class IfThenElse(Stmt):
    # O then_branch e o else_branch são statements
    def __init__(self, cond_expr, then_branch, else_branch):
        self.cond_expr = cond_expr
        self.then_branch = then_branch
        self.else_branch = else_branch

    def accept(self, visitor):
        return visitor.visitIfThenElseStmt(self)


class Printf(Stmt):
    # Expression: Lista de expressões a serem impressas
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitPrintfStmt(self)


class Returnf(Stmt):
    # Keyword: token do return
    # Value: valor que será retornado
    def __init__(self, keyword, value):
        self.keyword = keyword
        self.value = value

    def accept(self, visitor):
        return visitor.visitReturnfStmt(self)


class Var(Stmt):
    # names: nomes das variáveis
    def __init__(self, name, init_val, tp, index_array=-1, index_matrix=-1):
        self.name = name
        self.init_val = init_val
        self.tp = tp
        self.index_array = index_array
        self.index_matrix = index_matrix

    def accept(self, visitor):
        return visitor.visitVarStmt(self)


class Var_block(Stmt):
    # var_list: é surpreendentemente uma lista de var
    def __init__(self, var_list):
        self.var_list = var_list

    def accept(self, visitor):
        return visitor.visitVarBlockStmt(self)


class Const(Stmt):
    # const_name: nome da variável
    def __init__(self, name, init_val, tp, index_array=-1, index_matrix=-1):
        self.name = name
        self.init_val = init_val
        self.tp = tp
        self.index_array = index_array
        self.index_matrix = index_matrix

    def accept(self, visitor):
        return visitor.visitConstStmt(self)

class Const_block(Stmt):
    # const_name: nome da variável
    def __init__(self, const_list):
        self.const_list = const_list

    def accept(self, visitor):
        return visitor.visitConstBlockStmt(self)


class Struct(Stmt):
    # variables: lista de variáveis da struct
    def __init__(self, name, variables, extends=None):
        self.name = name
        self.variables = variables
        self.extends = extends

    def accept(self, visitor):
        return visitor.visitStructStmt(self)


class While(Stmt):
    # variables: lista de variáveis da struct
    def __init__(self, condition, body):
        self.body = body
        self.condition = condition

    def accept(self, visitor):
        return visitor.visitWhileStmt(self)


class Typedef(Stmt):
    # variables: lista de variáveis da struct
    def __init__(self, tp_name, old_tp):
        self.old_tp = old_tp
        self.tp_name = tp_name

    def accept(self, visitor):
        return visitor.visitTypedefStmt(self)


class Read(Stmt):
    # params: lista das variáveis onde será armazenado o que for lido
    def __init__(self, params):
        self.params = params

    def accept(self, visitor):
        return visitor.visitReadStmt(self)
