arq = open("teste.txt", "r")

lista = [i.rstrip("\n") for i in arq]

codigo = []
numero = []

for i in lista[:120]:
  data = i.split("->")
  cod = data[0]
  n = data[1].rstrip('%')


  codigo.append(list(cod))
  numero.append(list(n))

# print(codigo)

print(numero)

for i in numero:
  print(i)


