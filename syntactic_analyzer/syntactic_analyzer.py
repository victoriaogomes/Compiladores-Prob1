class SyntacticAnalyzer:

    def __init__(self, tokens_list):
        self.tokens_list = tokens_list

    def start(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            # TODO: Chamar estado typedef declaration
            print("VAI PARA TYPEDEF DECLARATION")
            self.start()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            # TODO: Chamar estado struct declaration
            print("VAI PARA STRUCT DECLARATION")
            self.start()
        elif self.tokens_list.lookahead().lexeme == 'var':
            # TODO: Chamar estado var declaration
            print("VAI PARA VAR DECLARATION")
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            # TODO: Chamar estado const declaration
            print("VAI PARA CONST DECLARATION")
            self.header2()
        elif self.tokens_list.lookahead().lexeme == ('function' or 'procedure'):
            # TODO: Chamar estado methods
            # TODO: Checar se esse or de function e procedure tá certo
            print("VAI PARA METHODS")
        else:
            # TODO: Descrever melhor o erro do estado inicial
            print("ERRO NO ESTADO INICIAL!!!!!")


    def header1(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            # TODO: Chamar estado typedef declaration
            print("VAI PARA TYPEDEF DECLARATION")
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            # TODO: Chamar estado struct declaration
            print("VAI PARA STRUCT DECLARATION")
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            # TODO: Chamar estado const declaration
            print("VAI PARA CONST DECLARATION")
            self.header3()
        elif self.tokens_list.lookahead().lexeme == ('function' or 'procedure'):
            # TODO: Chamar estado methods
            # TODO: Checar se esse or de function e procedure tá certo
            print("VAI PARA METHODS")
        else:
            # TODO: Descrever melhor o erro do do header 1
            print("ERRO NO ESTADO HEADER1!!!!!")

    def header2(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            # TODO: Chamar estado typedef declaration
            print("VAI PARA TYPEDEF DECLARATION")
            self.header2()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            # TODO: Chamar estado struct declaration
            print("VAI PARA STRUCT DECLARATION")
            self.header2()
        elif self.tokens_list.lookahead().lexeme == 'var':
            # TODO: Chamar estado var declaration
            print("VAI PARA VAR DECLARATION")
            self.header3()
        elif self.tokens_list.lookahead().lexeme == ('function' or 'procedure'):
            # TODO: Chamar estado methods
            # TODO: Checar se esse or de function e procedure tá certo
            print("VAI PARA METHODS")
        else:
            # TODO: Descrever melhor o erro do header 2
            print("ERRO NO ESTADO HEADER2!!!!!")

    def header3(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            # TODO: Chamar estado typedef declaration
            print("VAI PARA TYPEDEF DECLARATION")
            self.header3()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            # TODO: Chamar estado struct declaration
            print("VAI PARA STRUCT DECLARATION")
            self.header3()
        elif self.tokens_list.lookahead().lexeme == ('function' or 'procedure'):
            # TODO: Chamar estado methods
            # TODO: Checar se esse or de function e procedure tá certo
            print("VAI PARA METHODS")
        else:
            # TODO: Descrever melhor o erro do header 3
            print("ERRO NO ESTADO HEADER3!!!!!")

    def methods(self):
        if self.tokens_list.lookahead().lexeme == 'function':
            # TODO: Chamar estado function
            print("VAI PARA FUNCTION")
            self.methods()
        elif self.tokens_list.lookahead().lexeme == 'procedure':
            self.tokens_list.consume_token()
            # TODO: Chamar estado proc choice
            print("VAI PARA PROCEDURE CHOICE")
        else:
            # TODO: Descrever melhor o erro do methods
            print("ERRO NO ESTADO METHODS!!!!!")

    def proc_choice(self):
        if self.tokens_list.lookahead().lexeme == 'start':
            self.tokens_list.consume_token()
            # TODO: Chamar estado start procedure
            print("VAI PRA START PROCEDURE")
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            # TODO: Chamar estado procedure
            print("VAI PRA PROCEDURE")
        else:
            # TODO: Descrever melhor o erro do proc_choice
            print("ERRO NO ESTADO PROC_CHOICE!!!!!")

    def value(self):
        if self.tokens_list.lookahead().lexeme == ('true' or 'false'):
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme ==