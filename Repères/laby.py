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

precedent=dict()
afaire={entree}
fait=set()

while generateur not in afaire:
  temp=set()
  for s in afaire:
    tempo=M[s]-fait-afaire
    for so in tempo:
      precedent[so]=s
    temp|=tempo
  fait|=afaire
  afaire=set(temp)

s=generateur
pluscourt=[s]

while s!=entree:
  s=precedent[s]
  j,i=s
  L[j]=L[j][:i]+"+"+L[j][i+1:]
  pluscourt=[s]+pluscourt

for l in L:
  print(l)
print(len(pluscourt)-1)
