import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pylab as plt

def propiedades(red):
    # Diccionario a retornar
    caract = {}
    # NumPy Array con los grados de todos los nodos
    d = np.array([grado for nodo, grado in red.degree()])
    
    caract['Nodos'] = red.number_of_nodes()
    caract['Enlaces'] = red.number_of_edges()
    #caract['Dirigida'] = esDirigido(red)
    caract['Grado max'] = d.max()
    caract['Grado min'] = d.min()
    caract['Grado promedio'] = d.mean()
    caract['Densidad'] = caract['Enlaces'] / ((caract['Nodos']) * (caract['Nodos'] - 1) / 2)
    caract['Clustering medio'] = nx.average_clustering(red)
    caract['Transitividad'] = nx.transitivity(red)
    comps = list(nx.connected_component_subgraphs(red))
    diams = np.array([])
    for comp in comps:
        diams = np.append(diams, nx.diameter(comp))
    caract['Diámetro'] = int(diams.max())
        
    return caract

def esDirigido(file):

    with open(file,"r") as f:
        vecinos = defaultdict(set)
        i = 0
        s = True
        for line in f:
            a = line.rstrip('\n').split('\t')
            v = a[0]
            w = a[1]
            vecinos[v].add(w)
            i += 1
            if v in vecinos[w] and  w!=v:
                return True
            elif v == w and s:
                print("Warning:", file, "no es un grafo simple.")
                s = False
            
        return False

def intersect(l1, l2): 
# Intersección entre dos listas.
    l3 = [value for value in l1 if value in l2] 
    return l3
