try:
    x = int(input('Digite um número: '))
    y = int(input('Digite um outro número: '))
    print(x, '/', y, '=', x / y)
except ValueError:
    print('Valores não válidos! Digite números inteiros')
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print(x, '/', y, '=', x / y)
except ZeroDivisionError:
    print('É impossível fazer divisão por 0! Digite outro valor')
    x = int(input('Digite um número: '))
    y = int(input('Digite um outro número: '))
    print(x, '/', y, '=', x / y)