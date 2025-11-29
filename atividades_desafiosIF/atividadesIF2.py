# Verificação automática de liberação de um pedido 
# Desenvolva um programa, que receba três informações: 
# Quantidade disponível em estoque, 
# Quantidade solicitada pelo cliente, 
# Peso total do pedido. 
# O sistema deve liberar o pedido apenas se: 
# Tiver estoque suficiente 
# O peso total não ultrapassar 50 kg. 
# Se qualquer uma desas condições não for atendida, o
# programa deve informar, que o pedido não pode ser enviado. 



quantidade = float(input('qual quantidade tem em estoque ? '))
pedido = float(input('qual pedido do cliente ? '))
peso= float(input('qual peso total do pedido ? '))

if pedido <= 200 and peso <= 50 :
    print('seu pedido esta sendo separado')
else :
    print('exedeu estoque da loja ')