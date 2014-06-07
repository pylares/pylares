# -*- coding: utf-8 -*-

import sys

def _ValidarParametro(variable, nombre, tipos):
    if not isinstance(variable, tipos):
        raise(ValueError("El parámetro '" + nombre + "' es de un tipo inválido"))


def py23_unicode(var):
    if sys.version_info < (3,0,0):
        return unicode(var)
    else:
        return str(var)


def py23_iteritems(diccionario):
    try:
        return diccionario.iteritems()
    except:
        return diccionario.items()
