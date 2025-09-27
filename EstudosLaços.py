#Laços de repetição
#for item in range(3):
#    print(item)
"""
for item in coleção:
    # comandos
"""

# Range nunca inclui o último número
#for item in range(2,11,2):
#   print(item)

#listas de nomes
'''
nomes = ["João","Amanda","Rafael","Carol"]
for nome in nomes:
    print(nome)

idades = [13,15,18,30,50,75]
#Exibindo apenas os maiores de idade
for idade in idades:
    if idade >= 18:
        print(f'{idade} é maior de idade')
    else:
        print(f'{idade} é menor de idade')
'''
senhas = ["abc", "segura123", "12345", "python123", "oi"]
for senha in senhas:
    if len(senha) >= 6:
        print(f'A senha {senha} é válida')
    else:
        print(f'A senha {senha} deve possuir no mínimo 6 caracteres')
        