mercado = ['leita','quiejo', 'cafe','chá','acuçar','vingre']
#len
print(len(mercado))
item = input('digite item para adicionar:')

#append
mercado.append(item)
print(mercado)

#insert
mercado.insert(1, 'azeite')
print(mercado)

#pop
mercado.pop()
print(mercado)
mercado.pop(0)
print(mercado)

#remover
mercado
print(mercado)
if mercado in mercado:
 mercado.remove('cafe')
print(mercado)


