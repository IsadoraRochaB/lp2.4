print('Digite números para que se possa calcular a média')
laço = int(input('Digite um número: '))
n=0
s = 0
while laço != 0:
    s = s + laço
    laço = int(input('Digite  um número: '))
    n=n+1
    print('A média dos números é : ', s/n)