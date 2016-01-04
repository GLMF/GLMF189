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
compteur=0

while afaire:
  temp=set()
  for s in afaire:
    temp|=M[s]
  afaire=set(temp)
  compteur+=1

print(compteur)
