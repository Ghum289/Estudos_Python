#Os comentário em python são escritos com uma "#"
#Variáveis
velocidade_internet = 400
print(velocidade_internet)
#Números inteiros(int)
idade = 15
#Números decimais(float)
nota = 8.5
#Textos(string)(str)
nome_completo = "José Fábio"
#Booleanos(True or False - precisam ser em maiúsculo)(bool)
pode_entrar = True

#Verificar o tipo de variável
print(type(pode_entrar))

salário_mensal = input("Qual é o seu salário mensal: ")
horas_trabalhadas = input("Quantas horas trabalha por mês: ")
valor_hora = float(salário_mensal)/int(horas_trabalhadas)
print(valor_hora)
