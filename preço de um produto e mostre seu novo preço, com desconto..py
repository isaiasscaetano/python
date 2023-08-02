preços = float(input('qual e o preço do produto:'))
novo = preços - (preços * 5 /100)
print('o produto que custava R${}, na promoçao com desconto de 5% vai gustar R${}'.format(preços, novo))
