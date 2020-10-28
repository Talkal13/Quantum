import ply.lex as lex

class lexer_qsl:

    reserved = {
        'e':'E',
        'i':'I',
        'pi':'PI',
        'ox':'OTIMES',
        'import':'IMPORT',
        'blackbox': 'BLACKBOX'
    }

    tokens = [
        # Variables
        'BRA',
        'KET',
        'ID',
        # Operations
        'MULT',
        'ADD',
        'SUB',
        'DIV',
        'INPROD',
        'ASSIGN',
        # Constants
        'NUMBER',
        'NL',
        'CKET',
        'CBRA',
        # Priority
        'LPAR',
        'RPAR',
        'LBRA',
        'RBRA',
        'LCURL',
        'RCURL',
        'SCOL',
        'POW',
        'MEASURE',
        'STRING'
    ] + list(reserved.values())

    t_MULT = r'\*'
    t_ADD = r'\+'
    t_SUB = r'-'
    t_DIV = r'/'
    t_ASSIGN = r'='
    t_LPAR = r'\('
    t_RPAR = r'\)'
    t_LBRA = r'\['
    t_RBRA = r'\]'
    t_POW = r'\^'
    t_SCOL = r';'
    t_LCURL = r'\{'
    t_RCURL = r'\}'

    def t_STRING(self,t):
        r'\"[\w\/]*\"'
        return t

    def t_MEASURE(self,t):
        r'M_[a-zA-Z0-9]+'
        return t

    def t_NUMBER(self,t):
        r'\d+(\.\d+)?'
        t.value = t.value
        return t

    def t_BRA(self,t):
        r'<[a-zA-Z][a-zA-Z_0-9]*\|'
        return t

    def t_KET(self,t):
        r'\|[a-zA-Z][a-zA-Z_0-9]*\>'
        return t

    def t_INPROD(self,t):
        r'<[a-zA-Z_0-9]+\|[a-zA-Z_0-9]+\>'
        return t

    def t_CBRA(self,t):
        r'<\~?\d+\|'
        return t

    def t_CKET(self,t):
        r'\|\~?\d+\>'
        return t

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.type = 'NL'
        return t

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'
    t_ignore_COMMENT = '\#.*'
    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

