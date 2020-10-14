#!/bin/python3
from lexer import lextok
from parserqsl import parser
from process.link import link
from process.types import types
from process.execute import execute
import argparse

p = argparse.ArgumentParser(prog='main.py',  description="QSL Interpreter")
p.add_argument('program', nargs="?", help="path of the program to interpret")
p.add_argument('-t', '--tokens', action="store_true", help="Display the list of tokens instead of executing the program")
args = p.parse_args()

tv = {}
vlink = link(tv)
vtype = types()
vexp = execute()

if (args.program is None):
    while True:
        try:
            s = input('QSL> ')
        except EOFError:
            break
        if not s: continue
        lextok.input(s)
        if args.tokens:
            # Tokenize
            while True:
                tok = lextok.token()
                if not tok: 
                    break      # No more input
                print(tok)
        ast = parser.parse(s)
        ast.visit(vlink)
        ast.visit(vtype)
        ast.visit(vexp)
        print(ast.value)
else:
    with open(args.program) as f:
        data = f.read()
        if args.tokens:
            # Tokenize
            while True:
                tok = lextok.token()
                if not tok: 
                    break      # No more input
                print(tok)
        ast = parser.parse(data)
        for line in ast.lines:
            line.visit(vlink)
            line.visit(vtype)
            result = line.visit(vexp)
            print(line.value)