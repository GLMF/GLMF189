#!/usr/bin/python
# -*- coding: utf-8 -*-

M={"A":{"B","C"},
   "B":{"F","G"},
   "C":{"D","E"},
   "D":{"F","G","I"},
   "E":{"H"},
   "F":{"J"},
   "G":{"I","J","K","L"},
   "H":{"G","K"},
   "I":set(),
   "J":{"I"},
   "K":set(),
   "L":set()}

afaire={"A"}
precedent={c:(None,0) for c in M}
compteur=0

while afaire:
  compteur+=1
  temp=set()
  for s in afaire:
    for so in M[s]:
      precedent[so]=(s,compteur)
    temp|=M[s]
  afaire=set(temp)

compteur-=1
for s in precedent:
  if precedent[s][1]==compteur:
    break
print(compteur,s)

pluslong=[]
while s!=None:
  pluslong=[s]+pluslong
  s=precedent[s][0]
print("-".join(pluslong))
