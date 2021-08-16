from os import replace
with open('ExemplosDNA.txt', 'r') as var:
 recebevar = var.readlines()
print (recebevar)
i=0
while i < len(recebevar):
 x = recebevar[i]
 a1 = x.replace("A","u")
 a2 = a1.replace("T","a")
 a3 = a2.replace("G","c")
 a4 = a3.replace("C","g")
 print('\n')
 print(('liinha'),(i+1),(' linha original: '),(x))
 print(('linha transcrita'),(i+1),(':'),(a4.upper()))
 i=i+1
