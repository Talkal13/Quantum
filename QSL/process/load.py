class load:

    def __init__(self, parser):
        self.parser = parser

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)
    
    def visit_load(self, load):
        data = open(load.file).read()
        load.ast = self.parser.parse(data)
        load.ast.visit(self)

    def visit_assign(self, assig):
        pass

    def visit_add(self, expr):
        pass

    def visit_sub(self, expr):
        pass

    def visit_dot(self, expr):
        pass

    def visit_mult(self, expr):
        pass
    
    def visit_div(self, expr):
        pass

    def visit_pow(self, expr):
        pass

    def visit_inner(self, expr):
        pass

    def visit_tensor(self, expr):
        pass
    def visit_cket(self, ket):
        pass
    
    def visit_cbra(self, bra):
        pass

    def visit_ket(self, des):
        pass
    
    def visit_bra(self, des):
        pass

    def visit_id(self, des):
        pass
    
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