# 10 teste consecutive
import random

#inizializzo variabili
count = 0
# faccio 100000 volte 10 lanci: un milione di lanci
for x in range(100000):
    i = 0
    j = 0
    val = []
    while j < 10:
        # valuto probabilità del 50%
        val.append(random.randint(0, 1))
        j += 1

    if val == [1 for i in range(10)]:
        count += 1
    x += 1


print(count)
