from syntactic_analyzer import firsts_follows as f


class SyntacticAnalyzer:

    def __init__(self, tokens_list):
        self.tokens_list = tokens_list

    def start(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            self.start()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            self.start()
        elif self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            self.header2()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO INICIAL!!!!!")
            self.error_treatment('START')

    def header1(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            self.header3()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO HEADER1!!!!!")
            self.error_treatment('HEADER1')

    def header2(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            self.header2()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            self.header2()
        elif self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            self.header3()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO HEADER2!!!!!")
            self.error_treatment('HEADER2')

    def header3(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            self.header3()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            self.header3()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO HEADER3!!!!!")
            self.error_treatment('HEADER3')

    def methods(self):
        if self.tokens_list.lookahead().lexeme == 'function':
            print("VAI PARA FUNCTION")
            self.function()
            self.methods()
        elif self.tokens_list.lookahead().lexeme == 'procedure':
            self.tokens_list.consume_token()
            print("VAI PARA PROCEDURE CHOICE")
            self.proc_choice()
        else:
            print("ERRO NO ESTADO METHODS!!!!!")
            self.error_treatment('METHODS')

    def proc_choice(self):
        if self.tokens_list.lookahead().lexeme == 'start':
            self.tokens_list.consume_token()
            print("VAI PRA START PROCEDURE")
            self.start_procedure()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PRA PROCEDURE")
            self.procedure()
        else:
            print("ERRO NO ESTADO PROC_CHOICE!!!!!")
            self.error_treatment('PROCCHOICE')

    def variable(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            print("VAI PRA CONT ELEMENT")
            self.cont_element()
        elif self.tokens_list.lookahead().lexeme in {'global', 'local'}:
            print("VAI PRA SCOPE VARIABLE")
            self.scope_variable()
        else:
            print("ERRO NO ESTADO Variable!!!!!")
            self.error_treatment('VARIABLE')

    def scope_variable(self):
        if self.tokens_list.lookahead().lexeme in {'global', 'local'}:
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '.':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead.lexeme_type == 'IDE':
                    self.tokens_list.consume_token()
                    print("VAI PRA CONT ELEMENT")
                    self.cont_element()
                else:
                    print("ERRO NO ESTADO SCOPE Variable!!!!!")
                    self.error_treatment('SCOPEVARIABLE')
            else:
                print("ERRO NO ESTADO SCOPE Variable!!!!!")
                self.error_treatment('SCOPEVARIABLE')
        else:
            print("ERRO NO ESTADO SCOPE Variable!!!!!")
            self.error_treatment('SCOPEVARIABLE')

    def vect_mat_index(self):
        if self.tokens_list.lookahead().lexeme in {'true', 'false', 'global', 'local', '('}:
            print("VAI PRA ARIT EXP 1")
            self.arit_exp1()
        elif self.tokens_list.lookahead().lexeme_type in {'NRO', 'IDE', 'CAD'}:
            print("VAI PRA ARIT EXP 1")
            self.arit_exp1()
        else:
            print("ERRO NO ESTADO vect mat index!!!!!")
            self.error_treatment('VECTMATINDEX')

    def data_type(self):
        if self.tokens_list.lookahead().lexeme in {'int', 'string', 'real', 'boolean'}:
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO data type!!!!!")
            self.error_treatment('DATATYPE')

    def cont_element(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PRA vect mat index")
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                self.matrix_e1()
            else:
                print("ERRO EM CONT ELEMENT")
                self.error_treatment('CONTELEMENT')
        elif self.tokens_list.lookahead().lexeme == '.':
            print("VAI PRA MATRIZ E 2")
            self.matrix_e2()

    def struct_e1(self):
        if self.tokens_list.lookahead().lexeme == '.':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                print("VAI PRA CONT ELEMENT")
                self.cont_element()
            else:
                print("ERRO NO ESTADO struct e1!!!!!")
                self.error_treatment('STRUCTE1')
        else:
            print("ERRO NO ESTADO struct e1!!!!!")
            self.error_treatment('STRUCTE1')

    def matrix_e1(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PRA VECT MAT INDEX")
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                print("VAI PRA MATRIX E2")
                self.matrix_e2()
            else:
                print("ERRO NO ESTADO matrix e1!!!!!")
                self.error_treatment('MATRIZE1')
        else:
            self.matrix_e2()

    def matrix_e2(self):
        if self.tokens_list.lookahead().lexeme == '.':
            print("VAI PRA STRUCT E1")
            self.struct_e1()

    def var_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                print("VAI PRA FIRST VAR")
                self.first_var()
            else:
                print("ERRO NO ESTADO VAR DECLARATION!!!!!")
                self.error_treatment('VARDECLARATION')
        else:
            print("ERRO NO ESTADO VAR DECLARATION!!!!!")
            self.error_treatment('VARDECLARATION')

    def first_var(self):
        if self.tokens_list.lookahead().lexeme in {'int', 'real', 'boolean', 'struct'}:
            print("VAI PRA CONTINUE SOS")
            self.continue_sos()
            print("VAI PRA VAR ID")
            self.var_id()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PRA CONTINUE SOS")
            self.continue_sos()
            print("VAI PRA VAR ID")
            self.var_id()
        else:
            print("ERRO NO ESTADO FIRST VAR!!!!!")
            self.error_treatment('FIRSTVAR')

    def next_var(self):
        if self.tokens_list.lookahead().lexeme in {'int', 'real', 'boolean', 'struct', 'string'}:
            print("VAI PRA CONTINUE SOS")
            self.continue_sos()
            print("VAI PRA VAR ID")
            self.var_id()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PRA CONTINUE SOS")
            self.continue_sos()
            print("VAI PRA VAR ID")
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO NEXT VAR!!!!!")
            self.error_treatment('NEXTVAR')

    def continue_sos(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            print('VAI PRA DATATYPE')
            self.data_type()
        else:
            print('VAI PRA DATATYPE')
            self.data_type()

    def var_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            print('VAI PRA VAR EXP')
            self.var_exp()
        else:
            print("ERRO NO ESTADO VAR ID!!!!!")
            self.error_treatment('VARID')

    def var_exp(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print('VAI PRA VAR ID')
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            print('VAI PRA EXPRESSION')
            self.expression()
            print('VAI PRA VERIF VAR')
            self.verif_var()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print('VAI PRA NEXT VAR')
            self.next_var()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print('VAI PRA VECT MAT INDEX')
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                print('VAI PRA STRUCTURE')
                self.structure()
            else:
                print("ERRO NO ESTADO VAR EXP!!!!!")
                self.error_treatment('VAREXP')
        else:
            print("ERRO NO ESTADO VAR EX!!!!!")
            self.error_treatment('VAREXP')

    def structure(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print('VAI PRA VAR ID')
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            print('VAI PRA INIT ARRAY')
            self.init_array()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print('VAI PRA NEXT VAR')
            self.next_var()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                print('VAI PRA CONT MATRIX')
                self.cont_matrix()
            else:
                print("ERRO NO ESTADO STRUCTURE!!!!!")
                self.error_treatment('STRUCTURE')
        else:
            print("ERRO NO ESTADO STRUCTURE!!!!!")
            self.error_treatment('STRUCTURE')

    def cont_matrix(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            print('VAI PRA INIT MATRIX')
            self.init_matrix()
        elif self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print('VAI PRA VAR ID')
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print('VAI PRA EXPRESSION')
            self.next_var()
        else:
            print("ERRO NO CONT MATRIX!!!!!")
            self.error_treatment('CONTMATRIX')

    def init_array(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT ARRAY")
            self.next_array()
        else:
            print("ERRO NO ESTADO INIT ARRAY!!!!!")
            self.error_treatment('INITARRAY')

    def next_array(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT ARRAY")
            self.next_array()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            print("VAI PARA VERIF VAR")
            self.verif_var()
        else:
            print("ERRO NO ESTADO NEXT ARRAY!!!!!")
            self.error_treatment('NEXTARRAY')

    def init_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA MATRIZ VALUE")
            self.matrix_value()
        else:
            print("ERRO NO ESTADO INIT MATRIX!!!!!")
            self.error_treatment('INITMATRIX')

    def matrix_value(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT MATRIX")
            self.next_matrix()
        else:
            print("ERRO NO ESTADO MATRIX VALUE!!!!!")
            self.error_treatment('MATRIXVALUE')

    def next_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT MATRIX")
            self.next_matrix()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT")
            self.next()
        else:
            print("ERRO NO ESTADO NEXT MATRIX!!!!!")
            self.error_treatment('NEXTVALUE')

    def next(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA MATRIX VALUE")
            self.matrix_value()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.verif_var()
        else:
            print("ERRO NO ESTADO NEXT!!!!!")
            self.error_treatment('NEXT')

    def verif_var(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA VAR ID")
            self.var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT VAR")
            self.next_var()
        else:
            print("ERRO NO ESTADO VERIF VAR!!!!!")
            self.error_treatment('VERIFVAR')

    def const_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                print("VAI PARA FIRST CONST")
                self.first_const()
            else:
                print("ERRO NO ESTADO CONST DECLARATION!!!!!")
                self.error_treatment('CONSTDECLARATION')
        else:
            print("ERRO NO ESTADO CONST DECLARATION!!!!!")
            self.error_treatment('CONSTDECLARATION')

    def first_const(self):
        print("VAI PARA CONTINUE CONST SOS")
        self.continue_const_sos()
        print("VAI PARA CONST ID")
        self.const_id()

    def continue_const_sos(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            print("VAI PARA DATA TYPE")
            self.data_type()
        else:
            print("VAI PARA DATA TYPE")
            self.data_type()

    def next_const(self):
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            print("VAI PARA CONTINUE CONST SOS")
            self.continue_const_sos()
            print("VAI PARA CONST ID")
            self.const_id()

    def const_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            print("VAI PARA CONST EXP")
            self.const_exp()
        else:
            self.error_treatment('CONSTID')
            print("ERRO NO ESTADO CONST ID!!!!!")

    def const_exp(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA VERIF CONST")
            self.verif_const()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA VECT MAT INDEX")
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                print("VAI PARA CONT STRUCTURE")
                self.const_structure()
            else:
                print("ERRO NO ESTADO CONST EXP!!!!!")
                self.error_treatment('CONSTEXP')

    def const_structure(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA VECT MAT INDEX")
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '=':
                    self.tokens_list.consume_token()
                    print("VAI PARA INIT CONST MATRIX")
                    self.init_const_matrix()
                else:
                    print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
                    self.error_treatment('CONSTSTRUCTURE')
            else:
                print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
                self.error_treatment('CONSTSTRUCTURE')
        elif self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '[':
                self.tokens_list.consume_token()
                print("VAI PARA EXPRESSION")
                self.expression()
                print("VAI PARA NEXT CONST ARRAY")
                self.next_const_array()
            else:
                print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
                self.error_treatment('CONSTSTRUCTURE')
        else:
            print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
            self.error_treatment('CONSTSTRUCTURE')

    def next_const_array(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT CONST ARRAY")
            self.next_const_array()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            print("VAI PARA VERIF CONST")
            self.verif_const()
        else:
            print("ERRO NO ESTADO NEXT CONST ARRAY!!!!!")
            self.error_treatment('CONSTARRAY')

    def init_const_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA MATRIX CONST VALUE")
            self.matrix_const_value()
        else:
            print("ERRO NO ESTADO INIT CONST MATRIX!!!!!")
            self.error_treatment('CONSTMATRIX')

    def matrix_const_value(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT CONST MATRIX")
            self.next_const_matrix()
        else:
            print("ERRO NO ESTADO MATRIX CONST VALUE!!!!!")
            self.error_treatment('CONSTVALUE')

    def next_const_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT CONST MATRIX")
            self.next_const_matrix()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT CONST 2")
            self.next_const2()
        else:
            print("ERRO NO ESTADO NEXT CONST MATRIX!!!!!")
            self.error_treatment('NEXTCONSTMATRIX')

    def next_const2(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.matrix_const_value()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            self.verif_const()
        else:
            print("ERRO NO ESTADO NEXT CONST 2!!!!!")
            self.error_treatment('NEXTCONST2')

    def verif_const(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.const_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_const()
        else:
            print("ERRO NO ESTADO VERIF CONST!!!!!")
            self.error_treatment('VERIFCONST')

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
                    print("ERRO NO ESTADO FUNCTION!!!!!")
                    self.error_treatment('FUNCTION')
            else:
                print("ERRO NO ESTADO FUNCTION!!!!!")
                self.error_treatment('FUNCTION')
        else:
            print("ERRO NO ESTADO FUNCTION!!!!!")
            self.error_treatment('FUNCTION')

    def continue_function(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            self.block_function()
        elif self.tokens_list.lookahead().lexeme in {'int', 'real', 'string', 'boolean', 'struct'}:
            self.parameters()
            self.block_function()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.parameters()
            self.block_function()
        else:
            print("ERRO NO ESTADO CONTINUE FUNCTION!!!!!")
            self.error_treatment('CONTINUEFUNCTION')

    def parameters(self):
        if self.tokens_list.lookahead().lexeme in {'int', 'real', 'string',
                                                   'boolean'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                self.param_loop()
            else:
                print("ERRO NO ESTADO PARAMETERS!!!!!")
                self.error_treatment('PARAMETERS')
        elif self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                self.param_loop()
            else:
                print("ERRO NO ESTADO PARAMETERS!!!!!")
                self.error_treatment('PARAMETERS')
        else:
            print("ERRO NO ESTADO PARAMETERS!!!!!")
            self.error_treatment('PARAMETERS')

    def param_loop(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.parameters()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO PARAM LOOP!!!!!")
            self.error_treatment('PARAMLOOP')

    def block_function(self):
        if self.tokens_list.lookahead().lexeme == '{':
            self.tokens_list.consume_token()
            self.block_function_content()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '}':
                    self.tokens_list.consume_token()
                else:
                    print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
                    self.error_treatment('BLOCKFUNCTION')
            else:
                print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
                self.error_treatment('BLOCKFUNCTION')
        else:
            print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
            self.error_treatment('BLOCKFUNCTION')

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
            print("ERRO NO ESTADO FUNCTION CONTENT!!!!!")
            self.error_treatment('FUNCTIONCONTENT')

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
                print("ERRO NO ESTADO STRUCTURE DECLARATION!!!!!")
                self.error_treatment('STRUCTUREDECLARATION')
        else:
            # TODO: Descrever melhor o erro do STRUCTURE DECLARATION
            print("ERRO NO ESTADO STRUCTURE DECLARATION!!!!!")
            self.error_treatment('STRUCTUREDECLARATION')

    def struct_vars(self):
        if self.tokens_list.lookahead().lexeme == '{':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == 'var':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    self.first_struct_var()
                else:
                    print("ERRO NO ESTADO STRUCT VAR!!!!!")
                    self.error_treatment('STRUCTVAR')
            else:
                print("ERRO NO ESTADO STRUCT VAR!!!!!")
                self.error_treatment('STRUCTVAR')
        elif self.tokens_list.lookahead().lexeme == 'extends':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == 'var':
                        self.tokens_list.consume_token()
                        if self.tokens_list.lookahead().lexeme == '{':
                            self.tokens_list.consume_token()
                            self.first_struct_var()
                        else:
                            print("ERRO NO ESTADO STRUCT VAR!!!!!")
                            self.error_treatment('STRUCTVAR')
                    else:
                        print("ERRO NO ESTADO STRUCT VAR!!!!!")
                        self.error_treatment('STRUCTVAR')
                else:
                    print("ERRO NO ESTADO STRUCT VAR!!!!!")
                    self.error_treatment('STRUCTVAR')
            else:
                print("ERRO NO ESTADO STRUCT VAR!!!!!")
                self.error_treatment('STRUCTVAR')
        else:
            print("ERRO NO ESTADO STRUCT VAR!!!!!")
            self.error_treatment('STRUCTVAR')

    def first_struct_var(self):
        self.data_type()
        self.struct_var_id()

    def struct_var_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.struct_var_exp()
        else:
            print("ERRO NO ESTADO STRUCT VAR ID!!!!!")
            self.error_treatment('STRUCTVARID')

    def next_struct_var(self):
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO NEXT STRUCT VAR!!!!!")
                self.error_treatment('NEXTSTRUCTVAR')
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.data_type()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme in {'int', 'real', 'string', 'boolean'}:
            self.data_type()
            self.struct_var_id()
        else:
            print("ERRO NO ESTADO NEXT STRUCT VAR!!!!!")
            self.error_treatment('NEXTSTRUCTVAR')

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
                    print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
                    self.error_treatment('STRUCTVAREXP')
            else:
                print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
                self.error_treatment('STRUCTVAREXP')
        else:
            print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
            self.error_treatment('STRUCTVAREXP')

    def struct_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'NRO':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ']':
                    self.tokens_list.consume_token()
                    self.cont_struct_matrix()
                else:
                    print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
                    self.error_treatment('STRUCTMATRIX')
            else:
                print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
                self.error_treatment('STRUCTMATRIX')
        elif self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_struct_var()
        else:
            print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
            self.error_treatment('STRUCTMATRIX')

    def cont_struct_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            self.next_struct_var()
        else:
            print("ERRO NO ESTADO CONT STRUCT MATRIX!!!!!")
            self.error_treatment('CONTSTRUCTMATRIX')

    def expression(self):
        if self.tokens_list.lookahead().lexeme == '!':
            self.tokens_list.consume_token()
            self.rel_exp()
            self.log_exp()
        elif self.tokens_list.lookahead().lexeme in {'true', 'false', 'global', 'local', '('}:
            self.rel_exp()
            self.log_exp()
        elif self.tokens_list.lookahead().lexeme_type in {'IDE', 'NRO', 'CAD'}:
            self.rel_exp()
            self.log_exp()
        else:
            print("ERRO NO ESTADO EXPRESSION!!!!!")
            self.error_treatment('EXPRESSION')

    def log_exp(self):
        if self.tokens_list.lookahead().lexeme in {'&&', '||'}:
            self.logic_symbol()
            self.rel_exp()
            self.log_exp()

    def logic_symbol(self):
        if self.tokens_list.lookahead().lexeme == ('&&' or '||'):
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO LOGIC SYMBOL!!!!!")
            self.error_treatment('LOGICSYMBOL')

    def rel_exp(self):
        self.arit_exp1()
        self.rel_exp2()

    def rel_exp2(self):
        if self.tokens_list.lookahead().lexeme in {'>', '<', '==', '>=', '<='}:
            self.rel_symbol()
            self.arit_exp1()
            self.rel_exp2()

    def rel_symbol(self):
        if self.tokens_list.lookahead().lexeme in {'>', '<', '==', '>=', '<='}:
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO REL SYMBOL!!!!!")
            self.error_treatment('RELSYMBOL')

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
            print("ERRO NO ESTADO ARIT SYMB 1!!!!!")
            self.error_treatment('ARITSYMB1')

    def term(self):
        self.operate()
        self.term2()

    def term2(self):
        if self.tokens_list.lookahead().lexeme in {'*', '/'}:
            self.arit_symb2()
            self.operate()
            self.term2()

    def arit_symb2(self):
        if self.tokens_list.lookahead().lexeme in {'*', '/'}:
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO ARIT SYMB 2!!!!!")
            self.error_treatment('ARITSYMB2')

    def operate(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            self.expression()
            if self.tokens_list.lookahead().lexeme == ')':
                self.tokens_list.consume_token()
            else:
                # TODO: Descrever melhor o erro do OPERATE
                print("ERRO NO ESTADO OPERATE!!!!!")
        elif self.tokens_list.lookahead().lexeme in {'true', 'false'}:
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type in {'NRO', 'CAD'}:
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.cont_operate()
        elif self.tokens_list.lookahead().lexeme in {'global', 'local'}:
            self.scope_variable()
        else:
            print("ERRO NO ESTADO OPERATE!!!!!")
            self.error_treatment('OPERATE')

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
            print("ERRO NO ESTADO TYPEDEF DECLARATION!!!!!")
            self.error_treatment('TYPEDEFDECLARATION')

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
                        print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                        self.error_treatment('CONTTYPEDEFDEC')
                else:
                    print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                    self.error_treatment('CONTTYPEDEFDEC')
            else:
                print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                self.error_treatment('CONTTYPEDEFDEC')
        elif self.tokens_list.lookahead().lexeme_type == 'IDE' or self.tokens_list.lookahead().lexeme in {
                'int', 'real', 'string', 'boolean'}:
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ';':
                    self.tokens_list.consume_token()
                else:
                    print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                    self.error_treatment('CONTTYPEDEFDEC')
            else:
                print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                self.error_treatment('CONTTYPEDEFDEC')
        else:
            print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
            self.error_treatment('CONTTYPEDEFDEC')

    def start_procedure(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ')':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    self.proc_content()
                else:
                    print("ERRO NO ESTADO START PROCEDURE!!!!!")
                    self.error_treatment('STARTPROCEDURE')
            else:
                print("ERRO NO ESTADO START PROCEDURE!!!!!")
                self.error_treatment('STARTPROCEDURE')
        else:
            print("ERRO NO ESTADO START PROCEDURE!!!!!")
            self.error_treatment('STARTPROCEDURE')

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
                    print("ERRO NO ESTADO PROCEDURE!!!!!")
                    self.error_treatment('PROCEDURE')
            else:
                print("ERRO NO ESTADO PROCEDURE!!!!!")
                self.error_treatment('PROCEDURE')
        else:
            print("ERRO NO ESTADO PROCEDURE!!!!!")
            self.error_treatment('PROCEDURE')

    def proc_param(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme in {
                'struct', 'int', 'real', 'string', 'boolean'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.parameters()
        else:
            print("ERRO NO ESTADO PROC PARAM!!!!!")
            self.error_treatment('PROCPARAM')

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
                print("ERRO NO ESTADO PROC CONTENT!!!!!")
                self.error_treatment('PROCCONTENT')

    def proc_content2(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            self.const_declaration()
            self.proc_content4()
        else:
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO PROC CONTENT2!!!!!")
                self.error_treatment('PROCCONTENT2')

    def proc_content3(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            self.var_declaration()
            self.proc_content4()
        else:
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO PROC CONTENT3!!!!!")
                self.error_treatment('PROCCONTENT3')

    def proc_content4(self):
        self.code()
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO PROC CONTENT4!!!!!")
            self.error_treatment('PROCCONTENT4')

    def code(self):
        if self.tokens_list.lookahead().lexeme in {
            'global', 'local', 'struct', 'typedef', '++', '--', 'print', 'read', 'while',
                'if'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.command()
            self.code()

    def command(self):
        if self.tokens_list.lookahead().lexeme == 'print':
            self.print_func()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            self.other_commands()
        elif self.tokens_list.lookahead().lexeme in {'global', 'local'}:
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
        elif self.tokens_list.lookahead().lexeme in {'++', '--'}:
            self.tokens_list.consume_token()
            self.variable()
        else:
            print("ERRO NO ESTADO COMMAND!!!!!")
            self.error_treatment('COMMAND')

    def other_commands(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.function_call()
        else:
            self.cont_element()
            self.other_commands2()

    def other_commands2(self):
        if self.tokens_list.lookahead().lexeme in {'++', '--'}:
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO OTHER COMMANDS2!!!!!")

        elif self.tokens_list.lookahead().lexeme == '=':
            self.assignment()
        else:
            print("ERRO NO ESTADO OTHER COMMANDS2!!!!!")
            self.error_treatment('OTHERCOMMANDS2')

    def print_func(self):
        if self.tokens_list.lookahead().lexeme == 'print':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.printable_list()
            else:
                print("ERRO NO ESTADO PRINT FUNC!!!!!")
                self.error_treatment('PRINTFUNC')
        else:
            print("ERRO NO ESTADO PRINT FUNC!!!!!")
            self.error_treatment('PRINTFUNC')

    def printable_list(self):
        self.printable()
        self.next_print_value()

    def printable(self):
        if self.tokens_list.lookahead().lexeme_type == 'CAD':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme in {
                'global', 'local'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.variable()
        else:
            print("ERRO NO ESTADO PRINTABLE!!!!!")
            self.error_treatment('PRINTABLE')

    def next_print_value(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.printable_list()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO NEXT PRINT VALUE!!!!!")
                self.error_treatment('NEXTPRINTVALUE')
        else:
            print("ERRO NO ESTADO NEXT PRINT VALUE!!!!!")
            self.error_treatment('NEXTPRINTVALUE')

    def assignment(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            self.expression()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO ASSIGNMENT!!!!!")
                self.error_treatment('ASSIGNMENT')
        else:
            print("ERRO NO ESTADO ASSIGNMENT!!!!!")
            self.error_treatment('ASSIGNMENT')

    def function_call(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            self.cont_f_call()
        else:
            print("ERRO NO ESTADO FUNCTION CALL!!!!!")
            self.error_treatment('FUNCTIONCALL')

    def cont_f_call(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme in {
            'true', 'false', 'global', 'local', '(', '!'} or self.tokens_list.lookahead().lexeme_type in {
                'NRO', 'IDE', 'CAD'}:
            self.expression()
            self.f_call_params()
        else:
            print("ERRO NO ESTADO CONT F CALL!!!!!")
            self.error_treatment('CONTFCALL')

    def f_call_params(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            self.expression()
            self.f_call_params()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO F CALL PARAMS!!!!!")
            self.error_treatment('FCALLPARAMS')

    def read(self):
        if self.tokens_list.lookahead().lexeme == 'read':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                self.read_params()
            else:
                print("ERRO NO ESTADO READ!!!!!")
                self.error_treatment('READ')
        else:
            print("ERRO NO ESTADO READ!!!!!")
            self.error_treatment('READ')

    def read_params(self):
        print("VAI PARA VARIABLE")
        self.variable()
        print("VAI PARA READ LOOP")
        self.read_loop()

    def read_loop(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA READ PARAMS")
            self.read_params()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO READ LOOP!!!!!")
                self.error_treatment('READLOOP')
        else:
            print("ERRO NO ESTADO READ LOOP!!!!!")
            self.error_treatment('READLOOP')

    def while_func(self):
        if self.tokens_list.lookahead().lexeme == 'while':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                print("VAI PARA EXPRESSION")
                self.expression()
                if self.tokens_list.lookahead().lexeme == ')':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == '{':
                        self.tokens_list.consume_token()
                        print("VAI PARA CODE")
                        self.code()
                        if self.tokens_list.lookahead().lexeme == '}':
                            self.tokens_list.consume_token()
                        else:
                            print("ERRO NO ESTADO WHILE FUNC!!!!!")
                            self.error_treatment('WHILEFUNC')
                    else:
                        print("ERRO NO ESTADO WHILE FUNC!!!!!")
                        self.error_treatment('WHILEFUNC')
                else:
                    print("ERRO NO ESTADO WHILE FUNC!!!!!")
                    self.error_treatment('WHILEFUNC')
            else:
                print("ERRO NO ESTADO WHILE FUNC!!!!!")
                self.error_treatment('WHILEFUNC')
        else:
            print("ERRO NO ESTADO WHILE FUNC!!!!!")
            self.error_treatment('WHILEFUNC')

    def conditional(self):
        if self.tokens_list.lookahead().lexeme == 'if':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                print("VAI PARA EXPRESSION")
                self.expression()
                if self.tokens_list.lookahead().lexeme == ')':
                    self.tokens_list.consume_token()
                    if self.tokens_list.lookahead().lexeme == 'then':
                        self.tokens_list.consume_token()
                        if self.tokens_list.lookahead().lexeme == '{':
                            self.tokens_list.consume_token()
                            print("VAI PARA CODE")
                            self.code()
                            if self.tokens_list.lookahead().lexeme == '}':
                                self.tokens_list.consume_token()
                                print("VAI PARA ELSE PART")
                                self.else_part()
                            else:
                                print("ERRO NO ESTADO CONDITIONAL!!!!!")
                                self.error_treatment('CONDITIONAL')
                        else:
                            print("ERRO NO ESTADO CONDITIONAL!!!!!")
                            self.error_treatment('CONDITIONAL')
                else:
                    print("ERRO NO ESTADO CONDITIONAL!!!!!")
                    self.error_treatment('CONDITIONAL')
            else:
                print("ERRO NO ESTADO CONDITIONAL!!!!!")
                self.error_treatment('CONDITIONAL')
        else:
            print("ERRO NO ESTADO CONDITIONAL!!!!!")
            self.error_treatment('CONDITIONAL')

    def else_part(self):
        if self.tokens_list.lookahead().lexeme == 'else':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                print("VAI PARA CODE")
                self.code()
                if self.tokens_list.lookahead().lexeme == '}':
                    self.tokens_list.consume_token()

    def error_treatment(self, state):
        state_firsts = f.FirstsFollows.getFirsts(state)
        print(str(self.tokens_list.lookahead().file_line) + ' ERRO: esperava um dos seguintes tokens: ', ''.join(state_firsts)
              + '. RECEBI: ',
              self.tokens_list.lookahead().lexeme)
        state_follows = f.FirstsFollows.getFollows(state)
        while self.tokens_list.lookahead().lexeme not in state_follows and self.tokens_list.lookahead().lexeme != 'endOfFile($)':
            self.tokens_list.consume_token()
