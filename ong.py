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
   
def calcular(**kwargs):
    for key, value in kwargs.items():
        if("fact" in key):
            numFactorial=int(value)
            factorial(numFactorial)
        if("prod" in key):
            numeros = value
            productoria(numeros)

    
calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)