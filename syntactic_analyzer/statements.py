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
        return visitor.visitFunctionStmt()


class Procedure(Stmt):
    # procedure ano(){}
    # body é uma lista de stmt
    # params é uma lista de tokens
    def __init__(self, token_name, params, body):
        self.token_name = token_name
        self.params = params
        self.body = body

    def accept(self, visitor):
        return visitor.visitProcedureStmt()


class Expression(Stmt):

    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitExpressionStmt()


class IfThenElse(Stmt):
    # O then_branch e o else_branch são statements
    def __init__(self, cond_expr, then_branch, else_branch):
        self.cond_expr = cond_expr
        self.then_branch = then_branch
        self.else_branch = else_branch

    def accept(self, visitor):
        return visitor.visitIfThenElseStmt()


class Printf(Stmt):
    # Expression: Lista de expressões a serem impressas
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitPrintfStmt()


class Returnf(Stmt):
    # Keyword: token do return
    # Value: valor que será retornado
    def __init__(self, keyword, value):
        self.keyword = keyword
        self.value = value

    def accept(self, visitor):
        return visitor.visitReturnfStmt()


class Var(Stmt):
    # var_name: nome da variável
    def __init__(self, name, init_val):
        self.name = name
        self.init_value = init_val

    def accept(self, visitor):
        return visitor.visitVarStmt()


class Const(Stmt):
    # const_name: nome da variável
    def __init__(self, name, init_val):
        self.name = name
        self.init_val = init_val

    def accept(self, visitor):
        return visitor.visitConstStmt()


class Struct(Stmt):
    # variables: lista de variáveis da struct
    def __init__(self, name, variables, extends=None):
        self.name = name
        self.variables = variables
        self.extends = extends

    def accept(self, visitor):
        return visitor.visitStructStmt()


class While(Stmt):
    # variables: lista de variáveis da struct
    def __init__(self, condition, body):
        self.body = body
        self.condition = condition

    def accept(self, visitor):
        return visitor.visitWhileStmt()


class Typedef(Stmt):
    # variables: lista de variáveis da struct
    def __init__(self, tp_name, old_tp):
        self.old_tp = old_tp
        self.tp_name = tp_name

    def accept(self, visitor):
        return visitor.visitTypedefStmt()


class Read(Stmt):
    # params: lista das variáveis onde será armazenado o que for lido
    def __init__(self, params):
        self.params = params

    def accept(self, visitor):
        return visitor.visitReadStmt()
