# -*- coding: utf-8 -*-
import re
import sys

from enum import Enum

class States(Enum):
    init = 0
    h_found = 1
    ht_found = 2
    htt_found = 3
    http_found = 4
    hashtag_found = 5
    at_found = 6

def programa(texto):
    state = States.init # current iteration state
    emptysym = False # used to test emptyness in hashtags end mentions

    result=[]
    for c in texto:
        if state == States.init:
            if c == '@':
                state = States.at_found
                emptysym = True
            elif c == '#':
                state = States.hashtag_found
                emptysym = True
            elif c == 'h':
                state = States.h_found
            else:
                result.append(c)
        elif state == States.h_found:
            if c == 't':
                state = States.ht_found
            else:
                result.append('h' + c)
                state = States.init
        elif state == States.ht_found:
            if c == 't':
                state = States.htt_found
            else:
                result.append('ht' + c)
                state = States.init
        elif state == States.htt_found:
            if c == 'p':
                state = States.http_found
            else:
                result.append('htt' + c)
                state = States.init
        elif state == States.http_found:
            if c.isspace(): ## assume urls end only with a space
                result.append(c)
                state = States.init
        elif state in (States.hashtag_found, States.at_found):
            if c != '_' and not c.isalnum():
                if emptysym:
                    result.append('@' if state == States.at_found else '#')
                result.append(c)
                state = States.init
            elif emptysym:
                emptysym = False
    return ''.join(result)

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
