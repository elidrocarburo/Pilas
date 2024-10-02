import matplotlib.pyplot as plt

def graficar_pila(pila):
    plt.figure(figsize=(4, 4))
    plt.bar(range(len(pila)), pila, color='blue')
    plt.xlabel('Posición en la pila')
    plt.ylabel('Valor')
    plt.title('Estado de la pila')
    plt.xticks(range(len(pila)))
    plt.show()

pila = []

pila.append(1)
pila.append(2)
pila.append(3)

print("Pila después de agregar elementos:", pila)
graficar_pila(pila)

elemento = pila.pop()
print("Elemento eliminado:", elemento)
print("Pila después de eliminar un elemento:", pila)
graficar_pila(pila)

pila.append(4)
pila.append(5)
print("Pila después de agregar más elementos:", pila)
graficar_pila(pila)