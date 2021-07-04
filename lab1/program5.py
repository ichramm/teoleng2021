# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    m = re.finditer(r'^([#\.]?\w+)\s*\{\s*$[^}]*^\s*color: (rgb\([^;]+);', texto, flags=re.M)
    texto = ''.join(f'{a.groups()[0]} {a.groups()[1]}\r\n' for a in m)
    return texto

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
