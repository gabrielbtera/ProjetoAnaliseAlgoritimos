from time import time

# E = [randint(0,1000000) for i in range(0, 1000000)]
# print(E)
# arq = open('teste.txt', 'w')
# arq.write(f'{E}')

inicio = time()
def mergeSort(lista, inicio, fim):
  
  if (fim - inicio) > 1:
    meio = (fim + inicio) // 2
    mergeSort(lista, inicio, meio)
    mergeSort(lista, meio, fim)
    merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
  left = lista[inicio: meio]
  rigth = lista[meio: fim]
  head_left = 0
  head_rigth = 0

 

  size_l =  meio -  inicio
  size_r = fim - meio

  for k in range(inicio, fim):
    if head_left >= size_l:
      lista[k] = rigth[head_rigth]
      head_rigth += 1

    elif head_rigth >= size_r:
      lista[k] = left[head_left]
      head_left += 1
    elif left[head_left] < rigth[head_rigth]:
      lista[k] = left[head_left]
      head_left += 1
    else:
      lista[k] = rigth[head_rigth]
      head_rigth += 1


      



fim = time()
print('fim', fim)

print(fim-inicio)
