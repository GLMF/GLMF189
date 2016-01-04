#!/usr/bin/python
# -*- coding: utf-8 -*-

M={"A":{"B","C"},
   "B":{"A","E"},
   "C":{"A","D","F"},
   "D":{"C","I"},
   "E":{"B","G","H"},
   "F":{"C"},
   "G":{"E"},
   "H":{"E"},
   "I":{"D"}}

mini=len(M)
for s in M:
  compteur=-1
  afaire={s}
  fait=set()
  while afaire:
    temp=set()
    for so in afaire:
      temp|=M[so]
    temp-=fait
    temp-=afaire
    fait|=afaire
    afaire=set(temp)
    compteur+=1
  if mini>compteur:
    smini=s
    mini=compteur

print(smini,mini)
