# Il problema di Monty Hall

import random

# Inizializzazione variabili
i = 0
changedSuccess = 0

# Effettuiamo 1000 test
for i in range(1000):  #equivalente a while i < 1000:
    vals = [0, 0, 1]                # 0 --> capra | 1 --> auto
    random.shuffle(vals)            # mischio vettore
    index = random.randint(0, 2)    # scelgo porta da aprire
    reveal = random.randint(0, 2)   # porta che apre il conduttore
    while index == reveal or vals[reveal] == 1:
        reveal = random.randint(0, 2)
    if vals[index] == 0:            # se la porta originale conteneva la capra allora cambiando vinco
        changedSuccess += 1
    i += 1

print(changedSuccess)

