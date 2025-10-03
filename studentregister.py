import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()


studenter = []                                                          # Skapar en lista av studenter.


while True:
    print() 
    print("1. Lägg till student")
    print("2. Lista alla studenter")
    print("3. Avsluta\n")

    val = input("Välj ett alternativ 1-3. ")

    if val == "1":                                  
        namn = input("Vad heter studenten? ") 
        alder = input("Hur gammal är studenten? ")
        student = {                                                     # Skapar ett dictinary {student}
            "namn": namn,
            "alder": alder, 
        }
        studenter.append(student)                                       # Lägger till dictinary {student} till listan [studenter]
        print(f"Studenten {namn} som är {alder} år har lagts till i listan.\n")
    elif val == "2":
        if len(studenter) == 0:                                         # Om inga studenter finns i listan
            print("Inga studenter i listan.\n") 
        else:
            print("Här är listan på studenter:\n")
            for i, student in enumerate(studenter, start=1):            # Skapar en for-loop och går igenom listan [studenter]
                print(f"{i}. {student["namn"]} {student["alder"]} år.")
    elif val == "3":
        print("Avslutar programmet. Hej då!\n")
        break   
    else:
        print("Gör rätt..\n")

print(studenter)