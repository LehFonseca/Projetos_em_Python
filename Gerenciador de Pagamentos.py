print('{:=^40}'.format(' LOJAS FONSECA'))
preço = float(input('Qual o valor das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão débito
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} - SEM JUROS!.')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} - COM JUROS!')
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
