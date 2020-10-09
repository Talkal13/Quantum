from helper import generate_qubit

class program:
    def __init__(self, line, lines=None):
        self.lines = []
        if (lines is None):
            self.lines = [line]
        else:
            if (isinstance(lines, program)):
                self.lines = lines.lines
                self.lines.append(line)
            else:
                self.lines.append(lines)

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

# Constants
class cbra:
    def __init__(self, value):
        self.value = generate_qubit(int(value))
    def visit(self, visitor):
        return visitor.visit_cbra(self)

class cket:
    def __init__(self, value):
        self.value = generate_qubit(int(value)).T
    def visit(self, visitor):
        return visitor.visit_cket(self)



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
    def visit(self, visitor):
        return visitor.visit_ket_des(self)

class bra_des(des):
    def visit(self, visitor):
        return visitor.visit_bra_des(self)

class id_des(des):
    def visit(self, visitor):
        return visitor.visit_id_des(self)