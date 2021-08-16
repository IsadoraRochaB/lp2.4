with open('ExemplosDNA.txt', 'r') as var:
    recebevar = var.readlines()
print (recebevar)
print('\n')
i = 0
while i < len(recebevar):
 x = recebevar[i]
print(("Presença de Citocina"),(x.count('C')),('vezes na'),('linha'),(i+1
))
print(("Presença de Guanina"),(x.count('G')),('vezes na'),('linha'),(i+1)
)
print(("Presença de Timina"),(x.count('T')),('vezes na'),('linha'),(i+1))
print(("Presença de Adenina"),(x.count('A')),('vezes na'),('linha'),(i+1)
)
print('\n\n')
i=i+1
