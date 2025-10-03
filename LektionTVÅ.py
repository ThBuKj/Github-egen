


def lagg_till_student(studenter):                      # Lägger till en ny student i listan
    namn = input("Vad heter studenten? ")
    alder = input("Hur gammal är studenten? ")
    student = {
        "namn": namn,
        "alder": alder
    }
    studenter.append(student)
    print(f"Studenten {namn} som är {alder} år har lagts till i listan.\n")


def lista_studenter(studenter):                         # Skriver ut alla studenter
    if len(studenter) == 0:
        print("Inga studenter i listan.\n")
    else:
        print("\nHär är listan på studenter:\n")
        for i, student in enumerate(studenter, start=1):
            print(f"{i}. {student['namn']} {student['alder']} år.")
        print()  # Radbrytning för tydlighet


def meny():                                             # Visar menyn och hanterar användarens val
    studenter = []                                      # Här lagrar vi studenterna
    
    while True:
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
            print("Fel val, försök igen.\n")


# Starta programmet
meny()
