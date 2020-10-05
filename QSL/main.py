from lexer import *
from parser import *

# Test it out
data = '''|0><1|
'''

# Give the lexer some input
lextok.input(data)

# Tokenize
while True:
    tok = lextok.token()
    if not tok: 
        break      # No more input
    print(tok)
