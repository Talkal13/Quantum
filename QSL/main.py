#!/bin/python3
from lexer import lexer_qsl
from parserqsl import parser_qsl
from process.link import link
from process.types import types
from process.execute import execute
from process.load import load
from process.print import printkb
from process.slink import slink
import argparse

p = argparse.ArgumentParser(prog='main.py',  description="QSL Interpreter")
p.add_argument('program', nargs="?", help="path of the program to interpret")
p.add_argument('-t', '--tokens', action="store_true", help="Display the list of tokens instead of executing the program")
args = p.parse_args()

lqsl = lexer_qsl().build()
parser = parser_qsl().build(lexer_qsl())

tv = {}
vload = load(parser)
vlink = link(tv)
slin = slink()
vtype = types()
vexp = execute()
vprint = printkb()

if (args.program is None):
    while True:
        try:
            s = input('QSL> ')
        except EOFError:
            break
        if not s: continue
        lqsl.input(s)
        if args.tokens:
            # Tokenize
            while True:
                tok = lqsl.token()
                if not tok: 
                    break      # No more input
                print(tok)
        ast = parser.parse(s, lexer=lqsl)
        ast.visit(vload)
        ast.visit(vlink)
        ast.visit(slin)
        ast.visit(vtype)
        ast.visit(vexp)
else:
    with open(args.program) as f:
        data = f.read()
        lqsl.input(data)
        if args.tokens:
            while True:
                tok = lqsl.token()
                if not tok: 
                    break      # No more input
                print(tok)
        ast = parser.parse(data, lexer=lqsl)
        for line in ast.lines:
            line.visit(vload)
            line.visit(vlink)
            line.visit(slin)
            line.visit(vtype)
            result = line.visit(vexp)
            line.visit(vprint)