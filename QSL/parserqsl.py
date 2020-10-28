#!/bin/python3

import ply.yacc as yacc

from lexer import lexer_qsl
import re
from astqsl import *

class parser_qsl:

    start = 'program'

    # Program
    def p_program_mult(self,p):
        '''program : lines line'''
        p[0] = program(p[2], p[1])

    def p_program_single(self,p):
        '''program : line'''
        p[0] = program(p[1])

    def p_empty(self, p):
        'empty :'
        pass

    def p_jump(self,p):
        '''jump : jump NL
                | empty'''
        pass

    def p_line(self,p):
        '''line : jump expresion jump'''
        p[0] = p[2]

    def p_lines(self,p):
        '''lines : lines line
                | line '''
        if (len(p) == 2):
            p[0] = program(p[1])
        else:
            p[0] = program(p[2], p[1])

    # Expresions
    def p_expresion(self,p):
        '''expresion : e0
                    | assign
                    | import'''
        p[0] = p[1]

    # Import
    def p_import(self,p):
        '''import : IMPORT STRING'''
        p[0] = load_import(p[2])

    # Assign
    def p_assign(self,p):
        'assign : des ASSIGN e0'
        p[0] = assign(p[1], p[3])

    # Designators
    def p_des(self,p):
        ''' des : ket_des
                | bra_des
                | id_des '''
        p[0] = p[1]

    def p_ket_des(self,p):
        ' ket_des : KET'
        value = re.search(r'\|(.*?)\>', p[1]).group(1)
        p[0] = ket_des(value)

    def p_bra_des(self,p):
        'bra_des : BRA'
        value = re.search(r'\<(.*?)\|', p[1]).group(1)
        p[0] = bra_des(value)

    def p_id_des(self,p):
        'id_des : ID'
        p[0] = id_des(p[1])


    # Expresion priority
    def p_e0(self,p):
        '''e0 : e0 ADD e1
                | e0 SUB e1
                | e1'''
        if (len(p) == 2):
            p[0] = p[1]
        elif (p[2] == '+'):
            p[0] = addOp(p[1], p[3])
        elif (p[2] == '-'):
            p[0] = subOp(p[1], p[3])

    def p_e1(self,p):
        '''e1 : e1 MULT e2
                | e1 DIV e2
                | multseq
                | e2'''
        if (len(p) == 4):
            if (p[2] == '*'):
                p[0] = multOp(p[1], p[3])
            else:
                p[0] = divOp(p[1], p[3])
        else:
            p[0] = p[1]

    def p_e2(self,p):
        '''e2 : ket bra
                | inprod
                | e3'''
        if (len(p) == 3):
            p[0] = dotOp(p[1], p[2])
        else:
            p[0] = p[1]


    def p_e3(self,p):
        '''e3 : e4 POW e4
                | e4'''
        if (len(p) == 4):
            p[0] = powOp(p[1], p[3])
        else:
            p[0] = p[1]

    def p_e4(self,p):
        '''e4 : e4 OTIMES e5
                | multitensor
                | e5'''
        if len(p) == 4:
            p[0] = tensorOp(p[1], p[3])
        else:
            p[0] = p[1]

    def p_e5(self,p):
        '''e5 : ket
                | bra
                | pi
                | id
                | i
                | e
                | matrix
                | number
                | measure
                | blackbox
                | LPAR e0 RPAR'''
        if (len(p) == 4):
            p[0] = p[2]
        else:
            p[0] = p[1]

    def p_multseq(self,p):
        '''multseq : e2 e4
                    | e2 multseq '''
        p[0] = multOp(p[1], p[2])

    def p_multitensor(self, p):
        ''' multitensor : ket multitensor
                        | ket ket'''
        p[0] = tensorOp(p[1], p[2])

    def p_ket(self,p):
        ''' ket : ketv
                | cket'''
        p[0] = p[1]

    def p_bra(self,p):
        ''' bra : brav
                | cbra'''
        p[0] = p[1]

    def p_inprod(self,p):
        'inprod : INPROD'
        val0 = re.search(r'\<(.*?)\|', p[1]).group(1)
        if (val0.isdigit()):
            braq = cbra(val0)
        else:
            braq = bra_expr(val0)
        val1 = re.search(r'\|(.*?)\>', p[1]).group(1)
        if (val1.isdigit()):
            kett = cket(val1)
        else:
            kett = ket_expr(val1)
        p[0] = innerOp(braq, kett)

    # Constants
    def p_cket(self,p):
        'cket : CKET'
        value = re.search(r'\|(.*?)\>', p[1]).group(1)
        p[0] = cket(value)

    def p_cbra(self,p):
        'cbra : CBRA'
        value = re.search(r'\<(.*?)\|', p[1]).group(1)
        p[0] = cbra(value)

    def p_number(self,p):
        'number : NUMBER'
        p[0] = number(p[1])

    def p_imag(self,p):
        '''i : I
            | NUMBER I'''
        if (len(p) == 2):
            p[0] = complex_number("0", "1")
        else:
            p[0] = complex_number("0", p[1])

    def p_e(self,p):
        'e : E'
        p[0] = number(p[1])

    def p_pi(self,p):
        'pi : PI'
        p[0] = number(p[1])

    def p_matrix(self,p):
        'matrix : LBRA jump sequence jump RBRA'
        p[0] = matrix(p[3])

    def p_sequence(self,p):
        '''sequence : jump NUMBER sequence
                    | sequence SCOL sequence
                    | jump NUMBER jump'''
        if len(p) == 4:
            if (p[3] is None):
                p[0] = p[2]
            elif (p[1] is None):
                p[0] = p[2] + " " + p[3]
            else:
                p[0] = p[1] + "; " + p[3] 
            

    def p_measure(self,p):
        '''measure : MEASURE'''
        value = re.search(r'M_(.*)?', p[1]).group(1)
        p[0] = measure(value)

    def p_blackbox(self, p):
        '''blackbox : BLACKBOX LPAR bb_line RPAR'''
        p[0] = blackbox(p[3])

    def p_bb_line(self,p):
        '''bb_line : jump bb_statements jump'''
        p[0] = p[2]

    def p_bb_statements(self, p):
        '''bb_statements : e0'''
        p[0] = bbstate_matrix(p[1])


    # Variables 
    def p_ketv(self,p):
        '''ketv : KET'''
        value = re.search(r'\|(.*?)\>', p[1]).group(1)
        p[0] = ket_expr(value)

    def p_brav(self,p):
        '''brav : BRA'''
        value = re.search(r'\<(.*?)\|', p[1]).group(1)
        p[0] = bra_expr(value)

    def p_id(self,p):
        'id : ID'
        p[0] = id_expr(p[1])

    # Error rule for syntax errors
    def p_error(self,p):
        print(p)
    
    def build(self, lexer, **kwargs):
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
    