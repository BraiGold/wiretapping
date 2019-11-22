import sys, os
from math import log as LOG
from scapy.all import *

total_packt = 10
pkts=sniff(filter="arp",count= total_packt)

S2= {}
for pkt in pkts:
    #pkt.show()
    if pkt.psrc in S2:
        S2[pkt.psrc] += 1
    else:
        S2[pkt.psrc] = 1
    if pkt.pdst in S2:
        S2[pkt.pdst] += 1
    else:
        S2[pkt.pdst] = 1


print "-------------"
#print S2




# calculo  probabilidad entropia e informacion y muestro tabla
print '      simbolo                    probabilidad             informacion'
entropia = 0
for s_i in S2:
    p =  float(S2[s_i]) / (total_packt*2)
    print s_i + '                 ' + str( p ) + '                 '+  str( LOG(1/p,2) )
    entropia -= p * LOG(p,2)

print 'Entropia de la fuente: ' + str(entropia)
print 'Entropia maxima: ' + str( LOG(len(S2),2) )


archivoCapturas = open('./capturas_s2.csv' , 'w+')
archivoCapturas.write(str(entropia)+','+str( LOG(len(S2),2) )+'\n')
for key in S2:
    p =  float(S2[key]) / (total_packt*2)
    archivoCapturas.write(key  + ','+str(p)+','+ str( LOG(1/p,2) )+','+ str(S2[key])+ '\n')



# creo grafo s2:
G = {}
for pkt in pkts:
    if pkt[ARP].op == 1:
        if pkt[ARP].psrc in G:
            G[pkt[ARP].psrc].add(pkt[ARP].pdst)
        else:
            G[pkt[ARP].psrc] = set()
            G[pkt[ARP].psrc].add(pkt[ARP].pdst)


#guardo grafo en archivo
archivoG = open('./grafoS2.csv','w+')
for v in G:
    archivoG.write(v)
    for e in G[v]:
        archivoG.write(','+ e)
    archivoG.write('\n')
