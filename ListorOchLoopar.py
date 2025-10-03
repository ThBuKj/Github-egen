'''
summa = 0
lista_heltal = [1, 2, 3, 4, 5, 3]
storsta_varde = lista_heltal[0]

for heltal in lista_heltal:
    summa += heltal

    if heltal > storsta_varde:
        storsta_varde = heltal

print(summa)
print(storsta_varde)
print() 



tal = int(input("Skriv in ett tal: "))

for i in range(1, 11):
    nytt_tal = (tal * i)
#    print(nytt_tal)
    print(f"{tal} x {i} = {nytt_tal}")
'''



lista = list(range(1, 21))

for tal in lista:
    if tal % 2 == 0:
        print(tal)



lista = list(range(21, -1, -1))

for tal in lista:
    if tal % 2 == 0:
        print(tal)