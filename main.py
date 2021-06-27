from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila

linha = "----------------------------"
t = Torre()
t.register(1, "Torre do mal", "Rua do mal, 156")
t.print()

print(linha)

a = Apartamento(1, "Torre do mal", "Rua do mal, 156")
a.register(1,"257",10)
a.print()

print(linha)
a2 = Apartamento(1, "Torre do mal", "Rua do mal, 156")
a2.register(2,"657",8)
a2.print()

print(linha)

#fila
fila = Fila()
fila.push(1, "Torre do mal", "Rua do mal, 156", 1,"257",10)
fila.push(1, "Torre do mal", "Rua do mal, 156", 2,"657",8)
fila.push(1, "Torre do mal", "Rua do mal, 156", 3,"75",4)
fila.push(1, "Torre do mal", "Rua do mal, 156", 4,"142",17)
fila.push(1, "Torre do mal", "Rua do mal, 156", 5,"31",9)

print(fila.peek())

#tira elemento da fila
fila.pop()

print(fila.peek())