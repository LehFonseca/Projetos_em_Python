n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))
if media < 5:
    print('Sua média foi {}. Você está REPROVADO!'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi {}. Você está de RECUPERAÇÃO!'.format(media))
elif media >= 7.0:
    print('Parabéns! Sua média foi {}. Você está APROVADO!'.format(media))
