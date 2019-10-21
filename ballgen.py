# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:54:47 2019

@author: Alexis
"""


def ballGenerator(d, plain = False):
    """Generate text code for a filtration of the d-ball, or the d-1-sphere if plain is set to false.
    The filtration used is a simplicial filtration of a d dimension tetraedra, where value is set equal to dim
    in order to ensure that the creation is consistent.
    A d dimension tetraedra contains all the possible simplex in it so the code simply has to generate all the 
    strictly increasing tuples of all the dimensions less than d"""
    l = []
    nbpoints = d + 1
    for i in range(d):
        dim = i
        val = i
        vertices = list(range(dim + 1))
        while vertices[0] >= 0:
            nextline = str(val) + " " + str(dim)
            for indice in vertices:
                nextline += " " + str(indice)
            l.append(nextline)
            for k in range(dim, -1, -1):
                vertices[k] += 1
                if vertices[k] >= nbpoints - dim + k:
                    vertices[k] = -1
                else:
                    break
            for k in range(1, dim + 1):
                if vertices[k] == -1:
                    vertices[k] = vertices[k-1] + 1
    if plain:
        nextline = str(d) + " " + str(d)
        for i in range(nbpoints):
            nextline += " " + str(i)
        l.append(nextline)
    return l
            