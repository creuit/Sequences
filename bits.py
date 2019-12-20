bit = 0
step = 8

def bits(bit, step, stop):
    while bit < stop:
        bit += step
        print(bit)

def main():

    while True:
        stop = input("Say when: ")
        try:
            if int(stop) >= 0:
                stop = int(stop)
                break
        except Exception as e:
            print('try again')

    bits(bit, step, stop)


main()
