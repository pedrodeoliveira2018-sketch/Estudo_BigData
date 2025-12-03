# Desenvolva um algoritmo, que exiba um menu com quatro opções relacionadas a um sistema de usuários: 
# 1 – Criar um usuário 
# 2 – Editar usuário 
# 3 – Visualizar usuário 
# 4 – Deletar usuário 
# O sistema deve mostrar na tela o número, que o usuário digitou.  

s = input('olá deseja iniciar [S/N]').lower ()
print('1 – Criar um usuário\n 2 – Editar usuário \n 3 – Visualizar usuário \n 4 – Deletar usuário ')
codigo = int(input('escolha uma opção!: '))
match codigo:
            
    case 1:
        print('Criar um usuário')
    case 2:
         print('Editar usuário')
    case 3:
         print('Visualizar usuário')
    case 3:
         print('Deletar usuário')


# if s == ' s ' :            
# else:
#     print('Obrigado tenha um bom dia !')