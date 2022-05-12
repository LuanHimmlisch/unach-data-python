from time import sleep
from linked_list import LinkedList
from double_linked_list import DoubleLinkedList
from binary_tree import BinaryTree

option = -1
lista = LinkedList()
lista_doble = DoubleLinkedList()
arbol = BinaryTree(0)


def executeLinked():
    opt = -1
    while (opt != 0):
        print("|========= LISTA ENLAZADA =========|\n\n")
        print("1. Añadir un dato\n2.Remover un dato\n3. Imprimir lista\n")
        opt = int(input('[0 para salir]: '))

        if opt == 1:
            lista.append(input("Dato a añadir: "))
        elif opt == 2:
            lista.remove(input("Dato a eliminar: "))
        elif opt == 3:
            lista.show()
        sleep(0.5)
    pass


def executeDouble():
    opt = -1
    while (opt != 0):
        print("|========= LISTA DOBLEMENTE ENLAZADA =========|\n\n")
        print("1. Añadir un dato al final\n2. Añadir un dato al principio\n3. Remover un dato al final\n4. Remover un dato al principio\n5. Imprimir desde el principio\n6. Imprimir desde el final\n")
        opt = int(input('[0 para salir]: '))

        if opt == 1:
            lista_doble.append(input("Dato a añadir al final: "))
        elif opt == 2:
            lista_doble.prepend(input("Dato a añadir al inicio: "))
        elif opt == 3:
            lista_doble.delete_last()
        elif opt == 4:
            lista_doble.delete_start()
        elif opt == 5:
            lista_doble.loop()
        elif opt == 6:
            lista_doble.loop_end()
        sleep(0.5)
    pass


def executeTree():
    opt = -1
    while (opt != 0):
        print("|========= ÁRBOL BINARIO =========|\n\n")
        print("1. Añadir dato\n2. Buscar dato\n3. Remover dato\n4. Inorden\n5. Preorden\n6. Postorden\n")
        opt = int(input('[0 para salir]: '))

        if opt == 1:
            arbol.agregar(int(input('Dato a agregar: ')))
        elif opt == 2:
            print(arbol.buscar(int(input('Dato a buscar: '))))
        elif opt == 3:
            arbol.eliminar(int(input('Dato a eliminar: ')))
        elif opt == 4:
            arbol.inorden()
        elif opt == 5:
            arbol.preorden()
        elif opt == 6:
            arbol.postorden()
        sleep(0.5)
    pass


while (option != 0):
    print('Elige una estructura de datos para ver un ejemplo:\n\n')
    print('1. Árbol Binario\n2. Lista enlazada\n3. Lista doblemente enlazada\n\n')
    option = int(input('[0 para salir]: '))

    if option is 0:
        break
    elif option is 1:
        executeTree()
    elif option is 2:
        executeLinked()
    elif option is 3:
        executeDouble()
    else:
        print('Selecciona una opción del menú\n\n')

    sleep(0.5)
