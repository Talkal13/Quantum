#!/bin/python3

import ply.yacc as yacc

from lexer import tokens
import re
from ast import addOp, subOp, dotOp, assign, ket_expr, bra_expr, id_expr, ket_des, bra_des, id_des, cket, cbra, program


start = 'program'

def p_program_mult(p):
    '''program : lines line'''
    p[0] = program(p[2], p[1])

def p_program_single(p):
    '''program : line'''
    p[0] = program(p[1])

def p_line(p):
    '''line : expresion 
            | expresion NL'''
    p[0] = p[1]

def p_lines(p):
    '''lines : lines line
            | line '''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = program(p[2], p[1])

def p_expresion(p):
    '''expresion : e0
                | assign '''
    p[0] = p[1]

def p_assign(p):
    'assign : des ASSIGN e0'
    p[0] = assign(p[1], p[3])

def p_des(p):
    ''' des : ket_des
            | bra_des
            | id_des '''
    p[0] = p[1]

def p_ket_des(p):
    ' ket_des : KET'
    value = re.search(r'\|(.*?)\>', p[1]).group(1)
    p[0] = ket_des(value)

def p_bra_des(p):
    'bra_des : BRA'
    value = re.search(r'\<(.*?)\|', p[1]).group(1)
    p[0] = bra_des(value)

def p_id_des(p):
    'id_des : ID'
    p[0] = id_des(p[1])

def p_e0(p):
    '''e0 : e0 ADD e1
            | e0 SUB e1
            | e1'''
    if (len(p) == 2):
        p[0] = p[1]
    elif (p[2] == '+'):
        p[0] = addOp(p[1], p[3])
    elif (p[2] == '-'):
        p[0] = subOp(p[1], p[3])

def p_e1(p):
    '''e1 : ket bra
            | e2'''
    if (len(p) == 3):
        p[0] = dotOp(p[1], p[2])
    else:
        p[0] = p[1]
    
def p_e2(p):
    '''e2 : ket
            | bra
            | id'''
    p[0] = p[1]

def p_ket(p):
    ''' ket : ketv
            | cket'''
    p[0] = p[1]

def p_bra(p):
    ''' bra : brav
            | cbra'''
    p[0] = p[1]


def p_cket(p):
    'cket : CKET'
    value = re.search(r'\|(.*?)\>', p[1]).group(1)
    p[0] = cket(value)

def p_cbra(p):
    'cbra : CBRA'
    value = re.search(r'\<(.*?)\|', p[1]).group(1)
    p[0] = cbra(value)


def p_ketv(p):
    '''ketv : KET'''
    value = re.search(r'\|(.*?)\>', p[1]).group(1)
    p[0] = ket_expr(value)

def p_brav(p):
    '''brav : BRA'''
    value = re.search(r'\<(.*?)\|', p[1]).group(1)
    p[0] = bra_expr(value)

def p_id(p):
    'id : ID'
    p[0] = id_expr(p[1])

# Error rule for syntax errors
def p_error(p):
    print(p)


# Build the parser
parser = yacc.yacc()
