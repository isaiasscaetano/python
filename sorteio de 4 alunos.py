'''import random
b1 = str(input(' primeiro aluno:'))
b2 = str(input('segundo aluno:'))
b3 = str(input('terceiro aluno:'))
b4 = str(input('quarto aluno:'))
lista = [b1, b2, b3, b4]
escolhido = random.choice(lista)
print(' o aluno escolhido foi. {} '.format(escolhido'''


from random  import choice
b1 = str(input(' primeiro aluno:'))
b2 = str(input('segundo aluno:'))
b3 = str(input('terceiro aluno:'))
b4 = str(input('quarto aluno:'))
lista = [b1, b2, b3, b4]
escolhido = choice(lista)
print(' o aluno escolhido foi. {} '.format(escolhido))
