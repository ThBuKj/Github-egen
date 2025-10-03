

def lagg_till_student(studenter):
    namn = input("Vad heter studenten? ")
    try:
        alder = int(input("Hur gammal är studenten? "))
    except ValueError:
        print("Vänligen ange en giltig ålder.")
        return
    student = {
        "namn": namn,
        "alder": alder
    }
    studenter.append(student)
    print(f"Studenten {namn} som är {alder} år har lagts till i listan.\n")


def lista_studenter(studenter):
    if len(studenter) == 0:
        print("Inga studenter i listan.\n")
    else:
        print("Här är listan på studenter:\n")
        for i, student in enumerate(studenter, start=1):            # Skapar en for-loop och går igenom listan [studenter]
            print(f"{i}. {student['namn']} {student['alder']} år.")
        print()

