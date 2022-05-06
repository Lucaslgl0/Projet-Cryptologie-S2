from operations_liste import addition, multiplication, soustraction, division
import time
import random
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("seaborn")

x = [1, 2, 3, 4, 5]
y = []

taille = 200
liste1 = [random.randint(0, 9) for i in range(400)]
liste2 = [random.randint(0, 9) for i in range(taille)]
t1 = time.time()
addition(liste1, liste2)
t2 = time.time()
y.append(t2 - t1)
print("L'addition de deux liste de ", taille, "éléments prend", t2 - t1, "secondes.")

t1 = time.time()
multiplication(liste1, liste2)
t2 = time.time()
y.append(t2 - t1)
print(
    "La multiplication de deux liste de ",
    taille,
    "éléments prend",
    t2 - t1,
    "secondes.",
)

t1 = time.time()
soustraction(liste1, liste2)
t2 = time.time()
y.append(t2 - t1)
print(
    "La soustraction de deux liste de ", taille, "éléments prend", t2 - t1, "secondes."
)

t1 = time.time()
division(liste1, liste2)
t2 = time.time()
y.append(t2 - t1)
print("La division de deux liste de ", taille, "éléments prend", t2 - t1, "secondes.")

t1 = time.time()
t2 = time.time()
y.append(t2 - t1)
print(
    "L'exponentiation d'une liste de ", taille, "éléments prend", t2 - t1, "secondes."
)


ax = plt.subplot()
ax.bar(
    x,
    y,
    tick_label=["Addition", "Multiplication", "Soustraction", "Division", "Exposant"],
    label="Temps de calcul",
)
ax.set_title("Temps de calcul des différentes opérations")
ax.set_xlabel("Méthodes")
ax.set_ylabel("Temps (en s)")
plt.legend()
plt.show()
