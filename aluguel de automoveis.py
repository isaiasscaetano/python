dias = int(input('quais dias o automovel foi alugado:'))
km = float(input(' kms rodado do aumtomovel:'))
valor = (dias * 60) +  (km * 0.20)
print('o valor total do automovel e de R${:.2f}'.format(valor))
           
