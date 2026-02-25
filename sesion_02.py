# Tuplas
mi_tupla = (2, 4)
print("Mi tupla: ",mi_tupla)

# Lista
mi_lista = [1, 3.1416, "chris", mi_tupla]
print("el primer elemento de mi lista: ",mi_lista[0])
print("el cuarto elemento de mi lista: ",mi_lista[3])
print("el tercer elemento de mi lista: ",mi_lista[2])

# Diccionarios
mi_diccionario = {
    "mi_lista" : mi_lista,
    "nombre": "chris",
    "pi": 3.1416,
    "Tel":"663-429-1700"
    }
print("llave para acceder a mi diccionario mi_lista",mi_diccionario["mi_lista"])
print("llava para acceder a mi diccionario pi",mi_diccionario["pi"])
print("llave para acceder a mi diccionario tel",mi_diccionario["Tel"])