# 10 teste consecutive
import random

#inizializzo variabili
j = 0
i = 0
x = 0
avg = 0
# faccio 1000 prove
while x < 1000:
    i = 0
    j = 0
    while j < 10:
        # valuto probabilità del 50%
        val = random.randint(0, 999)
        if val > 500:
            j += 1
            # print("j: ",j)
        else:
            j = 0
        i += 1
    x += 1
    avg += i

print(avg/1000)
