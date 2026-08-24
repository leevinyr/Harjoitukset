hyttiluokka = input("Anna hyttisi luokka: ")

if(hyttiluokka.lower() == "lux"):
    print("LUX on parvekkeellinen hytti yläkannella.")
elif(hyttiluokka.lower() == "a"):
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif(hyttiluokka.lower() == "b"):
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif(hyttiluokka.lower() == "c"):
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")