import abc


class Expr:
    @abc.abstractmethod
    def accept(self, visitor):
        raise NotImplementedError


class Assign(Expr):
    # Assign: token = expr;
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitAssignExpr()


class Binary(Expr):
    # 5 + 4
    def __init__(self, left_expr, token_operator, right_expr):
        self.left_expr = left_expr
        self.token_operator = token_operator
        self.right_expr = right_expr

    def accept(self, visitor):
        return visitor.visitBinaryExpr()


class FunctionCall(Expr):
    # ano();
    def __init__(self, arguments, func_exp, token_parenthesis):
        self.arguments = arguments
        self.func_exp = func_exp
        self.token_parenthesis = token_parenthesis

    def accept(self, visitor):
        return visitor.visitFCallExpr()


class StructGet(Expr):
    # Pessoa.nome
    def __init__(self, struct_name, attr_name):
        self.struct_name = struct_name
        self.attr_name = attr_name

    def accept(self, visitor):
        return visitor.visitStructGetExpr()


class StructSet(Expr):
    # Pessoa.nome = Bruno
    def __init__(self, struct_name, attr_name, expr_value):
        self.struct_name = struct_name
        self.attr_name = attr_name
        self.expr_value = expr_value

    def accept(self, visitor):
        return visitor.visitStructSetExpr()


class Grouping(Expr):
    # (expr)
    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitGroupingExpr()


class LiteralVal(Expr):
    # int, real, string, boolean, IDE
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitLitValExpr()


class Logical(Expr):
    # &&, ||
    def __init__(self, left_expr, token_operator, right_expr):
        self.left_expr = left_expr
        self.token_operator = token_operator
        self.right_expr = right_expr

    def accept(self, visitor):
        return visitor.visitLogicalExpr()



class Unary(Expr):
    # !b, -5
    def __init__(self, token_operator, right_expr):
        self.token_operator = token_operator
        self.right_expr = right_expr

    def accept(self, visitor):
        return visitor.visitUnaryExpr()


class ConstVarAccess(Expr):
    # nome, idade
    def __init__(self, token_name, access_type='local'):
        self.token_name = token_name
        self.acces_type = access_type

    def accept(self, visitor):
        return visitor.visitConstVarAccessExpr()
