from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = int(input('''Qual seu sexo? 
[ M ] = 1
[ F ] = 2 \n'''))
masc = 1
fem = 2
idade = atual - nasc
print('Quam nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18 and sexo == 1:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade == 18 and sexo == 2:
    print('Você não precisa se alistar.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
if sexo == 1:
    print('Você é do sexo Masculino, então tem que se alistar.')
elif sexo == 2:
    print('Você é do sexo Feminino, não é necessário o alistamento.')
