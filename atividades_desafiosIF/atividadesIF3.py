# Acesso ao benefício especial da cooperativa 
# Crie um programa, que receba do usuário: 
# O tempo de filiação à cooperativa (em anos), 
# O valor movimentado nos últimos 6 meses. 
# O sistema deve verificar, se a pessoa tem direito a um benefício especial
# considerando que basta uma das condições ser verdadeira: 
# Ter mais de 3 anos de filiação 
# Ou ter movimentado mais de R$ 5.000,00. 
# Caso nenhuma condição seja atendida, o sistema deve informar, que o cooperado ainda
# não cumpre os requisitos. 


usuário = input('qual seu nome ? ')
tempo = float(input('qual tempo Sr(a) tem de filiação ? '))
valor = float(input('qual foi o valor movimentado nos ultimos 6 meses'))

if tempo >= 3 or valor >= 5.000 : 
    print(f'Sr {usuário} tem direito a benefício especial!')

else :
    print(f'Sr {usuário} ainda nao tem benefício especias')



