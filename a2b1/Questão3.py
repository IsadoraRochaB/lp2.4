def somaNum(a, b):
    if (a + b) > 1000:
        raise OverflowError
    else:
        return a + b
try:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('A soma dos valores é: ', somaNum(v1, v2))
except ValueError:
    print('Valores inválidos! Digite números inteiros')
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('A soma dos valores é: ', somaNum(v1, v2))
except OverflowError:
    print('Valores inválidos! Digite números onde a soma irá dará um valor menor que 1000')
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('A soma dos valores é:', somaNum(v1, v2))
