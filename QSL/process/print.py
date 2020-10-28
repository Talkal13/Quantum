import sys

class printkb:

    def __init__(self, output=sys.stdout):
        self.output = output

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)
            self.print("\n")
    
    def visit_load(self, load):
        pass

    def visit_assign(self, assig):
        s = assig.des.id + " = " + assig.des.__str__()
        print(s, file=self.output)

    def visit_add(self, expr):
        expr[0].visit(self)
        self.print(" + ")
        expr[1].visit(self)

    def visit_sub(self, expr):
        expr[0].visit(self)
        self.print(" + ")
        expr[1].visit(self)

    def visit_dot(self, expr):
        print(expr.value)

    def visit_mult(self, expr):
        expr[0].visit(self)
        self.print("\u2219")
        expr[1].visit(self)
    
    def visit_div(self, expr):
        expr[0].visit(self)
        self.print("/")
        expr[1].visit(self)

    def visit_pow(self, expr):
        expr[0].visit(self)
        self.print("^")
        expr[1].visit(self)

    def visit_inner(self, expr):
        self.print("<")
        expr[0].visit(self)
        self.print("|")
        expr[1].visit(self)
        self.print(">")

    def visit_tensor(self, expr):
        expr[0].visit(self)
        self.print(" \u2297 ")
        expr[1].visit(self)

    def visit_cket(self, ket):
        self.print(ket)
    
    def visit_cbra(self, bra):
        self.print(bra)

    def visit_ket(self, des):
        self.print("|" + des.link.id + ">")
    
    def visit_bra(self, des):
        self.print(des)

    def visit_id(self, des):
        self.print(des.link.id)
    
    def visit_complex(self, comp):
        pass
    
    def visit_number(self, numb):
        pass

    def visit_complex_number(self, numb):
        pass

    def visit_matrix(self, matrix):
        pass

    def visit_measure(self, measure):
        pass

    def visit_ket_des(self, link):
        pass
    
    def visit_bra_des(self, link):
        pass

    def visit_id_des(self, link):
        pass
    
    def visit_bbdef(self, link):
        pass

    def visit_bbstate_matrix(self, state):
        pass

    def print(self, s):
        print(s, end='', file=self.output)