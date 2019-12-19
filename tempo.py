def tmp(step, stop):
    while tempo < stop:
        tempo += step
        print(tempo)

tempo = 40
print(tempo)

tmp(2, 60)
tmp(3, 72)
tmp(4, 120)
tmp(6, 144)
tmp(8, 208)


