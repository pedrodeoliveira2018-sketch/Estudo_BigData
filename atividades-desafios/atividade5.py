#Construa um algoritmo, no qual o usuário digitará dois números. No final, 
# exibir o resultado das quatro operações básicas da matemática 
# (soma, subtração, divisão, multiplicação) 
# e o módulo entre o primeiro número, pelo segundo.

nota1 = int(input('digite o seu 1 numero: '))
nota2 = int(input('digite o seu 2 numero: '))
soma = nota1 + nota2 
subtração = nota1 - nota2 
multiplicação = nota1 * nota2 
divisão = nota1 / nota2 
print(f'A soma foi {soma}')
print(f'A subtração foi {subtração}')
print(f'A multiplicação foi {multiplicação}')
print(f'A divisão foi {divisão}')
