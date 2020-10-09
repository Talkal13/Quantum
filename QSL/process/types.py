
T_BRA = "T_BRA"
T_KET = "T_KET"
T_MATRIX = "T_MATRIX"

class types:

    def __init__(self):
        pass

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)

    def visit_assign(self, assig):
        assig.des.visit(self)
        assig.expr.visit(self)
        if (assig.des.type != assig.expr.type):
            raise Exception("Types not equal") # TODO: Error system

    def visit_add(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr.expr[0].type != expr.expr[1].type):
            raise Exception("Types not equal") #TODO
        expr.type = expr.expr[0].type
        

    def visit_sub(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr.expr[0].type != expr.expr[1].type):
            raise Exception("Types not equal") #TODO
        expr.type = expr.expr[0].type

    def visit_dot(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr.expr[0].type != T_KET or expr.expr[1].type != T_BRA):
            raise Exception("Type error") #TODO
        expr.type = T_MATRIX

    def visit_cket(self, ket):
        ket.type = T_KET
    
    def visit_cbra(self, bra):
        bra.type = T_BRA

    def visit_ket(self, des):
        des.type = des.link.type
    
    def visit_bra(self, des):
        des.type = des.link.type

    def visit_id(self, des):
        des.type = des.link.type

    def visit_ket_des(self, link):
        link.type = T_KET
    
    def visit_bra_des(self, link):
        link.type = T_BRA

    def visit_id_des(self, link):
        link.type = T_MATRIX