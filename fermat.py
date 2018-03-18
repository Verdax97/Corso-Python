# Paradosso di Fermat

import random
import matplotlib.pyplot as plt

vett = []
vetStat = []
i = 0
repeat = 0
j = 0
npers = 1
# Faccio il test partendo da una persona fino a 100 persone
while npers < 100:
    repeat = 0
    j = 0
    #per ogni persona faccio 1000 test
    while j < 1000:
        vett = []
        i = 0
        # Assegno a ogni persona un giorno dell'anno
        while i < npers:
            vett.append(random.randint(0, 365))
            i += 1
        # set() ritorna il set di una lista, ovvero la lista originale senza ripetizioni
        if len(vett) != len(set(vett)):
            repeat += 1
        j += 1
    vetStat.append(repeat)
    npers += 1
plt.plot(vetStat)
plt.ylabel('% almeno 2stessa età')
plt.show()
