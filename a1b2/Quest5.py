dic = {'UUU':'Fenil-alanina', 'UUC':'Fenil-alanina',
 'UUA':'Leucina', 'UUG':'Leucina','CUU':'Leucina', 'CUC':'Leucina','CUA':'Leucina', 'CUG':'Leucina',
 'AUU':'Isoleucina', 'AUC':'Isoleucina','AUA':'Isoleucina','AUG':'start codon',
 'GUU':'Valina', 'GUG':'Valina','GUA':'Valina', 'GUC':'Valina',
 'UCU':'Serina', 'UCC':'Serina','UCA':'Serina','UCG':'Serina',
 'CCU':'Prolina','CCC':'Prolina', 'CCA':'Prolina','CCG':'Prolina',
 'ACU':'Treonina','ACC':'Treonina', 'ACA':'Treonina','ACG':'Treonina',
 'GCU':'Alanina','GCC':'Alanina', 'GCA':'Alanina','GCG':'Alanina',
 'UAU':'Tirosina','UAC':'Tirosina', 'UAA':'Stop codon','UAG':'Stop codon',
 'CAU':'Histidina', 'CAC':'Histidina','CAA':'Glutamina','CAG':'Glutamina',
 'AAU':'Asparagina','AAC':'Asparagina','AAA':'Lisina', 'AAG':'Lisina',
 'GAU':'Acido aspartico', 'GAC':'Acido aspartico','GAA':'Acido Glutamico', 'GAG':'Acido Glutamico',
 'UGU':'Cysteine','UGC':'Cysteine', 'UGA':'Stop codon','UGG':'Tryptophan',
 'CGU':'Arginina','CGC':'Arginina', 'CGA':'Arginina','CGG':'Arginina',
 'AGU':'Serina', 'AGC':'Serina','AGA':'Arginina', 'AGG':'Arginina',
 'GGU':'Glicina', 'GGC':'Glicina','GGA':'Glicina','GGG':'Glicina'}
from os import replace
with open('ExemplosDNA.txt', 'r') as var:
 recebevar = var.readlines()
print (recebevar)
i=0
while i < len(recebevar):
 x = recebevar[i]
 a1 = x.replace("A","u")
 a2 = a1.replace("T","a")
 a3 = a2.replace("G","c")
 a4 = a3.replace("C","g")
 print('\n')
 print(('linha'),(i+1),('linha original: '),(x))
 print(('linha transcrita'),(i+1),(':'),(a4.upper()))
 a4 = a4.upper()
 j=0
 print('Sintetização de aminoácidos (depois do start ) ')
 for j in range(3, len(a4), 1):
  v1= ''
  v1 = a4[j-3]
  v1 += a4[j-2]
  v1 += a4[j-1]
 if dic[v1]=='start codon':
  k=j+1
 print (dic[v1])
 for j in range(k, len(a4), 1):
  v1= ''
  v1 = a4[j-3]
  v1 += a4[j-2]
  v1 += a4[j-1]
 if (dic[v1])=='Stop codon':
    break
 else:
    print (dic[v1])
 break
 i=i+1