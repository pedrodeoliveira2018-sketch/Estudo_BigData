# ATIVIDADE 04 
# Crie um algoritmo, que solicite ao usuário o valor de uma 
# compra e exiba um menu com quatro formas de pagamento. 
# Cada opção deve aplicar um desconto (ou juros) diferente: 
# 1 – PIX: Desconto de 12% 
# 2 – Débito: Desconto de 8% 
# 3 – Crédito: Acréscimo de 7% (juros) 
# 4 – Dinheiro: Desconto de 15% 
# Após o usuário escolher a forma de pagamento, o programa deve exibir: 
# O valor original da compra, 
# O valor do desconto ou dos juros aplicado, 
# O valor final a pagar, já com o cálculo realizado. 
# Caso a opção seja inexistente, o programa deve informar “Opção Invalida”. 


pagamento = float(input('qual o valor da sua compra ?'))
print('qual a forma de pagamento \n 1 – PIX: Desconto de 12% \n 2 – Débito: Desconto de 8% \n 3 – Crédito: Acréscimo de 7% (juros) \n 4 – Dinheiro: Desconto de 15% ')
opção = int(input('digite uma das opções a cima '))
