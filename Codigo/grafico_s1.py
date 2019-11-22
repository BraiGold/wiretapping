import sys, os
from math import log as LOG

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple



fileS1 = open('./capturas_s1.csv','r')

entropiaFuente,entropiaMaxima = map(float , fileS1.readline().split(","))
print(entropiaFuente)
print(entropiaMaxima)
Unicast = []
Broadcast = []
cantUni = []
cantBroad = []
labels = []
type_position = {}
for line in fileS1:
    uniOBroad,type,p,inf,cant = line.split(",")
    if type in type_position:
        if uniOBroad == "Unicast":
            Unicast[type_position[type]] = float(inf)
            cantUni[type_position[type]] = float(cant)
        else:
            Broadcast[type_position[type]] = float(inf)
            cantBroad[type_position[type]] = float(cant)
    else:
        labels.append(type)
        type_position[type]= len(Unicast)
        if uniOBroad == "Unicast":
            Unicast.append(float(inf))
            Broadcast.append(float(0))
            cantUni.append(float(cant))
            cantBroad.append(float(0))
        else:
            Unicast.append(float(0))
            Broadcast.append(float(inf))
            cantUni.append(float(0))
            cantBroad.append(float(cant))


n_groups = len(Unicast)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, Unicast, bar_width,
                alpha=opacity, color='b',
                label='Unicast')

rects2 = ax.bar(index + bar_width, Broadcast, bar_width,
                alpha=opacity, color='r',
                label='Broadcast')

ax.set_xlabel('type / Protocolo')
ax.set_ylabel('Cantidad De Informacion')
ax.set_title('Cantidad de informacion por simbolo')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

ax.axhline(entropiaMaxima, color="gray",linestyle='--')
ax.text(1.02, entropiaMaxima, "entropia maxima", va='center', ha="left", bbox=dict(facecolor="w"))
ax.axhline(entropiaFuente, color="gray",linestyle='--')
ax.text(1.02, entropiaFuente, "entropia fuente", va='center', ha="left", bbox=dict(facecolor="w"))
plt.show()



#pie charts




sizes = np.array(cantUni) + np.array(cantBroad)
explode =[min(100/k,1) for k in sizes]
# Plot
fig,ax = plt.subplots()
ax.set_title('Porcentaje Trafico Por protocolo')
plt.pie(sizes, labels=labels, autopct='%1.1f%%',explode =explode, startangle= 70)

plt.axis('equal')
plt.show()




# Plot
sizes = (np.sum(cantBroad),np.sum(cantUni))
fig,ax = plt.subplots()
ax.set_title('Porcentaje Trafico Unicast/Broadcast')
plt.pie(sizes, labels=('Broadcast','Unicast'), autopct='%1.1f%%', startangle=150)

plt.axis('equal')
plt.show()
