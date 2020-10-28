from helper import generate_qubit, parse_string
from math import log2
import numpy as np

class program:
    def __init__(self, line, lines=None):
        self.lines = []
        if (lines is None):
            self.lines = [line]
        else:
            if (isinstance(lines, program)):
                self.lines = lines.lines
                self.lines.append(line)
                

    def visit(self, visitor):
        return visitor.visit_program(self)


class assign:
    def __init__(self, id, expr):
        self.des = id
        self.expr = expr
        self.value = None

    def visit(self, visitor):
        return visitor.visit_assign(self)

class expr:
    def __init__(self, exp):
        self.exp = []
        self.exp.append(exp)
        self.value = None
    
    def visit(self):
        raise NotImplementedError

class bin_expr:
    def __init__(self, exp0, exp1):
        self.expr = []
        self.value = None
        self.expr.append(exp0)
        self.expr.append(exp1)

    def __getitem__(self, key):
        return self.expr[key]
        
    def visit(self):
        raise NotImplementedError

class dotOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_dot(self)

class addOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_add(self)

class subOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_sub(self)

class multOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_mult(self)

class divOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_div(self)

class powOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_pow(self)
    
class innerOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_inner(self)

class tensorOp(bin_expr):
    def visit(self, visitor):
        return visitor.visit_tensor(self)

# Constants
class cbra:
    def __init__(self, value):
        self.id = value
        val, size = parse_string(value)
        self.value = generate_qubit(val, size)
    def visit(self, visitor):
        return visitor.visit_cbra(self)
    def __repr__(self): return self.__str__()
    def __str__(self): return "<" + self.id + "|"

class cket:
    def __init__(self, value):
        self.id = value
        val, size = parse_string(value)
        self.value = generate_qubit(val, size).conj().T
    def visit(self, visitor):
        return visitor.visit_cket(self)
    def __repr__(self): return self.__str__()
    def __str__(self): return "|" + self.id + ">"


class number:
    def __init__(self, value):
        self.str = value
        self.type = None
    def visit(self, visitor):
        return visitor.visit_number(self)

class complex_number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        self.type = None
    def visit(self, visitor):
        return visitor.visit_complex_number(self)

class matrix:
    def __init__(self, sequence):
        self.sequence = sequence
    def visit(self, visitor):
        return visitor.visit_matrix(self)
    
class measure:
    def __init__(self, basis):
        self.basis = basis
    def visit(self, visitor):
        return visitor.visit_measure(self)

class entangle:
    def __init__(self, a, b, value):
        self.kets = [a, b]
        self.value = value
        self.density = value.dot(value.T)



# Vars expr

class des_ex:
    def __init__(self, id):
        self.id = id
        self.link = None

    def visit(self, visitor):
        raise NotImplementedError

class ket_expr(des_ex):
    def visit(self, visitor):
        return visitor.visit_ket(self)

class bra_expr(des_ex):
    def visit(self, visitor):
        return visitor.visit_bra(self)

class id_expr(des_ex):
    def visit(self, visitor):
        return visitor.visit_id(self)


# Vars desig
class des:
    def __init__(self, id):
        self.id = id
        self.value = None
    
    def visit(self, visitor):
        raise NotImplementedError

class ket_des(des):
    slinks = []
    def visit(self, visitor):
        return visitor.visit_ket_des(self)
    def trace(self, state):
        # Qiskit 
        trace_systems = len(state._dims) - 1 - np.array(qargs)
        new_dims = tuple(np.delete(np.array(state._dims), qargs))
        new_dim = np.product(new_dims)
        arr = state._data.reshape(state._shape)
        rho = np.tensordot(arr, arr.conj(),
                           axes=(trace_systems, trace_systems))
        rho = np.reshape(rho, (new_dim, new_dim))
    def __str__(self):
        if (self.value is None):
            return "None"
        s = ""
        i = 0
        (size, _) = self.value.shape
        size = int(log2(size))
        for a in self.value:
            for val in a:
                if (s != "" and val > 0):
                    s = s + " + "
                elif (s != "" and val < 0):
                    s = s + " - "
                if (val != 0 and abs(val) != 1):
                    s = s + f"{abs(float(val)):.4f}" + "|" + f"{int(i):0{size}b}" + ">"
                elif (val == 1 or val == -1):
                    s = s + "|" + f"{int(i):0{size}b}" + ">"
                i = i + 1
        return s
    def __repr__(self):
        return self.__str__()

class bra_des(des):
    slinks = []  
    def visit(self, visitor):
        return visitor.visit_bra_des(self)

class id_des(des):
    def visit(self, visitor):
        return visitor.visit_id_des(self)
    def __str__(self):
        return self.value.__str__()

# IMPORT
class load_import:
    def __init__(self, file):
        self.file = file.replace(r'"', '') + ".qsl"
        self.ast = None
    def visit(self, visitor):
        return visitor.visit_load(self)

class blackbox:
    def __init__(self, statements):
        self.statements = statements
    def visit(self, visitor):
        return visitor.visit_bbdef(self)

class bbstate_matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def visit(self, visitor):
        return visitor.visit_bbstate_matrix(self)