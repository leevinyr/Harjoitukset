vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))
if(kuukausi >= 1 and kuukausi < 4 or kuukausi == 12):
    print(vuodenajat[0])
elif(kuukausi >= 4 and kuukausi < 7):
    print(vuodenajat[1])
elif(kuukausi >= 7 and kuukausi < 9):
    print(vuodenajat[2])
elif(kuukausi >= 9 and kuukausi < 12):
    print(vuodenajat[3])
