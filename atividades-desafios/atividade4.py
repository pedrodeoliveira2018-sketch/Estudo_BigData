#Criar um algoritmo, que pergunte o nome de um estudante e peça também duas notas. 
#  O algoritmo deve calcular média e mostrar uma mensagem
#  informando o nome e a média calculada no final.

nome = input('qual seu nome?  ')
nota1 = float(input('qual sua nota do primeiro semestre ?: '))
nota2 = float(input('qual sua nota do segundo semestre ?: '))
media = nota1 + nota2 / 2
print(f'Olá {nome}')
print(f'A sua nota foi {media}')
