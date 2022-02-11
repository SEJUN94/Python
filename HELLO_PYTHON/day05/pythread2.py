import threading


def showNum():
    for i in range(100000):
        print(i, end="")
        if i % 100 == 0:
            print()


def showAscii():
    for i in (range(55203)):
        print(chr(i), end="")
        if i % 100 == 0:
            print()


t1 = threading.Thread(target=showNum)
t2 = threading.Thread(target=showAscii)
t1.start()
t2.start()

# showNum()
# showAscii()

