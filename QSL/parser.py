import ply.yacc as yacc

from lexer import tokens
import re
import numpy as np
from helper import generate_qubit

start = 'line'

def p_line(p):
    '''line : expresion 
            | expresion NL'''
    p[0] = p[1]

def p_expresion(p):
    '''expresion : r0
                | assign '''
    p[0] = p[1]

def p_r0(p):
    '''r0 : r0 ADD r1
            | r0 SUB r1
            | r1'''
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == '+'):
        p[0] = p[1] + p[3]
    elif (p[2] == '-'):
        p[0] = p[1] - p[3]

def p_r1(p):
    '''r1 : ket bra'''
    if (len(p) == 3):
        p[0] = p[2].dot(p[1])
    
def p_ket(p):
    '''ket : KET'''
    value = re.search(r'\|(.*?)\>', p[1]).group(1)
    p[0] = generate_qubit(int(value))

def p_bra(p):
    '''bra : BRA'''
    value = re.search(r'\<(.*?)\|', p[1]).group(1)
    p[0] = generate_qubit(int(value)).T

# Error rule for syntax errors
def p_error(p):
    print(p)


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('QSL> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)