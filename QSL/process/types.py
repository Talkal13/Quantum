
T_BRA = "T_BRA"
T_KET = "T_KET"
T_MATRIX = "T_MATRIX"
T_COMPLEX = "T_COMPLEX"
T_NUMBER = "T_NUMBER"
T_MEASUREMENT = "T_MEASUREMENT"

class types:

    def __init__(self):
        pass

    def visit_program(self, program):
        for line in program.lines:
            line.visit(self)

    def visit_load(self, load):
        load.ast.visit(self)

    def visit_assign(self, assig):
        assig.des.visit(self)
        assig.expr.visit(self)
        # if (assig.des.type != assig.expr.type):
        #     raise Exception("Types not equal") # TODO: Error system

    def visit_add(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        # if (expr.expr[0].type != expr.expr[1].type and (expr.expr[0].type != T_NUMBER or expr.expr[1].type != T_COMPLEX)):
        #     raise Exception("Types not equal") #TODO
        expr.type = expr.expr[1].type
        

    def visit_sub(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        # if (expr.expr[0].type != expr.expr[1].type or (expr.expr[0].type == T_NUMBER and expr.expr[1].type == T_COMPLEX)):
        #     raise Exception("Types not equal") #TODO
        expr.type = expr.expr[1].type

    def visit_dot(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        # if (expr.expr[0].type != T_KET or expr.expr[1].type != T_BRA):
        #     raise Exception("Type error") #TODO
        expr.type = T_MATRIX
    
    def visit_mult(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        # if (expr.expr[0].type != expr.expr[1].type):
        #     raise Exception("Types not equal") #TODO
        expr.type = expr.expr[1].type

    def visit_div(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        # if (expr.expr[0].type != expr.expr[1].type):
        #     raise Exception("Types not equal") #TODO
        expr.type = expr.expr[0].type
    
    def visit_pow(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        # if (expr.expr[0].type != T_NUMBER or (expr.expr[1].type != T_COMPLEX or expr.expr[1].type != T_NUMBER)):
        #     raise Exception("Type error") #TODO
        expr.type = expr.expr[1].type
    
    def visit_inner(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        expr.type = T_COMPLEX
    
    def visit_tensor(self, expr):
        for exp in expr.expr:
            exp.visit(self)
        if (expr[0].type != T_MATRIX and expr[0].type != T_KET and expr[0].type != T_BRA and expr[0].type != T_MEASUREMENT):
            raise Exception("Type error") #TODO
        if (expr[1].type == T_MEASUREMENT):
            expr.type = expr[1].type
        else:
            expr.type = expr[0].type

    def visit_complex(self, comp):
        comp.A.visit(self)
        comp.exp.visit(self)
        comp.type = T_COMPLEX
    
    def visit_number(self, numb):
        numb.type = T_NUMBER

    def visit_complex_number(self, comp):
        comp.type = T_COMPLEX
    
    def visit_matrix(self, matrix):
        matrix.type = T_MATRIX

    def visit_measure(self, measure):
        measure.type = T_MEASUREMENT

    def visit_cket(self, ket):
        ket.type = T_KET
    
    def visit_cbra(self, bra):
        bra.type = T_BRA

    def visit_ket(self, des):
        if (des.link.type != T_KET and des.link.type != T_BRA):
            raise TypeError("Type does not match")
        des.type = des.link.type
    
    def visit_bra(self, des):
        if (des.link.type != T_KET and des.link.type != T_BRA):
            raise TypeError("Type does not match")
        des.type = des.link.type

    def visit_id(self, des):
        des.type = des.link.type

    def visit_ket_des(self, link):
        link.type = T_KET
    
    def visit_bra_des(self, link):
        link.type = T_BRA

    def visit_id_des(self, link):
        link.type = T_MATRIX

    def visit_bbdef(self, link):
        link.statements.visit(self)
        link.type = link.statements.type

    def visit_bbstate_matrix(self, state):
        state.matrix.visit(self)
        state.type = state.matrix.type
        if (state.type != T_MATRIX):
            raise TypeError("Statement not a matrix")