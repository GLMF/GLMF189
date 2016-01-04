#!/usr/bin/python
# -*- coding: utf-8 -*-

L=["###############",
   "E #   #       #",
   "# # ### ##### #",
   "#       #     #",
   "#### #### #####",
   "#    #    #   #",
   "# # ####### # #",
   "G #         # #",
   "###############"]

M=dict()
lon=len(L[0])
lar=len(L)

for j in range(lar):
  for i in range(lon):
    if L[j][i]=="#":
      continue
    if L[j][i]=="E":
      entree=(j,i)
    elif L[j][i]=="G":
      generateur=(j,i)
    M[(j,i)]=set()
    if i>0 and L[j][i-1]!="#":
      M[(j,i)].add((j,i-1))
    if i+1<lon and L[j][i+1]!="#":
      M[(j,i)].add((j,i+1))
    if j>0 and L[j-1][i]!="#":
      M[(j,i)].add((j-1,i))
    if j+1<lar and L[j+1][i]!="#":
      M[(j,i)].add((j+1,i))

compteur=0
afaire={generateur}
fait=set()

while afaire:
  temp=set()
  for s in afaire:
    temp|=M[s]
  temp-=fait
  temp-=afaire
  fait|=afaire
  afaire=set(temp)
  compteur+=1

print(compteur-1)
