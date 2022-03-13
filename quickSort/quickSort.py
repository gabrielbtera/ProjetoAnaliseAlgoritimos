

def quickSort(lista, inicio, fim):
  if inicio < fim:
    particao = quebrar(lista, inicio, fim)

    quickSort(lista, inicio, particao -1)
    quickSort(lista, particao + 1, fim)

def quebrar(lista, inicio, fim):
  pivot = lista[fim]
  ponto_1 = inicio

  for ponto_2 in range(inicio, fim):
    if lista[ponto_2] >= pivot:
      lista[ponto_1], lista[ponto_2] = lista[ponto_2], lista[ponto_1]
      ponto_1 += 1
  
  lista[ponto_1], lista[fim] = pivot, lista[ponto_1]

  return ponto_1


lista = [3,1, 4,5,0,5]

quickSort(lista, 0, len(lista)-1)

print(lista)