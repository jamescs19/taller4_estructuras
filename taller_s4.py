import random
import sys
import math
sys.setrecursionlimit(5000)

random.seed(11)             
N = 1000

aleatoria = [random.randint(1, 9999) for _ in range(N)]
ordenada  = sorted(aleatoria)        
al_reves  = ordenada[::-1]

print(aleatoria[:5])  




def bubbleSort(lista):
    aux = list(lista)                  
    comparison= 0;
    exchanges= 0

    for i in range(len(aux) - 1):
        has_changed = False;
        for j in range(len(aux)- 1-i):
            comparison += 1
            if aux[j] > aux[j + 1]:
                aux[j], aux[j + 1] = aux[j + 1], aux[j]
                exchanges += 1  
                has_changed = True;
        if not has_changed:
                break;    

    return aux, comparison, exchanges


print("-----Bubble Sort-----")
lista_ord, comp, exchanges = bubbleSort(aleatoria)
assert lista_ord == ordenada, "la lista no quedó bien ordenada"
print(f"Comparaciones: {comp}, Intercambios: {exchanges}\n")


def selectionSort(lista):
    aux = list(lista)
    comparisons = 0
    exchanges  = 0

    for i in range(len(aux) - 1):
        lowIndex = i                     
        for j in range(i + 1, len(aux)):
            comparisons += 1
            if aux[j] < aux[lowIndex]:
                lowIndex = j
        if lowIndex != i:
            aux[i], aux[lowIndex] = aux[lowIndex], aux[i]
            exchanges += 1

    return aux, comparisons, exchanges
print("-----Selection Sort-----")
lista_sel, comp, exchanges = selectionSort(aleatoria) 
assert lista_sel == ordenada, "la lista no quedó bien ordenada"
print(f"Comparaciones: {comp}, Intercambios: {exchanges}\n")

#seleccionSort no puede aprovechar que la lista ya esta ordenada ya que siempre recorre 
#toda la lista para ecnontrar al menor



def insertionSort(lista):
    aux = list(lista)
    comparisons = 0
    moves   = 0

    for i in range(1, len(aux)):
        current = aux[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if aux[j] > current:
                aux[j+1] = aux[j]
                moves += 1
                j-=1
            else:
                break                 
        aux[j + 1] = current
        moves += 1

    return aux, comparisons, moves
print("-----Insertion Sort-----")
lista_ins, comp, moves = insertionSort(aleatoria)
assert lista_ins == ordenada, "la lista no quedó bien ordenada"
print(f"Comparaciones: {comp}, Movimientos: {moves}\n")

algoritmos = [("burbuja", bubbleSort), ("selección", selectionSort), ("inserción", insertionSort)]
escenarios = [("aleatoria", aleatoria), ("ordenada", ordenada), ("al revés", al_reves)]

print(f"{'':12s}{'aleatoria':>12s}{'ordenada':>12s}{'al revés':>12s}")
for nombre, f in algoritmos:
    fila = f"{nombre:12s}"
    for _, datos in escenarios:
        salida, comp, mov = f(datos)
        assert salida == ordenada, "Esta lista no quedo ordenada"
        fila += f"{comp:>12,d}"
    print(fila)
    
    
#Selection Sort comviene mas cuando mover los datos sea mas cosotso que compararlos
#ya que aunque hace muchas comparaciones hace pocos intercambios
# mientras que bubble hace muchos intercambios y insertion hace muchos movimientos

#segunda parte del taller


def fusionar(iz, de):
    resultado = []
    comparaciones = 0
    i = j = 0
    while i < len(iz) and j < len(de):
        comparaciones += 1
        if iz[i]<=de[j]:
            resultado.append(iz[i])
            i += 1         
        else:          
            resultado.append(de[j])
            j += 1         
    resultado +=iz[i:]
    resultado += de[j:]               
    return resultado, comparaciones
print("-----FUSION-----")               
print(fusionar([1, 4, 7], [2, 3, 9]))           


def mezcla(a):
    if len(a) <= 1:
        return list(a), 0
    mitad = len(a) // 2

    izquierda, c1 = mezcla(a[:mitad])
    derecha, c2 = mezcla(a[mitad:])

    juntas, c3 = fusionar(izquierda, derecha)

    return juntas, c1 + c2 + c3

print("-----MEZCLA-----")
lista_mezcla, comp_mezcla = mezcla(aleatoria)
assert lista_mezcla == ordenada, "La lista no quedo ordenada"
print("Comparaciones:", comp_mezcla)

def rapida(a, modo="medio"):
    if len(a) <= 1:
        return list(a), 0

    k = len(a) // 2 if modo == "medio" else len(a) - 1
    pivote = a[k]
    resto = a[:k] + a[k + 1:]

    menores, mayores, comparaciones = [], [], 0

    for v in resto:
        comparaciones += 1

        if v < pivote:
            menores.append(v)
        else:
            mayores.append(v)

    iz, c1 = rapida(menores, modo)
    de, c2 = rapida(mayores, modo)

    return iz + [pivote] + de, comparaciones + c1 + c2


print()
print("-----RAPIDA-----")

for modo in ["medio", "ultimo"]:
    for escenario, datos in [("Aleatoria", aleatoria), ("Ordenada", ordenada)]:
        salida, comparaciones = rapida(datos, modo)
        assert salida == ordenada

        print(f"Rapida ({modo:<6}) - {escenario:<9}: {comparaciones:,} comparaciones")
            
def binary_search(lista, num):
    
    min =0
    max=len(lista)-1
    steps=0
    
    while min<=max:
        steps+=1
        mid = (min+max)//2
        
        if lista[mid] == num:
            return mid, steps
        
        elif num<lista[mid]:
            max =mid-1 
        else:
            min =mid+1   
            
    return -1,steps        
print("-----BUSQUEDA BINARIA-----")        
peor = max(binary_search(ordenada, v)[1] for v in ordenada)
print("peor caso:", peor, "pasos")         
    

def equilibrio(n):
    costo_ordenar = n * math.log2(n)
    k = 1

    while True:
        sin_ordenar = k * n / 2
        con_orden = costo_ordenar + k * math.log2(n)

        if con_orden < sin_ordenar:
            return k

        k += 1
print("----EQUILIBRIO-----")
print(equilibrio(1000000)) # 
print(equilibrio(1000)) #  

# ================================================================
# TABLA FINAL - 5 algoritmos (dia 1 y dia 2), comparaciones
# ================================================================
#                  aleatoria    ordenada    al reves
# burbuja            499.149         999     499.500
# seleccion          499.500     499.500     499.500
# insercion          241.994         999     499.500
# mezcla               8.720      (similar en cualquier escenario no depende del orden)
# rapida (medio)       10.639       8.004
# rapida (ultimo)      11.137     477.636    peor caso: cuando el pivote siempre es el mas grande        
# Busqueda binaria: peor caso 10 pasos con 1.000 elementos, 20 pasos con 1.000.000
# Punto de equilibrio: 40 busquedas con n=1.000.000; 21 busquedas con n=1.000