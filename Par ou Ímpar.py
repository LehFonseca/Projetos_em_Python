numero = int(input('Digite um número inteiro: '))
resultado = numero % 2
if resultado == 0:
    print('Seu numero {} é par.'.format(numero))
else:
    print('Seu número {} é ímpar.'.format(numero))