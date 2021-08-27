D = int(input('Insira a quilometragem alcançada pela partícula: '))
D -= 5
(D%8)
if (D%8 <= 3):
    print (('Essa partícula atingiu o sensor'),(D%8))
else:
    print ('Essa partícula não chegou a atingir algum sensor')