class FirstsFollows:

    def __init__(self):
        print('FIRST FOLLOW CLASS')

    @staticmethod
    def getFollows(state):
        follows = {
            'START': ['endOfFile($)'],
            'HEADER1': ['endOfFile($)'],
            'HEADER2': ['endOfFile($)'],
            'HEADER3': ['endOfFile($)'],
            'METHODS': ['endOfFile($)'],
            'PROCCHOICE': ['endOfFile($)'],
            'VARIABLE': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                         'return', '}', ',', ')'],
            'SCOPEVARIABLE': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', '[', '(', '.',
                              '++', '--', '=', 'IDE', 'global', 'local', 'typedef', 'struct', 'print', 'read', 'while',
                              'if', 'return', '}', ')'],
            'VECTMATINDEX': [']'],
            'DATATYPE': ['IDE'],
            'CONTELEMENT': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', '++', '--', '=',
                            'IDE', 'global', 'local', 'typedef', 'struct', 'print', 'read', 'while', 'if', 'return',
                            '}', ')', '[', '(', '.'],
            'STRUCTE1': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', '++', '--', '=',
                         'IDE', 'global', 'local', 'typedef', 'struct', 'print', 'read', 'while', 'if', 'return', '}',
                         ')', '[', '(', '.'],
            'MATRIZE1': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', '++', '--', '=',
                         'IDE', 'global', 'local', 'typedef', 'struct', 'print', 'read', 'while', 'if', 'return', '}',
                         ')', '[', '(', '.'],
            'MATRIZE2': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', '++', '--', '=',
                         'IDE', 'global', 'local', 'typedef', 'struct', 'print', 'read', 'while', 'if', 'return', '}',
                         ')', '[', '(', '.'],
            'VARDECLARATION': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global',
                               'local', '++', '--', 'print', 'read', 'while', 'if', '}'],
            'FIRSTVAR': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                         '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXTVAR': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                        '--', 'print', 'read', 'while', 'if', '}'],
            'CONTINUESOS': ['IDE'],
            'VARID': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                      '--', 'print', 'read', 'while', 'if', '}'],
            'VAREXP': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                       '--', 'print', 'read', 'while', 'if', '}'],
            'STRUCTURE': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                          '++', '--', 'print', 'read', 'while', 'if', '}'],
            'CONTMATRIX': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                           '++', '--', 'print', 'read', 'while', 'if', '}'],
            'INITARRAY': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                          '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXTARRAY': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                          '++', '--', 'print', 'read', 'while', 'if', '}'],
            'INITMATRIX': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                           '++', '--', 'print', 'read', 'while', 'if', '}'],
            'MATRIXVALUE': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                            '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXTMATRIX': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                           '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXT': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                     '--', 'print', 'read', 'while', 'if', '}'],
            'VERIFVAR': ['typedef', 'struct', 'const', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                         '++', '--', 'print', 'read', 'while', 'if', '}'],
            'CONSTDECLARATION': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global',
                                 'local', '++', '--', 'print', 'read', 'while', 'if', '}'],
            'FIRSTCONST': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                           '++', '--', 'print', 'read', 'while', 'if', '}'],
            'CONTINUECONSTSOS': ['IDE'],
            'NEXTCONST': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                          '--', 'print', 'read', 'while', 'if', '}'],
            'CONSTID': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                        '--', 'print', 'read', 'while', 'if', '}'],
            'CONSTEXP': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local', '++',
                         '--', 'print', 'read', 'while', 'if', '}'],
            'STRUCTURECONST': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                               '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXTCONSTVETOR': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                               '++', '--', 'print', 'read', 'while', 'if', '}'],
            'INITCONSTMATRIX': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                                '++', '--', 'print', 'read', 'while', 'if', '}'],
            'MATRIXCONSTVALUE': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global',
                                 'local', '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXTCONSTMATRIZ': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                                '++', '--', 'print', 'read', 'while', 'if', '}'],
            'NEXTCONST2': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                           '++', '--', 'print', 'read', 'while', 'if', '}'],
            'VERIFCONST': ['typedef', 'struct', 'var', 'procedure', 'function', 'return', 'IDE', 'global', 'local',
                           '++', '--', 'print', 'read', 'while', 'if', '}'],
            'FUNCTION': ['procedure', 'function'],
            'CONTINUEFUNCTION': ['procedure', 'function'],
            'PARAMETERS': ['{'],
            'PARAMLOOP': ['{'],
            'BLOCKFUNCTION': ['procedure', 'function'],
            'BLOCKFUNCTIONCONTENT': [';'],
            'FUNCTIONCONTENT': [';'],
            'CONTENT1': [';'],
            'CONTENT2': [';'],
            'CONTENT3': [';'],
            'STRUCTUREDECLARATION': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global',
                                     'local', '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'STRUCTVARS': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local', '++',
                           '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'FIRSTSTRUCTVAR': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                               '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'STRUCTVARID': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                            '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'NEXTSTRUCTVAR': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                              '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'STRUCTVAREXP': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                             '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'STRUCTMATRIX': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                             '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'CONTSTRUCTMATRIX': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                                 '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'EXPRESSION': [',', ';', ']', ')'],
            'LOGEXP': [',', ';', ']', ')'],
            'LOGICSYMBOL': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'RELEXP': ['&&', '||', ',', ';', ']', ')'],
            'RELEXP2': ['&&', '||', ',', ';', ']', ')'],
            'RELSYMBOL': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'ARITEXP1': ['>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', ')'],
            'ARITEXP2': ['>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', ')'],
            'ARITSYMB1': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'TERM': ['+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', ')'],
            'TERM2': ['+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', ')'],
            'ARITSYMB2': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'OPERATE': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', ')'],
            'CONTOPERATE': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', ')'],
            'TYPEDEFDECLARATION': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global',
                                   'local', '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'CONTTYPEDEFDEC': ['typedef', 'struct', 'var', 'const', 'procedure', 'function', 'IDE', 'global', 'local',
                               '++', '--', 'print', 'read', 'while', 'if', 'return', '}'],
            'STARTPROCEDURE': ['endOfFile($)'],
            'PROCEDURE': ['procedure', 'function'],
            'PROCPARAM': ['{'],
            'PROCCONTENT': ['endOfFile($)', 'procedure', 'function'],
            'PROCCONTENT2': ['endOfFile($)', 'procedure', 'function'],
            'PROCCONTENT3': ['endOfFile($)', 'procedure', 'function'],
            'PROCCONTENT4': ['endOfFile($)', 'procedure', 'function'],
            'CODE': ['return', '}'],
            'COMMAND': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                        'return', '}'],
            'OTHERCOMMANDS': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                              'return', '}'],
            'OTHERCOMMANDS2': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while',
                               'if', 'return', '}'],
            'PRINTFUNC': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                          'return', '}'],
            'PRINTABLELIST': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while',
                                  'if', 'return', '}'],
            'PRINTABLE': [',', ')'],
            'NEXTPRINTVALUE': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while',
                                   'if', 'return', '}'],
            'ASSIGNMENT': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                           'return', '}'],
            'FUNCTIONCALL': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', 'IDE', 'global',
                             'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if', 'return', '}',
                             ')'],
            'CONTFCALL': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', 'IDE', 'global',
                          'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if', 'return', '}', ')'],
            'FCALLPARAMS': ['*', '/', '+', '-', '>', '<', '==', '<=', '>=', '&&', '||', ',', ';', ']', 'IDE', 'global',
                            'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if', 'return', '}',
                            ')'],
            'READ': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                     'return', '}'],
            'READPARAMS': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                           'return', '}'],
            'READLOOP': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                         'return', '}'],
            'WHILEFUNC': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                          'return', '}'],
            'CONDITIONAL': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                            'return', '}'],
            'ELSEPART': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if',
                         'return', '}'],
        }
        return follows[state]

    @staticmethod
    def getFirsts(state):
        firsts = {
            'START': ['typedef', 'struct', 'var', 'const', 'procedure', 'function'],
            'HEADER1': ['typedef', 'struct', 'const', 'procedure', 'function'],
            'HEADER2': ['typedef', 'struct', 'var', 'procedure', 'function'],
            'HEADER3': ['typedef', 'struct', 'procedure', 'function'],
            'METHODS': ['procedure', 'function'],
            'PROCCHOICE': ['start', 'IDE'],
            'VARIABLE': ['IDE', 'global', 'local'],
            'SCOPEVARIABLE': ['global', 'local'],
            'VECTMATINDEX': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'DATATYPE': ['int', 'real', 'string', 'boolean', 'IDE'],
            'CONTELEMENT': ['[', '.', 'vazio'],
            'STRUCTE1': ['.'],
            'MATRIZE1': ['[', '.', 'vazio'],
            'MATRIZE2': ['.', 'vazio'],
            'VARDECLARATION': ['var'],
            'FIRSTVAR': ['struct', 'int', 'real', 'string', 'boolean', 'IDE'],
            'NEXTVAR': ['}', 'struct', 'int', 'real', 'string', 'boolean', 'IDE'],
            'CONTINUESOS': ['struct', 'int', 'real', 'string', 'boolean', 'IDE'],
            'VARID': ['IDE'],
            'VAREXP': [',', '=', ';', '['],
            'STRUCTURE': ['[', '=', ',', ';'],
            'CONTMATRIX': ['=', ',', ';'],
            'INITARRAY': ['['],
            'NEXTARRAY': [',', ']'],
            'INITMATRIX': ['['],
            'MATRIXVALUE': ['['],
            'NEXTMATRIX': [',', ']'],
            'NEXT': [',', ']'],
            'VERIFVAR': [',', ';'],
            'CONSTDECLARATION': ['const'],
            'FIRSTCONST': ['struct', 'int', 'real', 'string', 'boolean', 'IDE'],
            'CONTINUECONSTSOS': ['struct', 'int', 'real', 'string', 'boolean', 'IDE'],
            'NEXTCONST': ['struct', 'int', 'real', 'string', 'boolean', 'IDE', '}'],
            'CONSTID': ['IDE'],
            'CONSTEXP': ['=', '['],
            'STRUCTURECONST': ['[', '='],
            'NEXTCONSTVETOR': [',', ']'],
            'INITCONSTMATRIX': ['['],
            'MATRIXCONSTVALUE': ['['],
            'NEXTCONSTMATRIZ': [',', ']'],
            'NEXTCONST2': [',', ']'],
            'VERIFCONST': [',', ';'],
            'FUNCTION': ['function'],
            'CONTINUEFUNCTION': [')', 'int', 'real', 'string', 'boolean', 'IDE', 'struct'],
            'PARAMETERS': ['int', 'real', 'string', 'boolean', 'IDE', 'struct'],
            'PARAMLOOP': [',', ')'],
            'BLOCKFUNCTION': ['{'],
            'BLOCKFUNCTIONCONTENT': ['var', 'const', 'return', 'IDE', 'global', 'local', 'typedef', 'struct', '++',
                                     '--', 'print', 'read', 'while', 'if'],
            'FUNCTIONCONTENT': ['return', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read',
                                'while', 'if'],
            'CONTENT1': ['const', 'return', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read',
                         'while', 'if'],
            'CONTENT2': ['var', 'return', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read',
                         'while', 'if'],
            'CONTENT3': ['return', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while',
                         'if'],
            'STRUCTUREDECLARATION': ['struct'],
            'STRUCTVARS': ['{', 'extends'],
            'FIRSTSTRUCTVAR': ['int', 'real', 'string', 'boolean', 'IDE'],
            'STRUCTVARID': ['IDE'],
            'NEXTSTRUCTVAR': ['int', 'real', 'string', 'boolean', 'IDE', '}'],
            'STRUCTVAREXP': [',', ';', '['],
            'STRUCTMATRIX': ['[', ',', ';'],
            'CONTSTRUCTMATRIX': [',', ';'],
            'EXPRESSION': ['!', '(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'LOGEXP': ['vazio', '&&', '||'],
            'LOGICSYMBOL': ['&&', '||'],
            'RELEXP': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'RELEXP2': ['vazio', '>', '<', '==', '<=', '>='],
            'RELSYMBOL': ['>', '<', '==', '<=', '>='],
            'ARITEXP1': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'ARITEXP2': ['vazio', '+', '-'],
            'ARITSYMB1': ['+', '-'],
            'TERM': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'TERM2': ['vazio', '*', '/'],
            'ARITSYMB2': ['*', '/'],
            'OPERATE': ['(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'CONTOPERATE': ['[', '(', '.', 'vazio'],
            'TYPEDEFDECLARATION': ['typedef'],
            'CONTTYPEDEFDEC': ['int', 'real', 'string', 'boolean', 'IDE', 'struct'],
            'STARTPROCEDURE': ['('],
            'PROCEDURE': ['IDE'],
            'PROCPARAM': ['int', 'real', 'string', 'boolean', 'IDE', 'struct', ')'],
            'PROCCONTENT': ['var', 'const', '}', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print',
                            'read', 'while', 'if'],
            'PROCCONTENT2': ['const', '}', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read',
                             'while', 'if'],
            'PROCCONTENT3': ['var', '}', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read',
                             'while', 'if'],
            'PROCCONTENT4': ['}', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while',
                             'if'],
            'CODE': ['vazio', 'IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while',
                     'if'],
            'COMMAND': ['IDE', 'global', 'local', 'typedef', 'struct', '++', '--', 'print', 'read', 'while', 'if'],
            'OTHERCOMMANDS': ['[', '(', '.', '++', '--', '='],
            'OTHERCOMMANDS2': ['++', '--', '='],
            'PRINTFUNC': ['print'],
            'PRINTABLELIST': ['CAD', 'IDE', 'global', 'local'],
            'PRINTABLE': ['CAD', 'IDE', 'global', 'local'],
            'NEXTPRINTVALUE': [',', ')'],
            'ASSIGNMENT': ['='],
            'FUNCTIONCALL': ['('],
            'CONTFCALL': ['!', ')', '(', 'true', 'false', 'NRO', 'NRO', 'CAD', 'IDE', 'global', 'local'],
            'FCALLPARAMS': [',', ')'],
            'READ': ['read'],
            'READPARAMS': ['IDE', 'global', 'local'],
            'READLOOP': [',', ')'],
            'WHILEFUNC': ['while'],
            'CONDITIONAL': ['if'],
            'ELSEPART': ['else', 'vazio'],
        }
        return firsts[state]
