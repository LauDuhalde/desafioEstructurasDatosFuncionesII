##Filtro Relevante

def filtro(precios,umbral,menorMayor):
    productos = []
    if(menorMayor=="menor"):
        productos = [producto for producto, valor in precios.items() if valor<umbral]
        print(f"Los productos menores al umbral son: ",", ".join(productos))
    elif (menorMayor=="mayor"):
        productos = [producto for producto, valor in precios.items() if valor>umbral]
        print(f"Los productos mayores al umbral son: ",", ".join(productos))
    else:
        print("Lo sentimos, no es una operación válida")
    
import sys
precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}
if(len(sys.argv)==3):
    filtro(precios,int(sys.argv[1]),sys.argv[2].lower())
elif (len(sys.argv)==2):
    filtro(precios,int(sys.argv[1]),"mayor")
else:
    print("Debe ingresar al menos el umbral de corte, si lo desaea también puede indicar si este umbral es 'menor' o 'mayor' (sin comillas)")