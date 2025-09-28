#função -> um bloco de código reutilizável
    # outra vantagem: organização

# como funciona:
    #def nome_da_função(parametros):
        # instrução 1
        # instrução 1
        # ...
        # return valor (opcional)

def calcular_imposto(valor): # de o nome da função como o que ela faz
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2

    return imposto


preco_produto1 = 2500
preco_produto2 = 3500
imposto_produto1 = calcular_imposto(preco_produto1)
imposto_produto2 = calcular_imposto(preco_produto2)
print(imposto_produto1)
print(imposto_produto2)

#Quando a função precisa de uma informação externa para funcionar
#utilizamos um parametro
