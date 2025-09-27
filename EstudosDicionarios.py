#Dicionários cria uma lista de valores com um rótulo
#Tem sempre uma chave - e um valor
emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plalza@gmail.com",
    "Barra": "barra@gmail.com"
# Chave: valor (syntaxe)
}

#buscar
email = emails_gerentes['Iguatemi']
print (email)

#adicionar ou modificar(caso já exista chave com o mesmo nome)
emails_gerentes["Leblon"] = "leblon@gmail.com"
print(emails_gerentes)

#uma das formas de mostrar todas as chaves com o .keys
print(emails_gerentes.keys())

#mostrando todos os valores com for
for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print (email)

#com .value
print(emails_gerentes.values())

#retirar um item dos dicionários
emails_gerentes.pop("Leblon")
print(emails_gerentes)

#Verificar se existe no dicionário
if "Barra" in emails_gerentes:
    print("Existe")
else:
    print("Não Existe")

#Da para fazer isso com os valres assim
if "leblon@gmail.com" in emails_gerentes.values():
    print("Existe")
else:
    print("Não Existe")