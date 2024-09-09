peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / (altura ** 2) # Ou podendo fazer (altura * altura).
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA!')
