print ("Informe três números diferentes para serem organizados de forma crescente:")
x = 0
vetor = list(range(3))
while x < 3:
   vetor [x] = int(input('Informe um numero:'))
   x = x+1
   vetor.sort()
   print('Os números organizados de forma crescente correspondem a: ',vetor)