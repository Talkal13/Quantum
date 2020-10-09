

class execute:

    def __init__(self):
        pass

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