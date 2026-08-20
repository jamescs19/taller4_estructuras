import random

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

