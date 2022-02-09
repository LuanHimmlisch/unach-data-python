# ACTIVIDAD SOBRE EL MANEJO DE ARREGLOS EN PYTHON

Luis Ángel Serrano Catalá

Estructura de Datos, Unidad 1.

LIDTS 2°P, Universidad Autónoma de Chiapas.

## Código

```py

num = -1
lista = []

while num != 0:
    num = int(input("Inserta un número (0 para salir): "))

    if num == 0:
        break

    lista.append(num)
pass

num = int(input("Inserta un número a eliminarse: "))
if num in lista:
    lista.remove(num)
    pass
else:
    print("No se encontró el número")
    pass

suma = sum(lista)
print(f"Suma de números: {suma}")

num = int(input("Inserta un número máximo: "))
minors = filter(lambda x: x < num, lista)

print("Números resultantes")
for key, item in enumerate(minors):
    print(f"[{key}]: {item}")

tuplas = list(dict.fromkeys(lista))
tuplas = map(lambda x: [x, lista.count(x)], tuplas)

print("\nRepeticiones de cada número:\n")
print(list(tuplas))

```

## Repositorio

Puede encontrar el código de todas mis actividades en su [repositorio de Github](https://github.com/LuanHimmlisch/unach-data-python)
