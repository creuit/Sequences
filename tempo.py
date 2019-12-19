tmp = 40
print(tmp)

def tempo(tmp, step, stop):
    while tmp < stop:
        tmp += step
        print(tmp)

tempo(tmp, 2, 60)
tempo(60, 3, 72)
tempo(72, 4, 120)
tempo(120, 6, 144)
tempo(144, 8, 208)
