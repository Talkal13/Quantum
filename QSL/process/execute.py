from math import sin, cos, pow, pi, e
from cmath import exp
from ast import number
from .types import T_COMPLEX, T_MATRIX, T_KET
import numpy as np

class execute:

    def __init__(self):
        pass

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)
            program.value = line.value

    def visit_assign(self, assig):
        assig.des.visit(self)
        assig.expr.visit(self)
        assig.des.value = assig.expr.value

    def visit_add(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value
        for exp in expr.expr[1:]:
            expr.value = expr.value + exp.value


    def visit_sub(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value
        for exp in expr.expr[1:]:
            expr.value = expr.value - exp.value

    def visit_dot(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value
        for exp in expr.expr[1:]:
            expr.value = expr.value.dot(exp.value)

    def visit_mult(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr[0].type == T_MATRIX and expr[1].type == T_KET):
            expr.value = expr[0].value.dot(expr.expr[1].value)
        else:
            expr.value = expr.expr[0].value * expr.expr[1].value
    
    def visit_div(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value
        for exp in expr.expr[1:]:
            expr.value = expr.value / exp.value
    
    def visit_pow(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (isinstance(expr.expr[0], number) and expr.expr[0].str == "e"):
            comp = expr.expr[1].value
            expr.value = e ** comp
        else:
            expr.value = pow(expr.expr[0].value, expr.expr[1].value)
    
    def visit_inner(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value.dot(expr.expr[1].value)[0][0]
        

    def visit_complex(self, comp):
        comp.A.visit(self)
        comp.exp.visit(self)
        comp.value = complex(comp.A.value * cos(comp.exp.value), comp.A.value * sin(comp.exp.value))
    
    def visit_number(self, numb):
        if (numb.str == 'pi'):
            numb.value = pi
        elif (numb.str == 'e'):
            numb.value = e
        else:
            numb.value = float(numb.str)

    def visit_complex_number(self, comp):
        real = float(comp.real)
        imag = float(comp.imag)
        comp.value = complex(real, imag)
        

    def visit_cket(self, ket):
        pass
    
    def visit_cbra(self, bra):
        pass

    def visit_ket(self, des):
        des.link.visit(self)
        des.value = des.link.value
    
    def visit_bra(self, des):
        des.link.visit(self)
        des.value = des.link.value

    def visit_id(self, des):
        des.link.visit(self)
        des.value = des.link.value

    def visit_ket_des(self, link):
        pass
    
    def visit_bra_des(self, link):
        pass

    def visit_id_des(self, link):
        pass