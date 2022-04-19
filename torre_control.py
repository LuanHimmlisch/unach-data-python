import queue
import random

# Luis Ángel Serrano Catalá
# 2°P LIDTS


class TorreDeControl:
    cola = queue.PriorityQueue()

    def __init__(self):
        pass

    # Prioridad
    def nuevo_arribo(self, vuelo=""):
        self.cola.put((1, vuelo))
        pass

    def nueva_partida(self, vuelo=""):
        self.cola.put((2, vuelo))
        pass

    def ver_estado(self):
        print("Vuelos esperando para aterrizar: ")
        print(self._get_of_priority(1))
        print("Vuelos esperando para despegar: ")
        print(self._get_of_priority(2))
        pass

    def asignar_pista(self):
        if len(self.cola.queue) == 0:
            print("No hay vuelos en espera")
            return

        action = ""

        if self.cola.queue[0][0] == 1:
            action = " aterrizó"
        else:
            action = " despegó"

        if random.randint(0, 99) > 1:
            print("El vuelo " + self.cola.queue[0][1] + action + " con éxito.")
        else:
            print("El avión del vuelo " +
                  self.cola.queue[0][1] + " se estrelló")

        self.cola.queue.pop(0)
        pass

    def _get_of_priority(self, num):
        return list(map(lambda x: x[1], filter(lambda x: x[0] == num, list(self.cola.queue))))
