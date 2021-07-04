# -*- coding: utf-8 -*-

import sys
import io
import nltk

def parse(s):
    grammar1 = """
    S -> '(' ')' | '(' N ' ' S ' ' S ')'
    d -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    D -> d | d D
    N -> D | '.' D | D '.' D | '-' N
    """
    grammar = nltk.CFG.fromstring(grammar1)
    s_tokenized = list(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))
    return tree[0] if len(tree) > 0 else False

def invert_tree(tree):
  if len(tree) <= 1:
    return tree
  else:
    num = tree[1] # tree[0] = '('
    if type(num) is nltk.Tree and num.label() == 'N':
      if num[0] == '-': # (D ...) or (- (N ...))
        tmp = tree[3]
        tree[3] = invert_tree(tree[5]) # tree[2] = ' '
        tree[5] = invert_tree(tmp)     # tree[4] = ' '
      else:
        tree[3] = invert_tree(tree[3]) # tree[2] = ' '
        tree[5] = invert_tree(tree[5])# tree[4] = ' '
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
          salida = "".join(invert_tree(tree).leaves())
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
