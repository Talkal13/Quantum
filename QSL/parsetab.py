
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programADD ASSIGN BRA CBRA CKET DIV ID KET MULT NL NUMBER SUBprogram : lines lineprogram : lineline : expresion \n            | expresion NLlines : lines line\n            | line expresion : e0\n                | assign assign : des ASSIGN e0 des : ket_des\n            | bra_des\n            | id_des  ket_des : KETbra_des : BRAid_des : IDe0 : e0 ADD e1\n            | e0 SUB e1\n            | e1e1 : ket bra\n            | e2e2 : ket\n            | bra\n            | id ket : ketv\n            | cket bra : brav\n            | cbracket : CKETcbra : CBRAketv : KETbrav : BRAid : ID'
    
_lr_action_items = {'KET':([0,2,3,4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[18,18,-6,-3,-7,-8,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-5,-4,33,33,33,-19,-31,-16,-30,-32,-17,-9,]),'BRA':([0,2,3,4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[19,19,-6,-3,-7,-8,-18,31,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-5,-4,31,31,31,-19,-31,-16,-30,-32,-17,-9,]),'ID':([0,2,3,4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[20,20,-6,-3,-7,-8,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-5,-4,34,34,34,-19,-31,-16,-30,-32,-17,-9,]),'CKET':([0,2,3,4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[21,21,-6,-3,-7,-8,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-5,-4,21,21,21,-19,-31,-16,-30,-32,-17,-9,]),'CBRA':([0,2,3,4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[24,24,-6,-3,-7,-8,-18,24,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-5,-4,24,24,24,-19,-31,-16,-30,-32,-17,-9,]),'$end':([1,3,4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,30,31,32,33,34,35,36,],[0,-2,-3,-7,-8,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-1,-4,-19,-31,-16,-30,-32,-17,-9,]),'NL':([4,5,6,7,9,10,11,15,16,17,18,19,20,21,22,23,24,30,31,32,33,34,35,36,],[26,-7,-8,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-19,-31,-16,-30,-32,-17,-9,]),'ADD':([5,7,9,10,11,15,16,17,18,19,20,21,22,23,24,30,31,32,33,34,35,36,],[27,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-19,-31,-16,-30,-32,-17,27,]),'SUB':([5,7,9,10,11,15,16,17,18,19,20,21,22,23,24,30,31,32,33,34,35,36,],[28,-18,-21,-22,-20,-24,-25,-23,-30,-31,-32,-28,-26,-27,-29,-19,-31,-16,-30,-32,-17,28,]),'ASSIGN':([8,12,13,14,18,19,20,],[29,-10,-11,-12,-13,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'lines':([0,],[2,]),'line':([0,2,],[3,25,]),'expresion':([0,2,],[4,4,]),'e0':([0,2,29,],[5,5,36,]),'assign':([0,2,],[6,6,]),'e1':([0,2,27,28,29,],[7,7,32,35,7,]),'des':([0,2,],[8,8,]),'ket':([0,2,27,28,29,],[9,9,9,9,9,]),'bra':([0,2,9,27,28,29,],[10,10,30,10,10,10,]),'e2':([0,2,27,28,29,],[11,11,11,11,11,]),'ket_des':([0,2,],[12,12,]),'bra_des':([0,2,],[13,13,]),'id_des':([0,2,],[14,14,]),'ketv':([0,2,27,28,29,],[15,15,15,15,15,]),'cket':([0,2,27,28,29,],[16,16,16,16,16,]),'id':([0,2,27,28,29,],[17,17,17,17,17,]),'brav':([0,2,9,27,28,29,],[22,22,22,22,22,22,]),'cbra':([0,2,9,27,28,29,],[23,23,23,23,23,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> lines line','program',2,'p_program_mult','parser.py',13),
  ('program -> line','program',1,'p_program_single','parser.py',17),
  ('line -> expresion','line',1,'p_line','parser.py',21),
  ('line -> expresion NL','line',2,'p_line','parser.py',22),
  ('lines -> lines line','lines',2,'p_lines','parser.py',26),
  ('lines -> line','lines',1,'p_lines','parser.py',27),
  ('expresion -> e0','expresion',1,'p_expresion','parser.py',34),
  ('expresion -> assign','expresion',1,'p_expresion','parser.py',35),
  ('assign -> des ASSIGN e0','assign',3,'p_assign','parser.py',39),
  ('des -> ket_des','des',1,'p_des','parser.py',43),
  ('des -> bra_des','des',1,'p_des','parser.py',44),
  ('des -> id_des','des',1,'p_des','parser.py',45),
  ('ket_des -> KET','ket_des',1,'p_ket_des','parser.py',49),
  ('bra_des -> BRA','bra_des',1,'p_bra_des','parser.py',54),
  ('id_des -> ID','id_des',1,'p_id_des','parser.py',59),
  ('e0 -> e0 ADD e1','e0',3,'p_e0','parser.py',63),
  ('e0 -> e0 SUB e1','e0',3,'p_e0','parser.py',64),
  ('e0 -> e1','e0',1,'p_e0','parser.py',65),
  ('e1 -> ket bra','e1',2,'p_e1','parser.py',74),
  ('e1 -> e2','e1',1,'p_e1','parser.py',75),
  ('e2 -> ket','e2',1,'p_e2','parser.py',82),
  ('e2 -> bra','e2',1,'p_e2','parser.py',83),
  ('e2 -> id','e2',1,'p_e2','parser.py',84),
  ('ket -> ketv','ket',1,'p_ket','parser.py',88),
  ('ket -> cket','ket',1,'p_ket','parser.py',89),
  ('bra -> brav','bra',1,'p_bra','parser.py',93),
  ('bra -> cbra','bra',1,'p_bra','parser.py',94),
  ('cket -> CKET','cket',1,'p_cket','parser.py',99),
  ('cbra -> CBRA','cbra',1,'p_cbra','parser.py',104),
  ('ketv -> KET','ketv',1,'p_ketv','parser.py',110),
  ('brav -> BRA','brav',1,'p_brav','parser.py',115),
  ('id -> ID','id',1,'p_id','parser.py',120),
]
