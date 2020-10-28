from math import sin, cos, pow, pi, e, sqrt
from cmath import exp
import numpy as np
from helper import generate_qubit, parse_string, q
from .types import T_COMPLEX, T_MATRIX, T_KET, T_NUMBER, T_MEASUREMENT, T_BRA, T_KET
global tv

class execute:

    def __init__(self):
        pass
        

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)
            program.value = line.value
        
    def visit_load(self, load):
        load.value = load.ast.visit(self)

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
        if (expr[0].type == T_MEASUREMENT and expr[1].type == T_KET):
            try:
                expr.value = 1/sqrt(expr[1].value.conj().T.dot(expr[0].value.conj().T).dot(expr[0].value).dot(expr[1].value)[0][0]) * expr[0].value.dot(expr[1].value)
            except ZeroDivisionError:
                expr.value = None
        elif (expr[0].type == T_MATRIX and expr[1].type == T_KET):
            (_, mt) = expr[0].value.shape
            (k, _) = expr[1].value.shape
            while(mt > k):
                expr[1].value = np.kron(expr[1].value, q[0].T)
                (k, _) = expr[1].value.shape
            while(mt < k):
                expr[0].value = np.kron(expr[0].value, np.identity(2))
                (_, mt) = expr[0].value.shape
            expr.value = expr[0].value.dot(expr.expr[1].value)
        elif (expr[0].type == T_MATRIX and expr[1].type == T_MATRIX):
            (_, m1) = expr[0].value.shape
            (m2, _) = expr[1].value.shape
            while(m1 > m2):
                expr[1].value = np.kron(expr[1].value, np.identity(2))
                (m2, _) = expr[1].value.shape
            while(m1 < m2):
                expr[0].value = np.kron(expr[0].value, np.identity(2))
                (_, m1) = expr[0].value.shape
            expr.value = expr[0].value * expr[1].value
        else:
            expr.value = expr.expr[0].value * expr.expr[1].value
        
        if (isinstance(expr.value, np.ndarray) and expr.value.shape == (1, 1)):
                expr.value = expr.value.A1[0]
        
    
    def visit_div(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value
        for exp in expr.expr[1:]:
            expr.value = expr.value / exp.value
    
    def visit_pow(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr.expr[0].type == T_NUMBER and expr.expr[0].str == "e"):
            comp = expr.expr[1].value
            expr.value = e ** comp
        else:
            expr.value = expr.expr[0].value ** expr.expr[1].value
    
    def visit_inner(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.value = expr.expr[0].value.dot(expr.expr[1].value)[0][0]

    def visit_tensor(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr[1].type == T_NUMBER):
            expr.value = np.kron(expr[0].value, expr[0].value)
            for _ in range(int(expr[1].value) - 2):
                expr.value = np.kron(expr.value, expr[0].value)
        else:
            expr.value = np.kron(expr[0].value, expr[1].value)
        

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
    
    def visit_matrix(self, mat):
        mat.value = np.matrix(mat.sequence)
        if (mat.value.shape == (1, 1)):
            mat.value = mat.value.A1[0]

    def visit_measure(self, measure):
        if measure.basis.isdigit():
            val, size = parse_string(measure.basis)
            measure.value = generate_qubit(val, size)
        else:
            measure.value = measure.link.value
        measure.value = measure.value.conj().T.dot(measure.value)

    def visit_cket(self, ket):
        pass
    
    def visit_cbra(self, bra):
        pass

    def visit_ket(self, des):
        des.link.visit(self)
        des.value = des.link.value
        if (des.link.type == T_BRA):
            des.value = des.value.conj().T
            des.type = T_KET
    
    def visit_bra(self, des):
        des.link.visit(self)
        des.value = des.link.value
        if (des.link.type == T_KET):
            des.value = des.value.conj().T
            des.type = T_BRA

    def visit_id(self, des):
        des.link.visit(self)
        des.value = des.link.value

    def visit_ket_des(self, link):
        pass
    
    def visit_bra_des(self, link):
        pass

    def visit_id_des(self, link):
        pass

    def visit_bbdef(self, link):
        link.statements.visit(self)
        link.value = link.statements.value

    def visit_bbstate_matrix(self, state):
        state.matrix.visit(self)
        state.value = state.matrix.value