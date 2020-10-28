class slink:

    def __init__(self):
        self.value = None
        self.tv = []

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)
        
    def visit_load(self, load):
        load.ast.visit(self)

    def visit_assign(self, assig):
        self.value = assig.des
        assig.expr.visit(self)
        self.value = None

    def slink_bin(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.slins = self.tv

    def visit_add(self, expr):
        self.slink_bin(expr)   

    def visit_sub(self, expr):
        self.slink_bin(expr)

    def visit_dot(self, expr):
        self.slink_bin(expr)

    def visit_mult(self, expr):
        self.slink_bin(expr)
    
    def visit_div(self, expr):
        self.slink_bin(expr)

    def visit_pow(self, expr):
        self.slink_bin(expr)

    def visit_inner(self, expr):
        self.slink_bin(expr)

    def visit_tensor(self, expr):
        self.slink_bin(expr)

    def visit_cket(self, ket):
        pass
    
    def visit_cbra(self, bra):
        pass

    def visit_ket(self, des):
        self.tv.append(des.link)
    
    def visit_bra(self, des):
        self.tv.append(des.link)

    def visit_id(self, des):
        pass
    
    def visit_number(self, numb):
        pass

    def visit_complex_number(self, numb):
        pass

    def visit_matrix(self, matrix):
        pass

    def visit_ket_des(self, link):
        pass
    
    def visit_bra_des(self, link):
        pass

    def visit_id_des(self, link):
        pass

    def visit_bbdef(self, link):
        link.statements.visit(self)

    def visit_bbstate_matrix(self, state):
        state.matrix.visit(self)

    def visit_measure(self, measure):
        pass
    