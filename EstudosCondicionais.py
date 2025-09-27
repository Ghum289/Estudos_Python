#Condicionais - if elif else
trabalho_terminado = False
if trabalho_terminado == True:
    print("Bora!")
else:
    print("Não posso sair")

#Como lidar com mais de uma situação?
"""
atrasos = int(input("quantas faltas você tem? "))
if atrasos >= 3:
    print("Você está suspenso!")
elif atrasos == 2:
    print("Mais uma falta está suspenso!")
elif atrasos == 1:
    print("Mais duas faltas está suspenso!")
else:
    print("pode entrar")
"""

valor1 = int(input("Digite um valor inteiro: "))
valor2 = int(input("Digite mais um valor inteiro: "))

if valor1 > valor2:
    print("O primeiro Valor é o maior valor")
elif valor1 < valor2:
    print("O segundo valor é o maior")
else:
    print("Os valore são iguais")