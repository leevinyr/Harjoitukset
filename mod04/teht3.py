sex = input("Anna biologinen sukupuolesi (mies/nainen): ")
hg = float(input("Anna hemoglobiiniarvosi (g/L): "))

if(sex.lower() == "mies" and hg < 134 or sex.lower() == "nainen" and hg < 117):
    print("Hemoglobiiniarvosi on liian alhainen.")
elif(sex.lower() == "mies" and hg > 195 or sex.lower() == "nainen" and hg > 175):
    print("Hemoglobiiniarvosi on liian korkea.")
elif(sex.lower() == "mies" and hg < 195 and hg > 134 or sex.lower() == "nainen" and hg < 175 and hg > 117):
    print("Hemoglobiiniarvosi on normaali.")