numbers = {"Viivi": "93848534985",
           "Ahmed": "235987",
           "Pekka": "394873",
           "George": "34987349587"}

valinta = input("Anna kaverin nimi: ")
if(valinta in numbers):
    print(f"Henkilön {valinta} numero on {numbers[valinta]}")
else:
    print("Nimeä ei löytynyt.")