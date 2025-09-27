# While

''' syntaxe
while consição:
    #código a ser executado
'''

# Criar um programa que permite 3 tentativas, antes de fechar
'''
tentativas = 0
while tentativas < 3:
    print("tente novamente")
    tentativas = tentativas + 1
'''
# Quando queremos que uma ação continue acontecendo, até que
# um critério seja satisfeito
# só pode logar, se digitar a senha correta
'''
senha = ''
while senha != '123456':
    senha = input("Digite a senha correta: ")

print("Bem-vindo ao sistema")
'''
#Garantir que algo esteja preenchido
#Só deve continuar, quando o usuário informar seu nome
'''
nome = ""
while nome == "":
    nome = input("Digite seu nome: ")

print(f"Bem vindo {nome}")
'''
#Contadores dentro de while
#Ser avisado as 17hrs do por do sol
'''
horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1

print("Hora de ver o por do sol")
'''

usuario = ""
senha = ""
tentativas = 0

while (usuario != "Jose" and senha != "senha123") and tentativas < 3:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    #tentativa += 1 == tentativa = tentativa + 1
    tentativas += 1 

if usuario != "Jose" and senha != "senha123":
    print ("Aguarde 30 minutos antes de tentar novamente")
else:
    print("Login feito com sucesso!")