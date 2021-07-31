n = int(input('Digite um número: '))
fat = 1
for a in range (n,1,-1):
    fat = fat*a
    print('O',n,'! é igual a:',fat)