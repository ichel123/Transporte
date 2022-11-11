#Ichel Delgado Morales - 20202020029

#Se utiliza la librería PuLP para programación Lineal
import pulp


#Listado de filas y columnas
########################################################
#Ejercicio 1
# filas = ["A", "B","C"]
# columnas = [1, 2, 3, 4]

# # diccionario con la capacidad de oferta de cada granja
# oferta = {"A": 15,"B": 25, "C": 10}
# # diccionario con la capacidad de demanda de cada almacen
# demanda = {1:5,2:15,3:15,4:15}
# #diccionario con los costos correspondientes a cada granja y almacen
# costos = {'A': {1 : 10, 2 : 2, 3 : 20, 4 : 11},
#           'B': {1 : 12, 2 : 7, 3 : 9, 4 : 20},
#         'C':   {1 : 4, 2 : 14, 3 : 16, 4 : 18}}

########################################################
#Ejercicio 2
# filas = ["A", "B","C"]
# columnas = [1, 2, 3, 4]

# # diccionario con la capacidad de oferta de cada granja
# oferta = {"A": 3000,"B": 7000, "C": 5000}
# # diccionario con la capacidad de demanda de cada almacen
# demanda = {1:4000,2:3000,3:4000,4:4000}
# #diccionario con los costos correspondientes a cada granja y almacen
# costos = {'A': {1 : 2, 2 : 2, 3 : 2, 4 : 1},
#           'B': {1 : 10, 2 : 8, 3 : 5, 4 : 4},
#         'C':   {1 : 7, 2 : 6, 3 : 6, 4 : 8}}
########################################################
#Ejercicio 3
filas = ["A", "B","C"]
columnas = [1, 2]

# diccionario con la capacidad de oferta de cada granja
oferta = {"A": 1000,"B": 1500, "C": 1200}
# diccionario con la capacidad de demanda de cada almacen
demanda = {1:2300,2:1400}
#diccionario con los costos correspondientes a cada granja y almacen
costos = {'A': {1 : 1000, 2 : 1690},
          'B': {1 : 1250, 2 : 1350},
        'C':   {1 : 1275, 2 : 850}}

########################################################
problema = pulp.LpProblem("Problema de distribución de materiales", pulp.LpMinimize)

#listado de tuplas que contiene todas las posibles rutas de tranporte.
rutas = [(f,c) for f in filas for c in columnas]
#Diccionario que almacenará las cantidades enviadas por cada ruta
variables = pulp.LpVariable.dicts("Rutas de envío",(filas,columnas),0, None, pulp.LpInteger)

#Se define la función objetivo y se agrega al problema
problema += sum(variables[f][c]*costos[f][c] for (f,c) in rutas)

#Restricción de oferta y demanda de cada almacén y granja del problema.
for f in filas:
    problema += sum(variables[f][c] for c in columnas) >= oferta[f]

for c in columnas:
    problema += sum(variables[f][c] for f in filas) <= demanda[c]

#Resolviendo el problema.
problema.solve()
problema.writeLP("problemaDeTransporte.lp")
print("Status:", pulp.LpStatus[problema.status])


for v in problema.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
print("Costo total = ", problema.objective.value())