import sys, os
from math import log as LOG
from scapy.all import *


total_packt = 10000
pkts=sniff( count= total_packt)


S = {}
for i in range(total_packt):
    key = ''
##    print 'protocolo: ' + pkts[i].name
    if (pkts[i][0].dst == 'ff:ff:ff:ff:ff:ff'):
        key = 'Broadcast,' +str(pkts[i][0].payload.name)
    else:
        key = 'Unicast,' +str(pkts[i][0].payload.name)

    if( key in S):
        S[key] += 1
    else:
        S[key] = 1



# calculo  probabilidad entropia e informacion y muestro tabla
print '      simbolo                    probabilidad             informacion'
entropia = 0
for s_i in S:
    p =  float(S[s_i]) / total_packt
    print s_i + '                 ' + str( p ) + '                 '+  str( LOG(1/p,2) )
    entropia -= p * LOG(p,2)

print 'Entropia de la fuente: ' + str(entropia)
print 'Entropia maxima: ' + str( LOG(len(S),2) )



#guardo la captura en csv
archivoCapturas = open('./capturas_s1.csv' , 'w+')
archivoCapturas.write(str(entropia)+','+str( LOG(len(S),2) ) + '\n')
for key in S:
    p =  float(S[key]) / total_packt
    archivoCapturas.write(key  + ',' + str(p) +','+str( LOG(1/p,2) )+','+str(S[key]) +'\n')
