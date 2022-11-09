#Ichel Delgado Morales - 20202020029

#Se utiliza la librería PuLP para programación Lineal
import pulp

#Se crea una variable problema que contiene los datos del problema
problema = pulp.LpProblem("Problema de distribución de materiales", pulp.LpMinimize)

#Listado de granjas y almacenes
granja = ["A", "B","C"]
almacen = [1, 2, 3, 4]

# diccionario con la capacidad de oferta de cada granja
oferta = {"A": 15,"B": 25, "C": 10}
# diccionario con la capacidad de demanda de cada almacen
demanda = {1:5,2:15,3:15,4:15}
#diccionario con los costos correspondientes a cada granja y almacen
costos = {'A': {1 : 10, 2 : 2, 3 : 20, 4 : 11},
          'B': {1 : 12, 2 : 7, 3 : 9, 4 : 20},
        'C':   {1 : 4, 2 : 14, 3 : 16, 4 : 18}}

#listado de tuplas que contiene todas las posibles rutas de tranporte.
rutas = [(c,b) for c in granja for b in almacen]
#Diccionario que almacenará las cantidades enviadas por cada ruta
variables = pulp.LpVariable.dicts("Cantidad",(granja,almacen),0)

#Se define la función objetivo y se agrega al problema
problema += pulp.lpSum(variables[c][b]*costos[c][b] for (c,b) in rutas)

#Restricción de oferta y demanda de cada almacén y granja del problema.
for c in granja:
    problema += pulp.lpSum(variables[c][b] for b in almacen) <= oferta[c]

for b in almacen:
    problema += pulp.lpSum(variables[c][b] for c in granja) >= demanda[b]

#Resolviendo el problema.
problema.solve()
print("Status:", pulp.LpStatus[problema.status])

for v in problema.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
print("Costo total = ", problema.objective.value())