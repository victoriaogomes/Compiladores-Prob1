from syntactic_analyzer import firsts_follows as f
import inspect
from copy import copy


class SyntacticAnalyzer:

    def __init__(self, tokens_list):
        self.tokens_list = tokens_list
        self.output_list = copy(tokens_list)

    def start(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            print("VAI PARA START")
            self.start()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            print("VAI PARA START")
            self.start()
        elif self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            print("VAI PARA HEADER 1")
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            print("VAI PARA HEADER 2")
            self.header2()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO INICIAL!!!!!")
            self.error_treatment('START', 'typedef ou struct ou var ou const ou function ou procedure')

    def header1(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            print("VAI PARA HEADER 1")
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            print("VAI PARA HEADER 1")
            self.header1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            print("VAI PARA HEADER 3")
            self.header3()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO HEADER1!!!!!")
            self.error_treatment('HEADER1', 'typedef ou struct ou const ou function ou procedure')

    def header2(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            print("VAI PARA HEADER 2")
            self.header2()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            print("VAI PARA HEADER 2")
            self.header2()
        elif self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            print("VAI PARA HEADER 3")
            self.header3()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO HEADER2!!!!!")
            self.error_treatment('HEADER2', 'typedef ou struct ou var ou function ou procedure')

    def header3(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
            print("VAI PARA HEADER 3")
            self.header3()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCT DECLARATION")
            self.structure_declaration()
            print("VAI PARA HEADER 3")
            self.header3()
        elif self.tokens_list.lookahead().lexeme in {'function', 'procedure'}:
            print("VAI PARA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO HEADER3!!!!!")
            self.error_treatment('HEADER3', 'typedef ou struct ou function ou procedure')

    def methods(self):
        if self.tokens_list.lookahead().lexeme == 'function':
            print("VAI PARA FUNCTION")
            self.function()
            print("VAI PARA METHODS")
            self.methods()
        elif self.tokens_list.lookahead().lexeme == 'procedure':
            self.tokens_list.consume_token()
            print("VAI PARA PROC CHOICE")
            self.proc_choice()
        else:
            print("ERRO NO ESTADO METHODS!!!!!")
            self.error_treatment('METHODS', 'function ou procedure')

    def proc_choice(self):
        if self.tokens_list.lookahead().lexeme == 'start':
            self.tokens_list.consume_token()
            print("VAI PRA START PROCEDURE")
            self.start_procedure()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PRA PROCEDURE")
            self.procedure()
            print("VAI PRA METHODS")
            self.methods()
        else:
            print("ERRO NO ESTADO PROC_CHOICE!!!!!")
            self.error_treatment('PROCCHOICE', 'start ou Identificador')

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
            self.error_treatment('VARIABLE', 'Identificador ou global ou local')

    def scope_variable(self):
        if self.tokens_list.lookahead().lexeme in {'global', 'local'}:
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '.':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme_type == 'IDE':
                    self.tokens_list.consume_token()
                    print("VAI PRA CONT ELEMENT")
                    self.cont_element()
                else:
                    print("ERRO NO ESTADO SCOPE Variable!!!!!")
                    self.error_treatment('SCOPEVARIABLE', 'Identificador')
            else:
                print("ERRO NO ESTADO SCOPE Variable!!!!!")
                self.error_treatment('SCOPEVARIABLE', '.')
        else:
            print("ERRO NO ESTADO SCOPE Variable!!!!!")
            self.error_treatment('SCOPEVARIABLE', 'global ou local')

    def vect_mat_index(self):
        if self.tokens_list.lookahead().lexeme in {'true', 'false', 'global', 'local', '('}:
            print("VAI PRA ARIT EXP 1")
            self.arit_exp1()
        elif self.tokens_list.lookahead().lexeme_type in {'NRO', 'IDE', 'CAD'}:
            print("VAI PRA ARIT EXP 1")
            self.arit_exp1()
        else:
            print("ERRO NO ESTADO vect mat index!!!!!")
            self.error_treatment('VECTMATINDEX',
                                 'true ou false ou global ou local ou ( ou Numero ou Identificador ou Cadeida de '
                                 'caracteres')

    def data_type(self):
        if self.tokens_list.lookahead().lexeme in {'int', 'string', 'real', 'boolean'}:
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO data type!!!!!")
            self.error_treatment('DATATYPE', 'int ou string ou real ou boolean ou Identificador')

    def cont_element(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PRA VECT MAT INDEX")
            self.vect_mat_index()
            if self.tokens_list.lookahead().lexeme == ']':
                self.tokens_list.consume_token()
                print("VAI PRA MATRIX E1")
                self.matrix_e1()
            else:
                print("ERRO EM CONT ELEMENT")
                self.error_treatment('CONTELEMENT', ']')
        else:
            print("VAI PRA MATRIX E 2")
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
                self.error_treatment('STRUCTE1', 'Identificador')
        else:
            print("ERRO NO ESTADO struct e1!!!!!")
            self.error_treatment('STRUCTE1', '.')

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
                self.error_treatment('MATRIZE1', ']')
        else:
            print("VAI PRA MATRIX E2")
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
                self.error_treatment('VARDECLARATION', '{')
        else:
            print("ERRO NO ESTADO VAR DECLARATION!!!!!")
            self.error_treatment('VARDECLARATION', 'var')

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
            self.error_treatment('FIRSTVAR', 'int ou real ou boolean ou struct ou Identificador')

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
            self.error_treatment('NEXTVAR', 'int ou real ou boolean ou struct ou string ou Identificador ou }')

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
            self.error_treatment('VARID', 'Identificador')

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
                self.error_treatment('VAREXP', ']')
        else:
            print("ERRO NO ESTADO VAR EX!!!!!")
            self.error_treatment('VAREXP', ', ou = ou ; ou [')

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
                self.error_treatment('STRUCTURE', ']')
        else:
            print("ERRO NO ESTADO STRUCTURE!!!!!")
            self.error_treatment('STRUCTURE', ', ou = ou ; ou {')

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
            self.error_treatment('CONTMATRIX', '= ou , ou ;')

    def init_array(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT ARRAY")
            self.next_array()
        else:
            print("ERRO NO ESTADO INIT ARRAY!!!!!")
            self.error_treatment('INITARRAY', '[')

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
            self.error_treatment('NEXTARRAY', ', ou ]')

    def init_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA MATRIZ VALUE")
            self.matrix_value()
        else:
            print("ERRO NO ESTADO INIT MATRIX!!!!!")
            self.error_treatment('INITMATRIX', '[')

    def matrix_value(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT MATRIX")
            self.next_matrix()
        else:
            print("ERRO NO ESTADO MATRIX VALUE!!!!!")
            self.error_treatment('MATRIXVALUE', '[')

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
            self.error_treatment('NEXTVALUE', ', ou ]')

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
            self.error_treatment('NEXT', ', ou ]')

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
            self.error_treatment('VERIFVAR', ', ou ;')

    def const_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                print("VAI PARA FIRST CONST")
                self.first_const()
            else:
                print("ERRO NO ESTADO CONST DECLARATION!!!!!")
                self.error_treatment('CONSTDECLARATION', '{')
        else:
            print("ERRO NO ESTADO CONST DECLARATION!!!!!")
            self.error_treatment('CONSTDECLARATION', 'const')

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
            print("ERRO NO ESTADO CONST ID!!!!!")
            self.error_treatment('CONSTID', 'Identificador')

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
                self.error_treatment('CONSTEXP', ']')

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
                    self.error_treatment('CONSTSTRUCTURE', '=')
            else:
                print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
                self.error_treatment('CONSTSTRUCTURE', ']')
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
                self.error_treatment('CONSTSTRUCTURE', '[')
        else:
            print("ERRO NO ESTADO CONST STRUCTURE!!!!!")
            self.error_treatment('CONSTSTRUCTURE', '] ou =')

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
            self.error_treatment('NEXTCONSTARRAY', ', ou ]')

    def init_const_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA MATRIX CONST VALUE")
            self.matrix_const_value()
        else:
            print("ERRO NO ESTADO INIT CONST MATRIX!!!!!")
            self.error_treatment('INITCONSTMATRIX', '[')

    def matrix_const_value(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA NEXT CONST MATRIX")
            self.next_const_matrix()
        else:
            print("ERRO NO ESTADO MATRIX CONST VALUE!!!!!")
            self.error_treatment('MATRIXCONSTVALUE', '[')

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
            self.error_treatment('NEXTCONSTMATRIX', ', ou ]')

    def next_const2(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA MATRIX CONST VALUE")
            self.matrix_const_value()
        elif self.tokens_list.lookahead().lexeme == ']':
            self.tokens_list.consume_token()
            print("VAI PARA VERIF CONST")
            self.verif_const()
        else:
            print("ERRO NO ESTADO NEXT CONST 2!!!!!")
            self.error_treatment('NEXTCONST2', ', ou ]')

    def verif_const(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA CONST ID")
            self.const_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT CONST")
            self.next_const()
        else:
            print("ERRO NO ESTADO VERIF CONST!!!!!")
            self.error_treatment('VERIFCONST', ', ou ;')

    def function(self):
        if self.tokens_list.lookahead().lexeme == 'function':
            self.tokens_list.consume_token()
            print("VAI PARA DATA TYPE")
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '(':
                    self.tokens_list.consume_token()
                    print("VAI PARA CONTINUE FUNCTION")
                    self.continue_function()
                else:
                    print("ERRO NO ESTADO FUNCTION!!!!!")
                    self.error_treatment('FUNCTION', '(')
            else:
                print("ERRO NO ESTADO FUNCTION!!!!!")
                self.error_treatment('FUNCTION', 'Identificador')
        else:
            print("ERRO NO ESTADO FUNCTION!!!!!")
            self.error_treatment('FUNCTION', 'function')

    def continue_function(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            print("VAI PARA BLOCK FUNCTION")
            self.block_function()
        elif self.tokens_list.lookahead().lexeme in {'int', 'real', 'string', 'boolean', 'struct'}:
            print("VAI PARA PARAMETERS")
            self.parameters()
            print("VAI PARA BLOCK FUNCTION")
            self.block_function()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PARA PARAMETERS")
            self.parameters()
            print("VAI PARA BLOCK FUNCTION")
            self.block_function()
        else:
            print("ERRO NO ESTADO CONTINUE FUNCTION!!!!!")
            self.error_treatment('CONTINUEFUNCTION', ') ou int ou real ou string ou boolean ou struct ou Identificador')

    def parameters(self):
        if self.tokens_list.lookahead().lexeme in {'int', 'real', 'string',
                                                   'boolean'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PARA DATA TYPE")
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                print("VAI PARA PARAM LOOP")
                self.param_loop()
            else:
                print("ERRO NO ESTADO PARAMETERS!!!!!")
                self.error_treatment('PARAMETERS', 'Identificador')
        elif self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            print("VAI PARA DATA TYPE")
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                print("VAI PARA PARAM LOOP")
                self.param_loop()
            else:
                print("ERRO NO ESTADO PARAMETERS!!!!!")
                self.error_treatment('PARAMETERS', 'Identificador')
        else:
            print("ERRO NO ESTADO PARAMETERS!!!!!")
            self.error_treatment('PARAMETERS', 'int ou real ou string ou boolean ou Identificador ou struct')

    def param_loop(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA PARAMETERS")
            self.parameters()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO PARAM LOOP!!!!!")
            self.error_treatment('PARAMLOOP', ', ou )')

    def block_function(self):
        if self.tokens_list.lookahead().lexeme == '{':
            self.tokens_list.consume_token()
            print("VAI PARA BLOCK FUNCTION CONTENT")
            self.block_function_content()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '}':
                    self.tokens_list.consume_token()
                else:
                    print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
                    self.error_treatment('BLOCKFUNCTION', '}')
            else:
                print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
                self.error_treatment('BLOCKFUNCTION', ';')
        else:
            print("ERRO NO ESTADO BLOCK FUNCTION!!!!!")
            self.error_treatment('BLOCKFUNCTION', '{')

    def block_function_content(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            print("VAI PARA CONTENT 1")
            self.content1()
        elif self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            print("VAI PARA CONTENT 2")
            self.content2()
        else:
            print("VAI PARA FUNCTION CONTENT")
            self.function_content()

    def function_content(self):
        print("VAI PARA CODE")
        self.code()
        if self.tokens_list.lookahead().lexeme == 'return':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
        else:
            print("ERRO NO ESTADO FUNCTION CONTENT!!!!!")
            self.error_treatment('FUNCTIONCONTENT', 'return')

    def content1(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            print("VAI PARA CONTENT 3")
            self.content3()
        else:
            print("VAI PARA FUNCTION CONTENT")
            self.function_content()

    def content2(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            print("VAI PARA CONTENT 3")
            self.content3()
        else:
            print("VAI PARA FUNCTION CONTENT")
            self.function_content()

    def content3(self):
        print("VAI PARA FUNCTION CONTENT")
        self.function_content()

    def structure_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'struct':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                print("VAI PARA STRUCT VARS")
                self.struct_vars()
            else:
                print("ERRO NO ESTADO STRUCTURE DECLARATION!!!!!")
                self.error_treatment('STRUCTUREDECLARATION', 'Identificador')
        else:
            print("ERRO NO ESTADO STRUCTURE DECLARATION!!!!!")
            self.error_treatment('STRUCTUREDECLARATION', 'struct')

    def struct_vars(self):
        if self.tokens_list.lookahead().lexeme == '{':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == 'var':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    print("VAI PARA FIRST STRUCT VAR")
                    self.first_struct_var()
                else:
                    print("ERRO NO ESTADO STRUCT VAR!!!!!")
                    self.error_treatment('STRUCTVAR', '{')
            else:
                print("ERRO NO ESTADO STRUCT VAR!!!!!")
                self.error_treatment('STRUCTVAR', 'var')
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
                            print("VAI PARA FISRT STRUCT VAR")
                            self.first_struct_var()
                        else:
                            print("ERRO NO ESTADO STRUCT VAR!!!!!")
                            self.error_treatment('STRUCTVAR', '{')
                    else:
                        print("ERRO NO ESTADO STRUCT VAR!!!!!")
                        self.error_treatment('STRUCTVAR', 'var')
                else:
                    print("ERRO NO ESTADO STRUCT VAR!!!!!")
                    self.error_treatment('STRUCTVAR', '{')
            else:
                print("ERRO NO ESTADO STRUCT VAR!!!!!")
                self.error_treatment('STRUCTVAR', 'Identificador')
        else:
            print("ERRO NO ESTADO STRUCT VAR!!!!!")
            self.error_treatment('STRUCTVAR', '{ ou extends')

    def first_struct_var(self):
        print("VAI PARA DATA TYPE")
        self.data_type()
        print("VAI PARA STRUCT VAR ID")
        self.struct_var_id()

    def struct_var_id(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            print("VAI PARA STRUCT VAR EXP")
            self.struct_var_exp()
        else:
            print("ERRO NO ESTADO STRUCT VAR ID!!!!!")
            self.error_treatment('STRUCTVARID', 'Identificador')

    def next_struct_var(self):
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO NEXT STRUCT VAR!!!!!")
                self.error_treatment('NEXTSTRUCTVAR', '}')
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PARA DATA TYPE")
            self.data_type()
            print("VAI PARA STRUCT VAR ID")
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme in {'int', 'real', 'string', 'boolean'}:
            print("VAI PARA DATA TYPE")
            self.data_type()
            print("VAI PARA STRUCT VAR ID")
            self.struct_var_id()
        else:
            print("ERRO NO ESTADO NEXT STRUCT VAR!!!!!")
            self.error_treatment('NEXTSTRUCTVAR', '} ou Identificador ou int ou real ou string ou boolean')

    def struct_var_exp(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA STRUCT VAR ID")
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT STRUCT VAR")
            self.next_struct_var()
        elif self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'NRO':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ']':
                    self.tokens_list.consume_token()
                    print("VAI PARA STRUCT MATRIX")
                    self.struct_matrix()
                else:
                    print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
                    self.error_treatment('STRUCTVAREXP', '}')
            else:
                print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
                self.error_treatment('STRUCTVAREXP', 'Numero')
        else:
            print("ERRO NO ESTADO STRUCT VAR EXP!!!!!")
            self.error_treatment('STRUCTVAREXP', ', ou ; ou [')

    def struct_matrix(self):
        if self.tokens_list.lookahead().lexeme == '[':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme_type == 'NRO':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ']':
                    self.tokens_list.consume_token()
                    print("VAI PARA CONT STRUCT MATRIX")
                    self.cont_struct_matrix()
                else:
                    print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
                    self.error_treatment('STRUCTMATRIX', ']')
            else:
                print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
                self.error_treatment('STRUCTMATRIX', 'Numero')
        elif self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA STRUCT VAR ID")
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT STRUCT VAR")
            self.next_struct_var()
        else:
            print("ERRO NO ESTADO STRUCT MATRIX!!!!!")
            self.error_treatment('STRUCTMATRIX', '[ ou , ou ;')

    def cont_struct_matrix(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA VAR ID")
            self.struct_var_id()
        elif self.tokens_list.lookahead().lexeme == ';':
            self.tokens_list.consume_token()
            print("VAI PARA NEXT STRUCT VAR")
            self.next_struct_var()
        else:
            print("ERRO NO ESTADO CONT STRUCT MATRIX!!!!!")
            self.error_treatment('CONTSTRUCTMATRIX', ', ou ;')

    def expression(self):
        if self.tokens_list.lookahead().lexeme == '!':
            self.tokens_list.consume_token()
            print("VAI PARA REL EXP")
            self.rel_exp()
            print("VAI PARA LOG EXP")
            self.log_exp()
        elif self.tokens_list.lookahead().lexeme in {'true', 'false', 'global', 'local', '('}:
            print("VAI PARA REL EXP")
            self.rel_exp()
            print("VAI PARA LOG EXP")
            self.log_exp()
        elif self.tokens_list.lookahead().lexeme_type in {'IDE', 'NRO', 'CAD'}:
            print("VAI PARA REL EXP")
            self.rel_exp()
            print("VAI PARA LOG EXP")
            self.log_exp()
        else:
            print("ERRO NO ESTADO EXPRESSION!!!!!")
            self.error_treatment('EXPRESSION',
                                 '! ou true ou false ou global ou local ou ( ou Numero ou Identificador ou Cadeira de '
                                 'Caracteres')

    def log_exp(self):
        if self.tokens_list.lookahead().lexeme in {'&&', '||'}:
            print("VAI PARA LOGIC SYMBOL")
            self.logic_symbol()
            print("VAI PARA REL EXP")
            self.rel_exp()
            print("VAI PARA LOG EXP")
            self.log_exp()

    def logic_symbol(self):
        if self.tokens_list.lookahead().lexeme in {'&&', '||'}:
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO LOGIC SYMBOL!!!!!")
            self.error_treatment('LOGICSYMBOL', '&& ou ||')

    def rel_exp(self):
        print("VAI PARA ARIT EXP 1")
        self.arit_exp1()
        print("VAI PARA REL EXP 2")
        self.rel_exp2()

    def rel_exp2(self):
        if self.tokens_list.lookahead().lexeme in {'>', '<', '==', '>=', '<='}:
            print("VAI PARA REL SYMBOL")
            self.rel_symbol()
            print("VAI PARA ARIT EXP 1")
            self.arit_exp1()
            print("VAI PARA REL EXP 2")
            self.rel_exp2()

    def rel_symbol(self):
        if self.tokens_list.lookahead().lexeme in {'>', '<', '==', '>=', '<='}:
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO REL SYMBOL!!!!!")
            self.error_treatment('RELSYMBOL', '> ou < ou == ou >= ou  <=')

    def arit_exp1(self):
        print("VAI PARA TERM")
        self.term()
        print("VAI PARA ARIT EXP 2")
        self.arit_exp2()

    def arit_exp2(self):
        if self.tokens_list.lookahead().lexeme in {'+', '-'}:
            print("VAI PARA ARIT SYMB 1")
            self.arit_symb1()
            print("VAI PARA TERM")
            self.term()
            print("VAI PARA ARIT EXP 2")
            self.arit_exp2()

    def arit_symb1(self):
        if self.tokens_list.lookahead().lexeme in {'+', '-'}:
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO ARIT SYMB 1!!!!!")
            self.error_treatment('ARITSYMB1', '+ ou  -')

    def term(self):
        print("VAI PARA OPERATE")
        self.operate()
        print("VAI PARA TERM 2")
        self.term2()

    def term2(self):
        if self.tokens_list.lookahead().lexeme in {'*', '/'}:
            print("VAI PARA ARIT SYMB 2")
            self.arit_symb2()
            print("VAI PARA OPERATE")
            self.operate()
            print("VAI PARA TERM 2")
            self.term2()

    def arit_symb2(self):
        if self.tokens_list.lookahead().lexeme in {'*', '/'}:
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO ARIT SYMB 2!!!!!")
            self.error_treatment('ARITSYMB2', '* ou /')

    def operate(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            if self.tokens_list.lookahead().lexeme == ')':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO OPERATE!!!!!")
                self.error_treatment('OPERATE', ')')
        elif self.tokens_list.lookahead().lexeme in {'true', 'false'}:
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type in {'NRO', 'CAD'}:
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            print("VAI PARA CONT OPERATE")
            self.cont_operate()
        elif self.tokens_list.lookahead().lexeme in {'global', 'local'}:
            print("VAI PARA SCOPE VARIABLE")
            self.scope_variable()
        else:
            print("ERRO NO ESTADO OPERATE!!!!!")
            self.error_treatment('OPERATE',
                                 '( ou true ou false ou glocal ou local ou Identificador ou Numero ou Cadeia de '
                                 'Caracteres')

    def cont_operate(self):
        if self.tokens_list.lookahead().lexeme == '(':
            print("VAI PARA FUNCTION CALL")
            self.function_call()
        else:
            print("VAI PARA CONT ELEMENT")
            self.cont_element()

    def typedef_declaration(self):
        if self.tokens_list.lookahead().lexeme == 'typedef':
            self.tokens_list.consume_token()
            print("VAI PARA CONT TYPEDEF DEC")
            self.cont_typedef_dec()
        else:
            print("ERRO NO ESTADO TYPEDEF DECLARATION!!!!!")
            self.error_treatment('TYPEDEFDECLARATION', 'typedef')

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
                        self.error_treatment('CONTTYPEDEFDEC', ';')
                else:
                    print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                    self.error_treatment('CONTTYPEDEFDEC', 'Identificador')
            else:
                print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                self.error_treatment('CONTTYPEDEFDEC', 'Identificador')
        elif self.tokens_list.lookahead().lexeme_type == 'IDE' or self.tokens_list.lookahead().lexeme in {
                'int', 'real', 'string', 'boolean'}:
            print("VAI PARA DATA TYPE")
            self.data_type()
            if self.tokens_list.lookahead().lexeme_type == 'IDE':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == ';':
                    self.tokens_list.consume_token()
                else:
                    print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                    self.error_treatment('CONTTYPEDEFDEC', ';')
            else:
                print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
                self.error_treatment('CONTTYPEDEFDEC', 'Identificador')
        else:
            print("ERRO NO ESTADO CONT TYPEDEF DEC!!!!!")
            self.error_treatment('CONTTYPEDEFDEC', 'struct ou int ou real ou string ou boolean ou Identificador')

    def start_procedure(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ')':
                self.tokens_list.consume_token()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    print("VAI PARA PROC CONTENT")
                    self.proc_content()
                else:
                    print("ERRO NO ESTADO START PROCEDURE!!!!!")
                    self.error_treatment('STARTPROCEDURE', '{')
            else:
                print("ERRO NO ESTADO START PROCEDURE!!!!!")
                self.error_treatment('STARTPROCEDURE', ')')
        else:
            print("ERRO NO ESTADO START PROCEDURE!!!!!")
            self.error_treatment('STARTPROCEDURE', '(')

    def procedure(self):
        if self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                print("VAI PARA PROC PARAM")
                self.proc_param()
                if self.tokens_list.lookahead().lexeme == '{':
                    self.tokens_list.consume_token()
                    print("VAI PARA PROC CONTENT")
                    self.proc_content()
                else:
                    print("ERRO NO ESTADO PROCEDURE!!!!!")
                    self.error_treatment('PROCEDURE', '{')
            else:
                print("ERRO NO ESTADO PROCEDURE!!!!!")
                self.error_treatment('PROCEDURE', '(')
        else:
            print("ERRO NO ESTADO PROCEDURE!!!!!")
            self.error_treatment('PROCEDURE', 'IDentificador')

    def proc_param(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme in {
                'struct', 'int', 'real', 'string', 'boolean'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PARA PARAMETERS")
            self.parameters()
        else:
            print("ERRO NO ESTADO PROC PARAM!!!!!")
            self.error_treatment('PROCPARAM', ') ou struct ou int ou real ou string ou boolean ou Identificador')

    def proc_content(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            print("VAI PARA PROC CONTENT 2")
            self.proc_content2()
        elif self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            print("VAI PARA PROC CONTENT")
            self.proc_content3()
        else:
            print("VAI PARA CODE")
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO PROC CONTENT!!!!!")
                self.error_treatment('PROCCONTENT', '}')

    def proc_content2(self):
        if self.tokens_list.lookahead().lexeme == 'const':
            print("VAI PARA CONST DECLARATION")
            self.const_declaration()
            print("VAI PARA PROC CONTENT 4")
            self.proc_content4()
        else:
            print("VAI PARA CODE")
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO PROC CONTENT2!!!!!")
                self.error_treatment('PROCCONTENT2', '}')

    def proc_content3(self):
        if self.tokens_list.lookahead().lexeme == 'var':
            print("VAI PARA VAR DECLARATION")
            self.var_declaration()
            print("VAI PARA PROC CONTENT")
            self.proc_content4()
        else:
            print("VAI PARA CODE")
            self.code()
            if self.tokens_list.lookahead().lexeme == '}':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO PROC CONTENT3!!!!!")
                self.error_treatment('PROCCONTENT3', '}')

    def proc_content4(self):
        print("VAI PARA CODE")
        self.code()
        if self.tokens_list.lookahead().lexeme == '}':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO PROC CONTENT4!!!!!")
            self.error_treatment('PROCCONTENT4', '}')

    def code(self):
        if self.tokens_list.lookahead().lexeme in {
            'global', 'local', 'struct', 'typedef', '++', '--', 'print', 'read', 'while',
                'if'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PARA COMMAND")
            self.command()
            print("VAI PARA CODE")
            self.code()

    def command(self):
        if self.tokens_list.lookahead().lexeme == 'print':
            print("VAI PARA PRINT FUNC")
            self.print_func()
        elif self.tokens_list.lookahead().lexeme_type == 'IDE':
            self.tokens_list.consume_token()
            print("VAI PARA OTHER COMMANDS")
            self.other_commands()
        elif self.tokens_list.lookahead().lexeme in {'global', 'local'}:
            print("VAI PARA SCOPE VARIABLES")
            self.scope_variable()
            print("VAI PARA OTHER COMMANDS")
            self.other_commands()
        elif self.tokens_list.lookahead().lexeme == 'read':
            print("VAI PARA READ")
            self.read()
        elif self.tokens_list.lookahead().lexeme == 'while':
            print("VAI PARA WHILE FUNC")
            self.while_func()
        elif self.tokens_list.lookahead().lexeme == 'if':
            print("VAI PARA CONDITIONAL")
            self.conditional()
        elif self.tokens_list.lookahead().lexeme == 'typedef':
            print("VAI PARA TYPEDEF DECLARATION")
            self.typedef_declaration()
        elif self.tokens_list.lookahead().lexeme == 'struct':
            print("VAI PARA STRUCTURE DECLARATION")
            self.structure_declaration()
        elif self.tokens_list.lookahead().lexeme in {'++', '--'}:
            self.tokens_list.consume_token()
            print("VAI PARA VARIABLE")
            self.variable()
        else:
            print("ERRO NO ESTADO COMMAND!!!!!")
            self.error_treatment('COMMAND',
                                 'print ou Identificador ou global ou local ou read ou while ou if ou typedef ou '
                                 'struct ou ++ ou --')

    def other_commands(self):
        if self.tokens_list.lookahead().lexeme == '(':
            print("VAI PARA FUNCTION CALL")
            self.function_call()
        else:
            print("VAI PARA CONT ELEMENT")
            self.cont_element()
            print("VAI PARA OTHER COMMANDS 2")
            self.other_commands2()

    def other_commands2(self):
        if self.tokens_list.lookahead().lexeme in {'++', '--'}:
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO OTHER COMMANDS2!!!!!")
                self.error_treatment('OTHERCOMMANDS2', ';')

        elif self.tokens_list.lookahead().lexeme == '=':
            print("VAI PARA ASSIGNMENT")
            self.assignment()
        else:
            print("ERRO NO ESTADO OTHER COMMANDS2!!!!!")
            self.error_treatment('OTHERCOMMANDS2', '++ ou -- ou =')

    def print_func(self):
        if self.tokens_list.lookahead().lexeme == 'print':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                print("VAI PARA PRINTABLE LIST")
                self.printable_list()
            else:
                print("ERRO NO ESTADO PRINT FUNC!!!!!")
                self.error_treatment('PRINTFUNC', '(')
        else:
            print("ERRO NO ESTADO PRINT FUNC!!!!!")
            self.error_treatment('PRINTFUNC', 'print')

    def printable_list(self):
        print("VAI PARA PRINTABLE")
        self.printable()
        print("VAI PARA NEXT PRINT VALUE")
        self.next_print_value()

    def printable(self):
        if self.tokens_list.lookahead().lexeme_type == 'CAD':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme in {
                'global', 'local'} or self.tokens_list.lookahead().lexeme_type == 'IDE':
            print("VAI PARA VARIABLE")
            self.variable()
        else:
            print("ERRO NO ESTADO PRINTABLE!!!!!")
            self.error_treatment('PRINTABLE', 'Cadeia de Caracteres ou global ou local ou identificador')

    def next_print_value(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA PRINTABLE LIST")
            self.printable_list()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO NEXT PRINT VALUE!!!!!")
                self.error_treatment('NEXTPRINTVALUE', ';')
        else:
            print("ERRO NO ESTADO NEXT PRINT VALUE!!!!!")
            self.error_treatment('NEXTPRINTVALUE', ', ou )')

    def assignment(self):
        if self.tokens_list.lookahead().lexeme == '=':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            if self.tokens_list.lookahead().lexeme == ';':
                self.tokens_list.consume_token()
            else:
                print("ERRO NO ESTADO ASSIGNMENT!!!!!")
                self.error_treatment('ASSIGNMENT', ';')
        else:
            print("ERRO NO ESTADO ASSIGNMENT!!!!!")
            self.error_treatment('ASSIGNMENT', '=')

    def function_call(self):
        if self.tokens_list.lookahead().lexeme == '(':
            self.tokens_list.consume_token()
            print("VAI PARA CONT F CALL")
            self.cont_f_call()
        else:
            print("ERRO NO ESTADO FUNCTION CALL!!!!!")
            self.error_treatment('FUNCTIONCALL', '(')

    def cont_f_call(self):
        if self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        elif self.tokens_list.lookahead().lexeme in {
            'true', 'false', 'global', 'local', '(', '!'} or self.tokens_list.lookahead().lexeme_type in {
                'NRO', 'IDE', 'CAD'}:
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA F CALL PARAMS")
            self.f_call_params()
        else:
            print("ERRO NO ESTADO CONT F CALL!!!!!")
            self.error_treatment('CONTFCALL',
                                 ') ou true ou false ou global ou local ou ( ou ! ou Numero ou Identificador ou '
                                 'Cadeia de Caracteres')

    def f_call_params(self):
        if self.tokens_list.lookahead().lexeme == ',':
            self.tokens_list.consume_token()
            print("VAI PARA EXPRESSION")
            self.expression()
            print("VAI PARA F CALL PARAMS")
            self.f_call_params()
        elif self.tokens_list.lookahead().lexeme == ')':
            self.tokens_list.consume_token()
        else:
            print("ERRO NO ESTADO F CALL PARAMS!!!!!")
            self.error_treatment('FCALLPARAMS', ', ou )')

    def read(self):
        if self.tokens_list.lookahead().lexeme == 'read':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '(':
                self.tokens_list.consume_token()
                print("VAI PARA READ PARAMS")
                self.read_params()
            else:
                print("ERRO NO ESTADO READ!!!!!")
                self.error_treatment('READ', '(')
        else:
            print("ERRO NO ESTADO READ!!!!!")
            self.error_treatment('READ', 'read')

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
                self.error_treatment('READLOOP', ';')
        else:
            print("ERRO NO ESTADO READ LOOP!!!!!")
            self.error_treatment('READLOOP', ', ou )')

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
                            self.error_treatment('WHILEFUNC', '}')
                    else:
                        print("ERRO NO ESTADO WHILE FUNC!!!!!")
                        self.error_treatment('WHILEFUNC', '{')
                else:
                    print("ERRO NO ESTADO WHILE FUNC!!!!!")
                    self.error_treatment('WHILEFUNC', ')')
            else:
                print("ERRO NO ESTADO WHILE FUNC!!!!!")
                self.error_treatment('WHILEFUNC', '(')
        else:
            print("ERRO NO ESTADO WHILE FUNC!!!!!")
            self.error_treatment('WHILEFUNC', 'while')

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
                                self.error_treatment('CONDITIONAL', '}')
                        else:
                            print("ERRO NO ESTADO CONDITIONAL!!!!!")
                            self.error_treatment('CONDITIONAL', '{')
                else:
                    print("ERRO NO ESTADO CONDITIONAL!!!!!")
                    self.error_treatment('CONDITIONAL', ')')
            else:
                print("ERRO NO ESTADO CONDITIONAL!!!!!")
                self.error_treatment('CONDITIONAL', '(')
        else:
            print("ERRO NO ESTADO CONDITIONAL!!!!!")
            self.error_treatment('CONDITIONAL', 'if')

    def else_part(self):
        if self.tokens_list.lookahead().lexeme == 'else':
            self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme == '{':
                self.tokens_list.consume_token()
                print("VAI PARA CODE")
                self.code()
                if self.tokens_list.lookahead().lexeme == '}':
                    self.tokens_list.consume_token()

    def error_treatment(self, state, expected_token):
        self.output_list.add_token('ERRO SINTATICO ESPERAVA: ' + expected_token
                                       + ' E RECEBI:', self.tokens_list.lookahead().lexeme,
                                       self.tokens_list.lookahead().file_line)
        state_firsts = f.FirstsFollows.getFirsts(state)
        print(str(self.tokens_list.lookahead().file_line) + ' ERRO SINTÁTICO ESPERAVA:', expected_token
              + ' E RECEBI:',
              self.tokens_list.lookahead().lexeme)
        state_follows = f.FirstsFollows.getFollows(state)
        print('FOLLOWS DESSE ESTADO:', state_follows)
        print('FIRSTS DESSE ESTADO:', state_firsts)
        if state == 'STRUCTVAREXP' or state == 'STRUCTMATRIX' or state == 'CONTSTRUCTMATRIX':
            self.next_struct_var()
        elif state == 'VAREXP' or state == 'STRUCTURE' or state == 'CONTMATRIX' or state == 'VERIFVAR':
            self.next_var()
        elif state == 'VERIFCONST':
            self.next_const()
        else:
            while self.tokens_list.lookahead().lexeme not in state_follows and self.tokens_list.lookahead().lexeme_type not in state_follows and self.tokens_list.lookahead().lexeme not in state_firsts and self.tokens_list.lookahead().lexeme_type not in state_follows and self.tokens_list.lookahead().lexeme != 'endOfFile($)':
                self.tokens_list.consume_token()
            if self.tokens_list.lookahead().lexeme in state_firsts or self.tokens_list.lookahead().lexeme_type in state_firsts:
                getattr(self, inspect.currentframe().f_back.f_code.co_name)()

        # elif self.tokens_list.lookahead().lexeme == '}' and (state.find('CONST') != -1 or state.find('VAR') != -1):
        #     print('CONSUMI }')
        #     self.tokens_list.consume_token()
        #     if state.find('STRUCT') != -1 and self.tokens_list.lookahead().lexeme == '}':
        #         print('CONSUMI DNV, ESTOU COM FOMI!')
        #         self.tokens_list.consume_token()

