import sys, os
from math import log as LOG

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple



fileS1 = open('./capturas_s2.csv','r')

entropiaFuente,entropiaMaxima = map(float , fileS1.readline().split(","))
print(entropiaFuente)
print(entropiaMaxima)
informationPerSymbol = []
labels =[]
for line in fileS1:
    symbol,p,inf,cant = line.split(",")
    labels.append(symbol)
    informationPerSymbol.append(float(inf))

print(informationPerSymbol)
objects = labels
y_pos = np.arange(len(objects))
performance = informationPerSymbol

fig, ax = plt.subplots()

ax.bar(y_pos, performance, align='center', alpha=0.5)


ax.set_xlabel('simbolo')
ax.set_ylabel('Cantidad De Informacion')
ax.set_title('Cantidad de informacion por simbolo')
ax.set_xticks(y_pos)

#ajustar el label a cuantos digitos quieras mostrar
labels2 = [hex(int(l.split('.')[3]))[2:] for l in labels]
ax.set_xticklabels(labels2)
#ax.legend()

ax.axhline(entropiaMaxima, color="gray",linestyle= '--')
ax.text(1.02, entropiaMaxima, "entropia maxima", va='center', ha="left", bbox=dict(facecolor="w"))
ax.axhline(entropiaFuente, color="gray",linestyle='--')
ax.text(1.02, entropiaFuente, "entropia fuente", va='center', ha="left", bbox=dict(facecolor="w"))
plt.show()


import networkx as nx
G = nx.Graph()
ip_to_node = {}

i = 0
archivoG = open('./grafoS2.csv','r')
for line in archivoG:
    verticeYejes = line[:-1].split(',')
    for VoE in verticeYejes:
        if VoE not in ip_to_node:
            ip_to_node[VoE] = i
            i += 1

archivoG.close()

for key in ip_to_node:
    G.add_node(ip_to_node[key])

#print('-------------------------------------------------------------------------------  ')
#print (ip_to_node['192.168.1.35'])
archivoG = open('./grafoS2.csv','r')
for line in archivoG:
    verticeYejes = line[:-1].split(',')
    G.add_edges_from(map(lambda x: (ip_to_node[verticeYejes[0]] , ip_to_node[x]),verticeYejes[1:] )    )
archivoG.close()

print('tamanio grafo' +str(len(G)))
nx.draw_shell(G, node_size=30,width=0.5,node_color='blue')
plt.show()
from graphviz import Digraph

dot = Digraph(comment='Grafo de mensajes')
ejes = []
archivoG = open('./grafoS2.csv','r')
for line in archivoG:
    verticeYejes = line[:-1].split(',')
    dot.node(verticeYejes[0], verticeYejes[0])
    for e in verticeYejes[1:]:
        dot.edge(verticeYejes[0], e)

#
dot.render('./grafoDibujo.gv', view=True)
