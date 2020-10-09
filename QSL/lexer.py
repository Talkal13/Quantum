import ply.lex as lex

reserved = {

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
    'ASSIGN',
    # Constants
    'NUMBER',
    'NL',
    'CKET',
    'CBRA'
] + list(reserved.values())

t_MULT = r'\*'
t_ADD = r'\+'
t_SUB = r'-'
t_DIV = r'/'
t_ASSIGN = r':='

def t_NUMBER(t):
    r'[-+]?\d+(.\d+)?'
    t.value = float(t.value)
    return t

def t_BRA(t):
    r'<[a-zA-Z][a-zA-Z_0-9]*\|'
    return t

def t_KET(t):
    r'\|[a-zA-Z][a-zA-Z_0-9]*\>'
    return t

def t_CBRA(t):
    r'<\d+\|'
    return t

def t_CKET(t):
    r'\|\d+\>'
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'ID')    # Check for reserved words
     return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NL'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lextok = lex.lex()
