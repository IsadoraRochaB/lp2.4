palavra = str(input('Digite uma palavra: '))
contrário = (palavra[::-1])
if palavra == contrário:
   print('Esta palavra é um palíndromo')
else:
   print('Esta palavra não é um palíndromo')