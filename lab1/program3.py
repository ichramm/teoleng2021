# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    tags = clases = ids = 0
    for m in re.finditer(r'^(\w+\s*\{)|(\.\w+\s*\{)|(#\w+\s*\{)', texto, flags=re.M):
        if m.group(1):
            tags += 1
        elif m.group(2):
            clases += 1
        elif m.group(3):
            ids += 1
    return f'tags: {tags}\nclases: {clases}\nids: {ids}'

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
