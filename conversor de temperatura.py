#exe 1
n1 = int(input(' um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e: {},o produto e: {} e a divisao e: {:.3f}'.format(s, m, d), end='')
print('divisao inteira: {} potencia: {}'.format (di, e))

print('_' * 20)

#exe 2
agora = int(input('qual o numero:'))
antes = agora - 1
depois = agora +1
print('esse numero vem antes: {} e esse vem depois: {}'.format(antes, depois))

agora = int(input('digite um numero:'))
print ('esse numero  e o primeiro: {} e o segundo: {}'.format(agora-1, agora+1))

print('_' * 20)

#exe 3
n = int(input('vale um valo:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de {} vale {}.'.format(n, d))
print('o triplo de {} vale{}. A raiz quadrada de a {} e igual a {:.2f}.'.format(n, (n*3),n,(n**(1/2))))

print('_' * 20)

#exe 4
v1 = float(input('primeira nota do aluno:'))
v2 = float(input('segunda nota do aluno:'))
media = (v1 + v2) / 2
print('a media entre {:.1f} e {:.1f} é igual a {:.1}'.format(v1, v2, media))

print('_' * 20)

#exe 5
medida = float(input('uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
print(' a medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

print('_' * 20)

#exe 6
mu = int(input('coloque um valor pra ver a sua tabuada:'))
print('{} x {} = {:2}'.format(mu, 1,mu*1))
print('{} x {} = {:2}'.format(mu, 2,mu*2))
print('{} x {} = {:2}'.format(mu, 3,mu*3))
print('{} X {} = {:2}'.format(mu, 4,mu*4))
print('{} X {} = {:2}'.format(mu, 5,mu*5))
print('{} x {} = {:2}'.format(mu, 6,mu*6))
print('{} x {} = {:2}'.format(mu, 7,mu*7))
print('{} x {} = {:2}'.format(mu, 8,mu*8))
print('{} x {} = {:2}'.format(mu, 9,mu*9))
print('{} x {} = {:2}'.format(mu, 10,mu*10))

print('_' * 20)

#exe 7
real = float(input('digite o quantos reais vc tem? R$'))
dolar = real / 4.81
euro = real / 5.41
iene = real / 0.035
libra = real / 6.30
print('o valor em reais,{:.2f} vale em dolar,{:.2f} vale em dolar,{:.2f} vale em iene,{:.2f} vale em libra,{:.2f}'.format(real, dolar, euro, iene, libra))

print('_' * 20)

#exe 8
largura = float(input('qual e a largura da parede'))
altura = float(input('qual e a altura da parede'))
area = largura * altura
print(' a sua parede tem a dimensao de {}x{} e sua area {}m²'.format(largura, altura, area))
tinta = area / 2
print('para pintar a sua parede, vai  precisa,{} litros de tinta'.format(tinta))

print('_' * 20)

#exe 9
preços = float(input('qual e o preço do produto'))
novo = preços - (preços * 5 /100)
print('o produto que custava R${}, na promoçao com desconto de 5% vai gustar R${}'.format(preços, novo))

print('_' * 20)

#exe10
salario = float(input('qual e salario do fucionari? R$'))
novo = salario + (salario * 20 / 100)
print('um fucionario que ganhava R${:.2f}, com 20% de aumento, passa a receber R${:.2f}'.format(salario, novo))

print('_'*20)

#exe11
c = float(input('informa a temperatura em °c:'))
f = ((9 * c ) / 5 + 32
print(' a temperatura de {} °c corresponde a {}°f!'.format(c, f))

print('_' * 20)

