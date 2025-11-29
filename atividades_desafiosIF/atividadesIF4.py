# Validação de Qualidade dos Dados: 
# Você está ajudando um analista de dados a validar informações recebidas em um arquivo.
# O analista quer saber, se um valor numérico fornecido pelo usuário é considerado: 
# Inválido 
# Baixo 
# Aceitável 
# Alto 
# A regra é: 
# Valores menores que 0, “Valor inválido.” 
# Valores entre 0 e 50, “Valor considerado BAIXO.” 
# Valores entre 51 e 200, “Valor ACEITÁVEL.” 
# Valores acima de 200, “Valor ALTO e pode indicar um erro no dado.” 
# Crie um programa que receba um número e mostre a mensagem


qualidade = int(input('qual nivel de qualidade de dados ? '))
if  qualidade > 200 :           
    print('Valor ALTO e pode indicar um erro no dado.') 
elif qualidade  >= 51  :
    print('Valor ACEITÁVEL.')
elif qualidade >= 1 :
    print('Valor considerado BAIXO.')
else : 
    print('Valores menores que 0, “Valor inválido.')






