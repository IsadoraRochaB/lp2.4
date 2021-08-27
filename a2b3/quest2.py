print('----INTEGRANTES E DATAS----')
N, M = [int(value) for value in input('\n-> Informe, respectivamente, o total de amigos do grupo e o total de dias em que houve reunião: ').split()]

print('\n----IDENTIFICADOR----')
I, R = [int(value) for value in input('\n-> Informe, respectivamente, o nº de amigo(s) infectado(s) externamente e o número da primeira reunião em que ele(s) participou(ram) infectado(s): ').split()]

restricoes = False

restricoes = True if 2<N and N<1000 else restricoes
restricoes = True if 2<M and M<1000 else restricoes
restricoes = True if 1<I and I<N else restricoes
restricoes = True if 1<R and R<M else restricoes

reunioes = []
infectados = {I}

print('\n----INFORMAÇÕES EM SEQUÊNCIA----')
print('*A primeira linha descreve os participantes da reunião 1, a segunda linha descreve os participantes da reunião 2 e assim por diante\n')

for value in range(M):
    reunioes.append([int(value) for value in input('-> ').split()])
    restricoes = True if 1<reunioes[-1][0] and reunioes[-1][0]<N else restricoes
    reunioes[-1].pop(0)
    restricoes = True if any(P<1 and N<P for P in reunioes[-1]) else restricoes

if restricoes:
    for i in range (R-1, M):
        if any(pessoa in infectados for pessoa in reunioes[i]):
            infectados.update(reunioes[i])

print('\n----TOTAL DE INFECTADOS----')
print(len(infectados))