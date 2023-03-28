import random
from getpass import getpass

wybor = ["Kamień", "Papier", "Nożyce"]
wyniki = []
ilosc = int(input("Podaj ilosc rund:\n"))
tryb_gry = int(input("Podaj tryb gry: (1- gracz vs komputer, 2- gracz vs gracz)\n"))
imiona = []
w1 = 0
w2 = 0
for i in range(0, tryb_gry):
    imiona.append(input("Podaj imie gracza " + str(i + 1) + ":\n"))
if (tryb_gry == 1):
    imiona.append("Komputer")
for i in range(0, ilosc):
    wybor1 = int(getpass(prompt=("Gracz " + imiona[0] + " wybiera: (1- kamień, 2- papier, 3- nożyce\n")))
    if (tryb_gry == 2):
        wybor2 = int(getpass(prompt=("Gracz " + imiona[1] + " wybiera: (1- kamień, 2- papier, 3- nożyce\n")))
    else:
        wybor2 = random.randrange(1, 4)
        print("Komputer wybiera ")
    if wybor1 == wybor2:
        tmp = "Remis!"
    else:
        if wybor1 == 1:
            if wybor2 == 3:
                tmp = ("Wygral " + imiona[0])
                w1 += 1
            else:
                tmp = ("Wygral " + imiona[1])
                w2 += 1
        else:
            if wybor1 == 2:
                if wybor2 == 1:
                    tmp = ("Wygral " + imiona[0])
                    w1 += 1
                else:
                    tmp = ("Wygral " + imiona[1])
                    w2 += 1
            else:
                if wybor2 == 2:
                    tmp = ("Wygral " + imiona[0])
                    w1 += 1
                else:
                    tmp = ("Wygral " + imiona[1])
                    w2 += 1

    wyniki.append(wybor[wybor1 - 1] + " vs " + wybor[wybor2 - 1] + " " + tmp)
    print(tmp)
    print(str(w1) + " vs " + str(w2))
print("====Historia====")
for s in wyniki:
    print(s)
print("=======Wyniki=======")


print(imiona[0] + ": " + str(w1))
print(imiona[1] + ": " + str(w2))
if(w1>w2):
    print("Wyrgał " + imiona[0])
else:
    if(w2>w1):
        print("Wygrał " + imiona[1])
    else:
        print("Remis!")