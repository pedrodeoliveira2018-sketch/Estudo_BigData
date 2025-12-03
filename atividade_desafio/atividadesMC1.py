# ATIVIDADE 01 
# Crie um algoritmo, que solicite ao usuário a digitação de um número (inteiro ou decimal).
# O algoritmo então, deve exibir uma mensagem indicando, se o número é:  
# Positivo, 
# Negativo, 
# Ou zero


número = int(input('digite o número !: '))

match número:
    case  1 | 4 | 7 :
        print('Positivo')
    case 2 | 5 | 8:
       print ('6 zero')   
    case 3 | 6 | 9:
        print ('Negativo') 