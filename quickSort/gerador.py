from random import randrange

file = open("entrada.txt", "w")

file.write("500\n")
for i in range(500):
  tamanho = randrange(1, 500)
  file.write(f"{tamanho}\n")
  lista = [randrange(500) for i in range(tamanho)]
  for i in lista:
    file.write(f"{i} ")
  file.write("\n")
