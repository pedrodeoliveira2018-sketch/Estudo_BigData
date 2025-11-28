#Elabore um algoritmo que leia um número e 
# escreva na tela, além do próprio número, 
# mostre também o anterior e o sucessor.

numero = int(input('escreva seu numero: ' ))
subi = numero - 1 
soma = numero + 1
print(f'o numero anterior ao seu é: {subi}')
print(f'seu numero é: {numero}')
print(f'o numero sucessor ao seu é: {soma}')