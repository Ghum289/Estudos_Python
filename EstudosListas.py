#Listas
'''
preços = [20,50,100]
print(preços[2]) #acessando por índice

nomes = ["Brasil", "EUA", "Méximo"]

print(nomes[2]) #acessando por índice
'''

#Encontrat índice automaticamente
'''
print(nomes.index("EUA"))
'''
#Manipular - add novos itens
'''
salarios = [2500, 5000, 7000]
salario_usuario = float(input("Qual o seu salário"))
salarios.append(salario_usuario)
print(salarios)
'''

salarios = [2500, 5000, 7000]
total = 0
for salario in salarios:
    total = total + salario

print (total)