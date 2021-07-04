# -*- coding: utf-8 -*-

import sys
import io
import nltk

def pre_check(s: str):
  s = s.strip()
  print(s)
  if s.endswith("1"):
    n1 = s.count("1")
    n2 = s.count("2")
    n3 = s.count("3")
    if n1 % 2 != 0:
      print("# 1's not even")
    if n2 % 2 != 0:
      print("# 2's not even")
    if n3 % 2 == 0:
      print("# 3's even")
  else:
    print("does not end in 1")

def parse(s):
    pre_check(s)
    grammar = """
    S  -> Q6
    Q0 -> '1' Q4 | '2' Q2 | '3' Q1
    Q1 -> '1' Q5 | '2' Q3 | '3' Q0
    Q2 -> '1' Q6 | '2' Q0 | '3' Q3
    Q3 -> '1' Qf | '2' Q1 | '3' Q2
    Q4 -> '1' Q0 | '2' Q6 | '3' Q5
    Q5 -> '1' Q1 | '2' Q7 | '3' Q4
    Q6 -> '1' Q2 | '2' Q4 | '3' Q7
    Q7 -> '1' Q3 | '2' Q5 | '3' Q6
    Qf -> '1' Q3 | '2' Q5 | '3' Q6
    Qf ->
    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = list(s.strip())
    parser = nltk.ChartParser(grammar)
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
    except ValueError as e:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
