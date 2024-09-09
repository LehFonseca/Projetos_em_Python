n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O número {} é maior que o {}.'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o {}.'.format(n2, n1))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
# Podendo fazer else direto, porque ou o número é maior ou menor, assim sendo iguais.
