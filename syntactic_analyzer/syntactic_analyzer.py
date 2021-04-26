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

    def variable(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            # TODO: Chamar CONT ELEMENTO
            print("VAI PRA CONT ELEMENT")
        elif self.tokens_list.lookahead().lexeme == ('global' or 'local'):
            self.scope_variable()
            print("VAI PRA SCOPE VARIABLE")
        else:
            # TODO: Descrever melhor o erro do variable
            print("ERRO NO ESTADO Variable!!!!!")

    def scope_variable(self):
        if self.tokens_list.lookahead().lexeme == ('global' or 'local'):
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '.':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead.lexeme_type == 'IDE':
                    self.tokens_list.consume_token()
                    # TODO: Chamar CONT ELEMENT
                    print("VAI PRA CONT ELEMENT")
                else:
                    # TODO: Descrever melhor o erro do scope variable
                    print("ERRO NO ESTADO SCOPE Variable!!!!!")
            else:
                # TODO: Descrever melhor o erro do scope variable
                print("ERRO NO ESTADO SCOPE Variable!!!!!")
        else:
            # TODO: Descrever melhor o erro do scope variable
            print("ERRO NO ESTADO SCOPE Variable!!!!!")

    def vect_mat_index(self):
        if self.tokens_list.lookahead().lexeme == ('true' or 'false' or 'global' or 'local' or '('):
            # TODO: Chamar ARIT EXP 1
            print("VAI PRA ARIT EXP 1")
        elif self.tokens_list.lookahead().lexeme_type == ('NRO' or 'IDE' or 'CAD'):
            # TODO: Chamar ARIT EXP 1
            print("VAI PRA ARIT EXP 1")
        else:
            # TODO: Descrever melhor o erro do vect mat index
            print("ERRO NO ESTADO  vect mat index!!!!!")

    def data_type(self):
        if self.tokens_list.lookahead().lexeme_type == ('NRO' or 'CAD' or 'IDE'):
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme == ('true' or 'false'):
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do data type
            print("ERRO NO ESTADO data type!!!!!")

    def cont_element(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            print("VAI PRA vect mat index 1")
        elif self.tokens_list.lookahead().lexeme == '.':
            # TODO: Chamar MATRIZ E 2
            print("VAI PRA MATRIZ E 2")

    def struct_e1(self):
        if self.tokens_list.lookahead().lexeme == '.':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                self.cont_element()
                print("VAI PRA CONT ELEMENT")
            else:
                # TODO: Descrever melhor o erro do struct e1
                print("ERRO NO ESTADO struct e1!!!!!")
        else:
            # TODO: Descrever melhor o erro do struct e1
            print("ERRO NO ESTADO struct e1!!!!!")

    def matrix_e1(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            print("VAI PRA VECT MAT INDEX")
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                self.matrix_e2()
                print("VAI PRA MATRIX E2")
            else:
                # TODO: Descrever melhor o erro do matrix e1
                print("ERRO NO ESTADO matrix e1!!!!!")
        else:
            self.matrix_e2()

    def matrix_e2(self):
        if self.tokens_list.lookahead().lexeme == '.':
            self.struct_e1()
            print("VAI PRA STRUCT E1")

    def var_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                self.first_var()
            else:
                # TODO: Descrever melhor o erro do VAR DECLARATION
                print("ERRO NO ESTADO VAR DECLARATION!!!!!")
        else:
            # TODO: Descrever melhor o erro do VAR DECLARATION
            print("ERRO NO ESTADO VAR DECLARATION!!!!!")

    def first_var(self):
        if self.tokens_list.lookahead().lexeme == ('int' or 'real' or 'boolean' or 'struct'):
            self.continue_sos()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.continue_sos()
            self.var_id()
        else:
            # TODO: Descrever melhor o erro do FIRST VAR
            print("ERRO NO ESTADO FIRST VAR!!!!!")

    def next_var(self):
        if self.tokens_list.lookahead().lexeme == ('int' or 'real' or 'boolean' or 'struct'):
            self.continue_sos()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.continue_sos()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do NEXT VAR
            print("ERRO NO ESTADO NEXT VAR!!!!!")

    def continue_sos(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            self.data_type()
        else:
            self.data_type()

    def var_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.var_exp()
        else:
            # TODO: Descrever melhor o erro do VAR ID
            print("ERRO NO ESTADO VAR ID!!!!!")

    def var_exp(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            self.expression()
            self.verif_var()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_var()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                self.structure()
            else:
                # TODO: Descrever melhor o erro do VAR EXP
                print("ERRO NO ESTADO VAR EXO!!!!!")
        else:
            # TODO: Descrever melhor o erro do VAR EXP
            print("ERRO NO ESTADO VAR EXO!!!!!")

    def structure(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            self.init_array()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_var()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                self.cont_matrix()
            else:
                # TODO: Descrever melhor o erro do STRUCTURE
                print("ERRO NO ESTADO STRUCTURE!!!!!")
        else:
            # TODO: Descrever melhor o erro do STRUCTURE
            print("ERRO NO ESTADO STRUCTURE!!!!!")

    def cont_matrix(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            self.init_matrix()
        elif self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_var()
        else:
            # TODO: Descrever melhor o erro do CONT MATRIX
            print("ERRO NO CONT MATRIX!!!!!")

    def init_array(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.expression()
            self.next_array()
        else:
            # TODO: Descrever melhor o erro do INIT ARRAY
            print("ERRO NO ESTADO INIT ARRAY!!!!!")

    def next_array(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.expression()
            self.next_array()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.verif_var()
        else:
            # TODO: Descrever melhor o erro do NEXT ARRAY
            print("ERRO NO ESTADO NEXT ARRAY!!!!!")

    def init_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.matrix_value()
        else:
            # TODO: Descrever melhor o erro do INIT MATRIX
            print("ERRO NO ESTADO INIT MATRIX!!!!!")

    def matrix_value(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.expression()
            self.next_matrix()
        else:
            # TODO: Descrever melhor o erro do MATRIX VALUE
            print("ERRO NO ESTADO MATRIX VALUE!!!!!")

    def next_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.expression()
            self.next_matrix()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.next()
        else:
            # TODO: Descrever melhor o erro do NEXT MATRIX
            print("ERRO NO ESTADO NEXT MATRIX!!!!!")

    def next(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.matrix_value()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.verif_var()
        else:
            # TODO: Descrever melhor o erro do NEXT
            print("ERRO NO ESTADO INIT NEXT!!!!!")

    def verif_var(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_var()
        else:
            # TODO: Descrever melhor o erro do VERIF VAR
            print("ERRO NO ESTADO VERIF VAR!!!!!")

    def const_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                self.first_const()
            else:
                # TODO: Descrever melhor o erro do CONST DECLARATION
                print("ERRO NO ESTADO CONST DECLARATION!!!!!")
        else:
            # TODO: Descrever melhor o erro do CONST DECLARATION
            print("ERRO NO ESTADO CONST DECLARATION!!!!!")

    def first_const(self):
        self.continue_const_sos()
        self.const_id()

    def continue_const_sos(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            self.data_type()
        else:
            self.data_type()

    def next_const(self):
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            self.continue_const_sos()
            self.const_id()

    def const_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.const_exp()
        else:
            # TODO: Descrever melhor o erro do CONST ID
            print("ERRO NO ESTADO CONST ID!!!!!")

    def const_exp(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            self.expression()
            self.verif_const()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                self.const_structure()
            else:
                # TODO: Descrever melhor o erro do CONST EXP
                print("ERRO NO ESTADO CONST EXP!!!!!")

    def const_structure(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '=':
                    self.tokens_list.consume_token()
                    self.init_const_matrix()
                else:
                    # TODO: Descrever melhor o erro do CONST STRUCTURE
                    print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
            else:
                # TODO: Descrever melhor o erro do CONST STRUCTURE
                print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
        elif self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '[':
                self.tokens_list.consume_token()
                self.expression()
                self.next_const_array()
            else:
                # TODO: Descrever melhor o erro do CONST STRUCTURE
                print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
        else:
            # TODO: Descrever melhor o erro do CONST STRUCTURE
            print("ERRO NO ESTADO CONST STRUCTURE!!!!!")

    def next_const_array(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.expression()
            self.next_const_array()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.verif_const()
        else:
            # TODO: Descrever melhor o erro do NEXT CONST ARRAY
            print("ERRO NO ESTADO NEXT CONST ARRAY!!!!!")

    def init_const_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.matrix_const_value()
        else:
            # TODO: Descrever melhor o erro do INIT CONST MATRIX
            print("ERRO NO ESTADO INIT CONST MATRIX!!!!!")

    def matrix_const_value(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.expression()
            self.next_const_matrix()
        else:
            # TODO: Descrever melhor o erro do MATRIX CONST VALUE
            print("ERRO NO ESTADO MATRIX CONST VALUE!!!!!")

    def next_const_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.expression()
            self.next_const_matrix()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.next_const2()
        else:
            # TODO: Descrever melhor o erro do NEXT CONST MATRIX
            print("ERRO NO ESTADO NEXT CONST MATRIX!!!!!")

    def next_const2(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.matrix_const_value()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.verif_const()
        else:
            # TODO: Descrever melhor o erro do NEXT CONST 2
            print("ERRO NO ESTADO NEXT CONST 2!!!!!")

    def verif_const(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.const_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_const()
        else:
            # TODO: Descrever melhor o erro do VERIF CONST
            print("ERRO NO ESTADO VERIF CONST!!!!!")

    def function(self):
        if self.tokens_list.lookahead().lexeme == 'function':
            self.tokens_list.consume_token()
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '(':
                    self.tokens_list.consume_token()
                    self.continue_function()
                else:
                    # TODO: Descrever melhor o erro do FUNCTION
                    print("ERRO NO ESTADO FUNCTION!!!!!")
            else:
                # TODO: Descrever melhor o erro do FUNCTION
                print("ERRO NO ESTADO FUNCTION!!!!!")
        else:
            # TODO: Descrever melhor o erro do FUNCTION
            print("ERRO NO ESTADO FUNCTION!!!!!")

    def continue_function(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            self.block_function()
        elif self.tokens_list.lookahead().lexeme == ('int' or 'real' or 'string' or 'boolean' or 'struct'):
            self.parameters()
            self.block_function()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.parameters()
            self.block_function()
        else:
            # TODO: Descrever melhor o erro do CONTINUE FUNCTION
            print("ERRO NO ESTADO CONTINUE FUNCTION!!!!!")

    def parameters(self):
        if self.tokens_list.lookahead().lexeme == ('int' or 'real' or 'string' or 'boolean') or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                self.param_loop()
            else:
                # TODO: Descrever melhor o erro do PARAMETERS
                print("ERRO NO ESTADO PARAMETERS!!!!!")
        elif self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                self.param_loop()
            else:
                # TODO: Descrever melhor o erro do PARAMETERS
                print("ERRO NO ESTADO PARAMETERS!!!!!")
        else:
            # TODO: Descrever melhor o erro do PARAMETERS
            print("ERRO NO ESTADO PARAMETERS!!!!!")

    def param_loop(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.parameters()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do PARAM LOOP
            print("ERRO NO ESTADO PARAM LOOP!!!!!")

    def block_function(self):
        if self.tokens_list.lookahead().lexeme == '{':
            self.tokens_list.consume_token()
            self.block_function_content()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '}':
                    self.tokens_list.consume_token()
                else:
                    # TODO: Descrever melhor o erro do BLOCK FUNCTION
                    print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
            else:
                # TODO: Descrever melhor o erro do BLOCK FUNCTION
                print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
        else:
            # TODO: Descrever melhor o erro do BLOCK FUNCTION
            print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")

    def block_function_content(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.var_declaration()
            self.content1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            self.const_declaration()
            self.content2()
        else:
            self.function_content()

    def function_content(self):
        self.code()
        if self.tokens_list.lookahead().lexeme == 'return':
            self.tokens_list.consume_token()
            self.expression()
        else:
            # TODO: Descrever melhor o erro do FUNCTION CONTENT
            print("ERRO NO ESTADO FUNCTION CONTENT!!!!!")

    def content1(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            self.const_declaration()
            self.content3()
        else:
            self.function_content()

    def content2(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.var_declaration()
            self.content3()
        else:
            self.function_content()

    def content3(self):
        self.function_content()

    def structure_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                self.struct_vars()
            else:
                # TODO: Descrever melhor o erro do STRUCTURE DECLARATION
                print("ERRO NO ESTADO STRUCTURE DECLARATION!!!!!")
        else:
            # TODO: Descrever melhor o erro do STRUCTURE DECLARATION
            print("ERRO NO ESTADO STRUCTURE DECLARATION!!!!!")

    def struct_vars(self):
        if self.tokens_list.lookahead().lexeme == '{':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == 'var':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme() == '{':
                    self.tokens_list.consume_token()
                    self.first_struct_var()
                else:
                    # TODO: Descrever melhor o erro do STRUCT VAR
                    print("ERRO NO ESTADO STRUCT VAR!!!!!")
            else:
                # TODO: Descrever melhor o erro do STRUCT VAR
                print("ERRO NO ESTADO STRUCT VAR!!!!!")
        elif self.tokens_list.lookahead().lexeme == 'extends':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == 'var':
                        self.tokens_list.consume_token()
                        if self.tokens_list.lookahead().lexeme() == '{':
                            self.tokens_list.consume_token()
                            self.first_struct_var()
                        else:
                            # TODO: Descrever melhor o erro do STRUCT VAR
                            print("ERRO NO ESTADO STRUCT VAR!!!!!")
                    else:
                        # TODO: Descrever melhor o erro do STRUCT VAR
                        print("ERRO NO ESTADO STRUCT VAR!!!!!")
                else:
                    # TODO: Descrever melhor o erro do STRUCT VAR
                    print("ERRO NO ESTADO STRUCT VAR!!!!!")
            else:
                # TODO: Descrever melhor o erro do STRUCT VAR
                print("ERRO NO ESTADO STRUCT VAR!!!!!")
        else:
            # TODO: Descrever melhor o erro do STRUCT VAR
            print("ERRO NO ESTADO STRUCT VAR!!!!!")

    def first_struct_var(self):
        self.data_type()
        self.struct_var_id()

    def struct_var_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.struct_var_exp()
        else:
            # TODO: Descrever melhor o erro do STRUCT VAR ID
            print("ERRO NO ESTADO STRUCT VAR ID!!!!!")

    def next_struct_var(self):
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do NEXT STRUCT VAR
                print("ERRO NO ESTADO NEXT STRUCT VAR!!!!!")
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.data_type()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ('int' or 'real' or 'string' or 'boolean'):
            self.data_type()
            self.struct_var_id()
        else:
            # TODO: Descrever melhor o erro do NEXT STRUCT VAR
            print("ERRO NO ESTADO NEXT STRUCT VAR!!!!!")

    def struct_var_exp(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_struct_var()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'NRO':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ']':
                    self.tokens_list.consume_token()
                    self.struct_matrix()
                else:
                    # TODO: Descrever melhor o erro do STRUCT VAR EXP
                    print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
            else:
                # TODO: Descrever melhor o erro do STRUCT VAR EXP
                print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
        else:
            # TODO: Descrever melhor o erro do STRUCT VAR EXP
            print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")

    def struct_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'NRO':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ']':
                    self.tokens_list.consume_token()
                    self.cont_struct_matrix()
                else:
                    # TODO: Descrever melhor o erro do STRUCT MATRIX
                    print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
            else:
                # TODO: Descrever melhor o erro do STRUCT MATRIX
                print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
        elif self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_struct_var()
        else:
            # TODO: Descrever melhor o erro do STRUCT MATRIX
            print("ERRO NO ESTADO STRUCT MATRIX!!!!!")

    def cont_struct_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_struct_var()
        else:
            # TODO: Descrever melhor o erro do CONT STRUCT MATRIX
            print("ERRO NO ESTADO CONT STRUCT MATRIX!!!!!")

    def expression(self):
        if self.tokens_list.lookahead().lexeme == '!':
            self.tokens_list.consume_token()
            self.rel_exp()
            self.log_exp()
        elif self.tokens_list.lookahead().lexeme == ('true' or 'false' or 'global' or 'local' or '('):
            self.rel_exp()
            self.log_exp()
        elif self.tokens_list.lookahead().lexeme_type == ('IDE' or 'NRO' or 'CAD'):
            self.rel_exp()
            self.log_exp()
        else:
            # TODO: Descrever melhor o erro do EXPRESSION
            print("ERRO NO ESTADO EXPRESSION!!!!!")

    def log_exp(self):
        if self.tokens_list.lookahead().lexeme == ('&&' or '||'):
            self.logic_symbol()
            self.rel_exp()
            self.log_exp()

    def logic_symbol(self):
        if self.tokens_list.lookahead().lexeme == ('&&' or '||'):
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do LOGIC SYMBOL
            print("ERRO NO ESTADO LOGIC SYMBOL!!!!!")

    def rel_exp(self):
        self.arit_exp1()
        self.rel_exp2()

    def rel_exp2(self):
        if self.tokens_list.lookahead().lexeme == ('>' or '<' or '==' or '>=' or '<='):
            self.rel_symbol()
            self.arit_exp1()
            self.rel_exp2()

    def rel_symbol(self):
        if self.tokens_list.lookahead().lexeme == ('>' or '<' or '==' or '>=' or '<='):
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do REL SYMBOL
            print("ERRO NO ESTADO REL SYMBOL!!!!!")

    def arit_exp1(self):
        self.term()
        self.arit_exp2()

    def arit_exp2(self):
        if self.tokens_list.lookahead().lexeme == ('+' or '-'):
            self.arit_symb1()
            self.term()
            self.arit_exp2()

    def arit_symb1(self):
        if self.tokens_list.lookahead().lexeme == ('+' or '-'):
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do ARIT SYMB 1
            print("ERRO NO ESTADO ARIT SYMB 1!!!!!")

    def term(self):
        self.operate()
        self.term2()

    def term2(self):
        if self.tokens_list.lookahead().lexeme == ('*' or '/'):
            self.arit_symb2()
            self.operate()
            self.term2()

    def arit_symb2(self):
        if self.tokens_list.lookahead().lexeme == ('*' or '/'):
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do ARIT SYMB 2
            print("ERRO NO ESTADO ARIT SYMB 2!!!!!")

    def operate(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            self.expression()
            if self.tokens_list.lookahead().lexeme == ')':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do OPERATE
                print("ERRO NO ESTADO OPERATE!!!!!")
        elif self.tokens_list.lookahead().lexeme == ('true' or 'false'):
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type == ('NRO' or 'CAD'):
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.cont_operate()
        elif self.tokens_list.lookahead().lexeme == ('global' or 'local'):
            self.scope_variable()
        else:
            # TODO: Descrever melhor o erro do OPERATE
            print("ERRO NO ESTADO OPERATE!!!!!")

    def cont_operate(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.function_call()
        else:
            self.cont_element()

    def typedef_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            self.tokens_list.consume_token()
            self.cont_typedef_dec()
        else:
            # TODO: Descrever melhor o erro do TYPEDEF DECLARATION
            print("ERRO NO ESTADO TYPEDEF DECLARATION!!!!!")

    def cont_typedef_dec(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme_type == 'IDE':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == ';':
                        self.tokens_list.consume_token()
                    else:
                        # TODO: Descrever melhor o erro do CONT TYPEDEF DEC
                        print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                else:
                    # TODO: Descrever melhor o erro do CONT TYPEDEF DEC
                    print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
            else:
                # TODO: Descrever melhor o erro do CONT TYPEDEF DEC
                print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
        elif self.tokens_list.lookahead().lexeme_type == 'IDE' or self.tokens_list.lookahead().lexeme == ('int' or 'real' or 'string' or 'boolean'):
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ';':
                    self.tokens_list.consume_token()
                else:
                    # TODO: Descrever melhor o erro do CONT TYPEDEF DEC
                    print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
            else:
                # TODO: Descrever melhor o erro do CONT TYPEDEF DEC
                print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
        else:
            # TODO: Descrever melhor o erro do CONT TYPEDEF DEC
            print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")

    def start_procedure(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ')':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    self.proc_content()
                else:
                    # TODO: Descrever melhor o erro do START PROCEDURE
                    print("ERRO NO ESTADO  START PROCEDURE!!!!!")
            else:
                # TODO: Descrever melhor o erro do START PROCEDURE
                print("ERRO NO ESTADO  START PROCEDURE!!!!!")
        else:
            # TODO: Descrever melhor o erro do START PROCEDURE
            print("ERRO NO ESTADO  START PROCEDURE!!!!!")

    def procedure(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.proc_param()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    self.proc_content()
                else:
                    # TODO: Descrever melhor o erro do PROCEDURE
                    print("ERRO NO ESTADO PROCEDURE!!!!!")
            else:
                # TODO: Descrever melhor o erro do PROCEDURE
                print("ERRO NO ESTADO PROCEDURE!!!!!")
        else:
            # TODO: Descrever melhor o erro do PROCEDURE
            print("ERRO NO ESTADO PROCEDURE!!!!!")

    def proc_param(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme == ('struct' or 'int' or 'real' or 'string' or 'boolean') or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.parameters()
        else:
            # TODO: Descrever melhor o erro do PROC PARAM
            print("ERRO NO ESTADO PROC PARAM!!!!!")

    def proc_content(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.var_declaration()
            self.proc_content2()
        elif self.tokens_list.lookahead().lexeme == 'const':
            self.const_declaration()
            self.proc_content3()
        else:
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do PROC CONTENT
                print("ERRO NO ESTADO PROC CONTENT!!!!!")

    def proc_content2(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            self.const_declaration()
            self.proc_content4()
        else:
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do PROC CONTENT2
                print("ERRO NO ESTADO PROC CONTENT2!!!!!")

    def proc_content3(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.var_declaration()
            self.proc_content4()
        else:
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do PROC CONTENT3
                print("ERRO NO ESTADO PROC CONTENT3!!!!!")

    def proc_content4(self):
        self.code()
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do PROC CONTENT4
            print("ERRO NO ESTADO PROC CONTENT4!!!!!")

    def code(self):
        if self.tokens_list.lookahead().lexeme == ('global' or 'local' or 'struct' or 'typedef' or '++' or '--' or 'print' or 'read' or 'while' or 'if') or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.command()
            self.code()

    def command(self):
        if self.tokens_list.lookahead().lexeme == 'print':
            self.print_func()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.other_commands()
        elif self.tokens_list.lookahead().lexeme == ('global' or 'local'):
            self.scope_variable()
            self.other_commands()
        elif self.tokens_list.lookahead().lexeme == 'read':
            self.read()
        elif self.tokens_list.lookahead().lexeme == 'while':
            self.while_func()
        elif self.tokens_list.lookahead().lexeme == 'if':
            self.conditional()
        elif self.tokens_list.lookahead().lexeme == 'typedef':
            self.typedef_declaration()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            self.structure_declaration()
        elif self.tokens_list.lookahead().lexeme == ('++' or '--'):
            self.tokens_list.consume_token()
            self.variable()
        else:
            # TODO: Descrever melhor o erro do COMMAND
            print("ERRO NO ESTADO COMMAND!!!!!")

    def other_commands(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.function_call()
        else:
            self.cont_element()
            self.other_commands2()

    def other_commands2(self):
        if self.tokens_list.lookahead().lexeme == ('++' or '--'):
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do OTHER COMMANDS2
                print("ERRO NO ESTADO OTHER COMMANDS2!!!!!")
        elif self.tokens_list.lookahead().lexeme == '=':
            self.assignment()
        else:
            # TODO: Descrever melhor o erro do OTHER COMMANDS2
            print("ERRO NO ESTADO OTHER COMMANDS2!!!!!")

    def print_func(self):
        if self.tokens_list.lookahead().lexeme == 'print':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.printable_list()
            else:
                # TODO: Descrever melhor o erro do PRINT FUNC
                print("ERRO NO ESTADO PRINT FUNC!!!!!")
        else:
            # TODO: Descrever melhor o erro do PRINT FUNC
            print("ERRO NO ESTADO PRINT FUNC!!!!!")

    def printable_list(self):
        self.printable()
        self.next_print_value()

    def printable(self):
        if self.tokens_list.lookahead().lexeme_type == 'CAD':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme == ('global' or 'local') or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.variable()
        else:
            # TODO: Descrever melhor o erro do PRINTABLE
            print("ERRO NO ESTADO PRINTABLE!!!!!")

    def next_print_value(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.printable_list()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do NEXT PRINT VALUE
                print("ERRO NO ESTADO NEXT PRINT VALUE!!!!!")
        else:
            # TODO: Descrever melhor o erro do NEXT PRINT VALUE
            print("ERRO NO ESTADO NEXT PRINT VALUE!!!!!")

    def assignment(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            self.expression()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do ASSIGNMENT
                print("ERRO NO ESTADO ASSIGNMENT!!!!!")
        else:
            # TODO: Descrever melhor o erro do ASSIGNMENT
            print("ERRO NO ESTADO ASSIGNMENT!!!!!")

    def function_call(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            self.cont_f_call()
        else:
            # TODO: Descrever melhor o erro do FUNCTION CALL
            print("ERRO NO ESTADO FUNCTION CALL!!!!!")

    def cont_f_call(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme == ('true' or 'false' or 'global' or 'local' or '(' or '!') or self.tokens_list.lookahead().lexeme_type == ('NRO' or 'IDE' or 'CAD'):
            self.expression()
            self.f_call_params()
        else:
            # TODO: Descrever melhor o erro do CONT F CALL
            print("ERRO NO ESTADO CONT F CALL!!!!!")

    def f_call_params(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.expression()
            self.f_call_params()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        else:
            # TODO: Descrever melhor o erro do F CALL PARAMS
            print("ERRO NO ESTADO F CALL PARAMS!!!!!")

    def read(self):
        if self.tokens_list.lookahead().lexeme == 'read':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.read_params()
            else:
                # TODO: Descrever melhor o erro do READ
                print("ERRO NO ESTADO READ!!!!!")
        else:
            # TODO: Descrever melhor o erro do READ
            print("ERRO NO ESTADO READ!!!!!")

    def read_params(self):
        self.variable()
        self.read_loop()

    def read_loop(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.read_params()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do READ LOOP
                print("ERRO NO ESTADO READ LOOP!!!!!")
        else:
            # TODO: Descrever melhor o erro do READ LOOP
            print("ERRO NO ESTADO READ LOOP!!!!!")

    def while_func(self):
        if self.tokens_list.lookahead().lexeme == 'while':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.expression()
                if self.tokens_list.lookahead().lexeme == ')':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == '{':
                        self.tokens_list.consume_token()
                        self.code()
                        if self.tokens_list.lookahead().lexeme == '}':
                            self.tokens_list.consume_token()
                        else:
                            # TODO: Descrever melhor o erro do WHILE FUNC
                            print("ERRO NO ESTADO WHILE FUNC!!!!!")
                    else:
                        # TODO: Descrever melhor o erro do WHILE FUNC
                        print("ERRO NO ESTADO WHILE FUNC!!!!!")
                else:
                    # TODO: Descrever melhor o erro do WHILE FUNC
                    print("ERRO NO ESTADO WHILE FUNC!!!!!")
            else:
                # TODO: Descrever melhor o erro do WHILE FUNC
                print("ERRO NO ESTADO WHILE FUNC!!!!!")
        else:
            # TODO: Descrever melhor o erro do WHILE FUNC
            print("ERRO NO ESTADO WHILE FUNC!!!!!")

    def conditional(self):
        if self.tokens_list.lookahead().lexeme == 'if':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.expression()
                if self.tokens_list.lookahead().lexeme == ')':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == 'then':
                        self.tokens_list.consume_token()
                        if self.tokens_list.lookahead().lexeme == '{':
                            self.tokens_list.consume_token()
                            self.code()
                            if self.tokens_list.lookahead().lexeme == '}':
                                self.tokens_list.consume_token()
                                self.else_part()
                            else:
                                # TODO: Descrever melhor o erro do CONDITIONAL
                                print("ERRO NO ESTADO CONDITIONAL!!!!!")
                        else:
                            # TODO: Descrever melhor o erro do CONDITIONAL
                            print("ERRO NO ESTADO CONDITIONAL!!!!!")
                else:
                    # TODO: Descrever melhor o erro do CONDITIONAL
                    print("ERRO NO ESTADO CONDITIONAL!!!!!")
            else:
                # TODO: Descrever melhor o erro do CONDITIONAL
                print("ERRO NO ESTADO CONDITIONAL!!!!!")
        else:
            # TODO: Descrever melhor o erro do CONDITIONAL
            print("ERRO NO ESTADO CONDITIONAL!!!!!")

    def else_part(self):
        if self.tokens_list.lookahead().lexeme == 'else':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                self.code()
                if self.tokens_list.lookahead().lexeme == '}':
                    self.tokens_list.consume_token()
