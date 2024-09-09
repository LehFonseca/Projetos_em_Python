from datetime import date
atual = date.today().year
nascimento = int(input("Qual a data de nascimento do atleta? "))
idade = atual - nascimento
if idade <= 9:
    print('O atleta tem {} anos, e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, e está na categoria JÚNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, e está na categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos, e está na categoria MASTER'.format(idade))
