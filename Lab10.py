import time
import threading

def clock(h, m, s):
    global stop_threads

    while True :
        if stop_threads:
            break

        time.sleep(1)
        if(s == 60):
            s = 0
            m += 1

        if(m == 60):
            m = 0
            h += 1

        if(h == 24):
            h = 0

        # dodawanie 0 przed liczba
        if h < 10:
            zero_h = "0" + str(h)
        else:
            zero_h = str(h)

        if m < 10:
            zero_m = "0" + str(m)
        else:
            zero_m = str(m)

        if s < 10:
            zero_s = "0" + str(s)
        else:
            zero_s = str(s)

        print(str(zero_h + ":" + zero_m + ":" + zero_s))
        s += 1


if __name__ == '__main__':

    print("Funkcje programu:")
    print("c - obecna godzina")
    print("n - nowa godzina")
    print("e - wyjscie z programu\n")
    print("Zmien godzine w formacie HH:MM:SS")
    print("format HH:MM:SS")

    global stop_threads

    hours = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    t = threading.Timer (1 , clock , [ 12 , 00 , 00 ])

    while True :
        input1 = input("")
        user = input1.split(":")
        try:
            if "c" in user[0]:
                hours = int(time.strftime("%H"))
                minutes = int(time.strftime("%M"))
                seconds = int(time.strftime("%S"))

            elif "e" in user[0]:
                stop_threads = True
                time.sleep(1)
                break
            elif "n" in user[0]:
                stop_threads = True
                time.sleep(1)
                input1 = input("Wpisz godzine: ")
                user = input1.split(":")
                hours = int(user[0])
                minutes = int(user[1])
                seconds = int(user[2])
            else:
                hours = int(user[0])
                minutes = int(user[1])
                seconds = int(user[2])

            stop_threads = True
            time.sleep(1)
            stop_threads = False
            t = threading.Timer (1 , clock , [ hours , minutes , seconds+2 ])
            t.start()
        except:
            print("Blad! Zly format!")

    if(t.is_alive()):
        t.join()