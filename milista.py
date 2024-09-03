# Ejemplo de uso de listas
misnovias = ["Athena","Kamala","Mary"]
misNumeros = [666,77,10]
# Mostrando mis novias
print(misnovias)
# Mostrando mis numeros raros
print(misNumeros)
print("---Accediendo a los elementos de la lista---")
print(misnovias[-2])
if "Klay" in misnovias:
    print("Si, 'Kamala' esta en la lista de mis novias")
else:
    print("Chale, no eres mi novia")
print("Numeros de novias")
Nnovias = len(misnovias)
print(f"Numero de novias = {Nnovias}")
print("Ciclo for en listas")
posicion = 0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion = posicion + 1