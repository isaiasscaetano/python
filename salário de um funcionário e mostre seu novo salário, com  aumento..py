salario = float(input('qual e salario do fucionari? R$'))
novo = salario + (salario * 20 / 100)
print('um fucionario que ganhava R${:.2f}, com 20% de aumento, passa a receber R${:.2f}'.format(salario, novo))
