#!/bin/python3
from parser import parser
from process.link import link
from process.types import types
from process.execute import execute
import argparse

p = argparse.ArgumentParser(prog='main.py',  description="QSL Interpreter")
p.add_argument('program', nargs="?", help="path of the program to interpret")
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
        ast = parser.parse(s)
        result = ast.visit(vlink)
        print(result)
else:
    with open(args.program) as f:
        data = f.read()
        print(data)
        ast = parser.parse(data)
        for line in ast.lines:
            line.visit(vlink)
            line.visit(vtype)
            result = line.visit(vexp)
            print(line.value)