# Programa de ejemplo para la demostracion del uso del metodo de las Pilas
# y para la demostracion de la conversion de la notacion Infija a Prefija
# Desarrollado por el Dr. Carlos A. García Ramos, para la Materia de Estructura de Datos
# De la Carrera de Ingenieria de Desarrollo y Tecnologias de Software
# Por la Universidad Nacional Autonoma de Chiapas, Facultad de Contaduria y Administracion, Campus 1.
# Tuxtla Gutierrez, Chiapas a 22 de Marzo del 2022.

class Stack(object):
    # Operaciones Basicas
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()

    def esta_vacia(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def ver_pila(self):
        print(self.items)
    # Operaciones Secundarias

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def ValorA(i):
    for j in range(len(Expresion1)):
        if Expresion1[j][0] == i:
            return Expresion1[j][1]


def ValorB(i):
    for j in range(len(Expresion2)):
        if Expresion2[j][0] == Pila.top():
            return Expresion2[j][1]


def vaciar():
    for k in range(Pila.size()):
        temp = Pila.desapilar()
        if temp != '(' and temp != ')':
            Prefija.append(temp)


Pila = Stack()
vA = 0
vB = 0
Prefija = ([])
Expresion1 = (['+', 1], ['-', 1], ['*', 2], ['/', 2], ['**', 4], ['(', 5])
Expresion2 = (['(', 0], ['+', 1], ['-', 1], ['/', 2],
              ['*', 2], ['**', 3], [')', 6])

Infija = ([])
Infija.extend("3*4/(3+1)")

for i in reversed(Infija):
    if i == '+' or i == '-' or i == '*' or i == '/' or i == '(' or i == ')':
        if i != ')':
            if Pila.esta_vacia():
                Pila.apilar(i)
            else:
                vA = ValorA(i)
                vB = ValorB(Pila.top())
                if vA >= vB:
                    Pila.apilar(i)
                elif vA < vB:
                    Prefija.append(Pila.desapilar())
                    Pila.apilar(i)
    else:
        Prefija.append(i)
if not Pila.esta_vacia():
    vaciar()
print(list(reversed(Prefija)))
