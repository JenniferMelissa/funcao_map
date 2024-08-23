#funcao map 
# pega funcao pronta, geralmente a funcao lambda, e aplica ela (funcao) diretamente a uma lista, gerando uma outra lista
#gerando uma lista nova do zero, dessa juncao

calcular_pg = lambda x: x * 2

#lista 
numeros = [1,2,3,4,5,6,7,8,9]

#usando funcao map para gera uma lista de prograssao aritmetica
pg = list(map(calcular_pg, numeros))
#funcao list = gera uma lista

#exibir na tela lista
for i in pg:
    print(i)

