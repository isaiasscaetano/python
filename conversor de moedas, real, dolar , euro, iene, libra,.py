real = float(input('digite o quantos reais vc tem? R$'))
dolar = real / 4.81
euro = real / 5.41
iene = real / 0.035
libra = real / 6.30
print('o valor em reais. {:.2f} vale em dolar. {:.2f} vale em dolar. {:.2f} vale em iene. {:.2f} vale em libra. {:.2f}'.format(real, dolar, euro, iene, libra))
