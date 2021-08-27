arq = open("Pontos-surf.csv", "r")
arq.seek(0,0)
mod = []
auxiliar = arq.readlines()
arq.seek(0,0)
cont = len(arq.read().split())
arq.seek(0,0)
str_arq = arq.read()
arq.seek(0,0)
agregar = []
vetor = []
z = 0
aux_medias = []
soma = []
for x in range(0, cont, 6):
    vetor.append(arq.read().split()[x])
    arq.seek(0,0)
    variação = "".join(vetor[z])
    str_arq = str_arq.replace(variação, "")
    arq.seek(0,0)
    z = z+1
for x in range(0, z):
    aux_maxmin = auxiliar[x].replace(vetor[x], "").replace(",","").split()
    maximo = max(aux_maxmin)
    minimo = min(aux_maxmin)
    mod.append(auxiliar[x].replace(maximo, "").replace(minimo, ""))
vet_aux = vetor
vetor = sorted(set(vetor))
for x in range(0, len(vetor)):
    for z in range(0, len(mod)):
        if vetor[x] in mod[z]:
            agregar.append(mod[z])
aux_medias = "".join(agregar)
for x in range(0, len(vetor)):
    aux_medias = aux_medias.replace(vetor[x],"")
split_aux = aux_medias.replace(",","").split()
for x in range(0, len(split_aux), 3):
    sintetizador = 0
    for z in range(x, x+3):
        sintetizador = float(split_aux[z]) + sintetizador
    soma.append(round(sintetizador/3, 2))
vet_aux = sorted(vet_aux)
prova_real = []
var_media = []
base = []
for x in range(0, len(vet_aux)):
    testando = vet_aux[x], soma[x]
    prova_real.append(testando)
prova_real = list(prova_real)
for x in range(0, len(vetor)):
    for z in range(0, len(prova_real)):
        if vetor[x] in prova_real[z]:
            var_media.append(prova_real[z][1])
        if z == len(prova_real)-1:
            var_media.append("\n")
for x in range(0, len(var_media)):
    listagem = [str(i) for i in var_media]
var_media = " ".join(listagem).split("\n")
notas_final = 0
k = 0
prova_real.clear()
for x in range(0, len(var_media)-1):
    var_media[x] = sorted(var_media[x].split())[len(var_media[x].split())-2:len(var_media[x].split())]
    notas_final = 0
    for z in range(0,2):
        notas_final = float(var_media[x][z]) + notas_final
    if x != len(var_media)-1:
        print("".join(vetor[k]).replace(",", " -"), round(notas_final, 2))
    k = k+1