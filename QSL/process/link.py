

class link:

    def __init__(self, tv):
        self.tv = tv

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)

    def visit_assign(self, assig):
        assig.des.visit(self)
        assig.expr.visit(self)

    def visit_add(self, expr):
        for exp in expr.expr:
            exp.visit(self)

    def visit_sub(self, expr):
        for exp in expr.expr:
            exp.visit(self)

    def visit_dot(self, expr):
        for exp in expr.expr:
            exp.visit(self)

    def visit_mult(self, expr):
        for exp in expr.expr:
            exp.visit(self)
    
    def visit_div(self, expr):
        for exp in expr.expr:
            exp.visit(self)

    def visit_pow(self, expr):
        for exp in expr.expr:
            exp.visit(self)

    def visit_inner(self, expr):
        for exp in expr.expr:
            exp.visit(self)

    def visit_cket(self, ket):
        pass
    
    def visit_cbra(self, bra):
        pass

    def visit_ket(self, des):
        des.link = self.tv[des.id]
    
    def visit_bra(self, des):
        des.link = self.tv[des.id]

    def visit_id(self, des):
        des.link = self.tv[des.id]
    
    def visit_complex(self, comp):
        comp.A.visit(self)
        comp.exp.visit(self)
    
    def visit_number(self, numb):
        pass

    def visit_complex_number(self, numb):
        pass

    def visit_ket_des(self, link):
        self.tv[link.id] = link
    
    def visit_bra_des(self, link):
        self.tv[link.id] = link

    def visit_id_des(self, link):
        self.tv[link.id] = link
    