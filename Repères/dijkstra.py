#!/usr/bin/python
# -*- coding: utf-8 -*-

def form(d,i,fait,inf):
  if d=="@":
    return " - |"
  elif d==inf:
    return " ∞ |"
  c=str(d)
  if i not in fait:
    if len(c)==1:
      return " "+c+" |"
    return " "*(3-len(c))+c+"|"
  return " * |"

M=[[0,12,0,14,0,0,0,0],
   [12,0,0,0,0,9,16,21],
   [0,0,0,0,13,10,0,0],
   [14,0,0,0,10,0,0,0],
   [0,0,13,10,0,16,0,10],
   [0,9,10,0,16,0,0,11],
   [0,16,0,0,0,0,0,11],
   [0,21,0,0,10,11,11,0]]

inf=len(M)*(max(max(l) for l in M)+1)
precedent=[-1 for s in range(len(M))]
distances=[inf for s in range(len(M))]
depart=ord("A")-65
arrivee=ord("H")-65
distances[depart]=0
fait=set()
afaire=set(range(len(M)))

print(" "+" | ".join(chr(i+65) for i in range(len(M)))+" | choix")

while afaire:
  dmin=inf
  for s in afaire:
    if dmin>distances[s]:
      dmin=distances[s]
      smin=s
  print("-"*(4*len(M)+7))
  print("".join(form(distances[i],i,fait,inf) for i in range(len(M)))+" "*3+chr(smin+65))
  print("".join(form(chr(precedent[i]+65),i,fait,inf) for i in range(len(M)))+" préc.")
  fait.add(smin)
  afaire.remove(smin)
  for s in afaire:
    if distances[smin]+M[s][smin]<distances[s] and M[s][smin]:
      distances[s]=distances[smin]+M[s][smin]
      precedent[s]=smin

s=arrivee
pluscourt=[s]
while s!=depart:
  s=precedent[s]
  pluscourt=[s]+pluscourt

print(distances[arrivee])
print("-".join([chr(i+65) for i in pluscourt]))
