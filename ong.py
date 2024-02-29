def factorial(numero):
    factorial = 1
    for i in range(numero):
        factorial*=i+1
    print(f"El factorial de {numero} es {factorial}")
    
def productoria(numeros):
    productoria = 1
    for numero in numeros:
        productoria*=int(numero)
    print(f"La productoria de {numeros} es {productoria}")

def calcular(calculos):
    listaProvisoria = calculos.lower().split("=")
    for i in range(len(listaProvisoria)):
        if("fact" in listaProvisoria[i]):
            numFactorial=int(listaProvisoria[i+1].split(",")[0])
            factorial(numFactorial)
        if("prod" in listaProvisoria[i]):
            numeros = listaProvisoria[i+1].split("]")[0].split("[")[1]
            productoria(numeros.split(","))
    
calcular("fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6")