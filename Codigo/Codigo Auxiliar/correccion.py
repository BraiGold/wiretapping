import sys, os
from math import log as LOG

archivoCapturasViejo = open('./capturas_s2.csv','r')
entr,maxentr =archivoCapturasViejo.readline().split(',')

S2 = {}
total_packt = 0
for line in archivoCapturasViejo:
    symbol,p,inf,cant = line.split(",")
    print(cant)
    total_packt += float(cant)
    S2[symbol] = float(cant)


entropia = 0
for s_i in S2:
    p =  float(S2[s_i]) / (total_packt)
    print (s_i + '                 ' + str( p ) + '                 '+  str( LOG(1/p,2) ) )
    entropia -= p * LOG(p,2)

archivoCapturas = open('./capturas_s2_corregido.csv' , 'w+')
archivoCapturas.write(str(entropia)+','+str( LOG(len(S2),2) )+'\n')
for key in S2:
    p =  float(S2[key]) / (total_packt)
    archivoCapturas.write(key  + ','+str(p)+','+ str( LOG(1/p,2) )+','+ str(S2[key])+ '\n')
