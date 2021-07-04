# -*- coding: utf-8 -*-

import sys
import io
import nltk

def parse(s):
    grammar = """
    S -> Par | Add | Sub | Mul | Div| Exp | Abs | Num
    D -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    D -> '0' D | '1' D | '2' D | '3' D | '4' D | '5' D | '6' D | '7' D | '8' D | '9' D
    Num -> D | '.' D | D '.' D | '-' Num
    Par -> '(' S ')'
    Add -> S ' ' '+' ' ' S
    Sub -> S ' ' '-' ' ' S
    Mul -> S ' ' '*' ' ' S
    Div -> S ' ' '/' ' ' S
    Exp -> S '^' S
    Abs -> '|' S '|'
    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = list(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
