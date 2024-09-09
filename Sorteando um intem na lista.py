#import random
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista) = quando usado com o import random
escolhido = choice(lista) #quando usado com o from / import
print('O aluno escolhido foi {}.'.format(escolhido))
