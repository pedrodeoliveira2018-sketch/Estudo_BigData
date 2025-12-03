# Escreva um algoritmo em Python, que receba um valor monetário de venda fornecido pelo usuário
# e classifique esta venda de acordo com as seguintes regras: 
# Venda pequena: Valores inferiores a 100. 
# Venda média: Valores entre 100 (inclusive) e 500 (exclusive). 
# Venda grande: Valores iguais ou superiores a 500

venda = int(input('qual o valor da sua compra ?: '))

match venda :
     case v if v < 100 :
         print('pequena compra ')
         print('voce ganhou 10 pontos ')
     case v if v < 500 :
         print ('compra media ')  
         print ('voce ganhou 25 pontos ') 
     case v if v >= 500 :
         print ('grande compra ') 
         print('voce ganhou 50 pontos ')
     case _ :
        print('invalido')   