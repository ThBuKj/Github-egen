

from studentregisterFUNK import lagg_till_student, lista_studenter

def main():
    studenter = []  # Skapar en lista av studenter.

    while True:
        print()
        print("1. Lägg till student")
        print("2. Lista alla studenter")
        print("3. Avsluta\n")

        val = input("Välj ett alternativ 1-3: ")

        if val == "1":
            lagg_till_student(studenter)
        elif val == "2":
            lista_studenter(studenter)
        elif val == "3":
            print("Avslutar programmet. Hej då!\n")
            break
        else:
            print("Gör rätt..\n")

    print(studenter)


if __name__ == "__main__":
    main()
