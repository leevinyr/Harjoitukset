kt = "python"
ss = "rules"

arvaukset = 0
while(arvaukset < 5):
    kt_arvaus = input("Anna käyttäjätunnus: ")
    ss_arvaus = input("Anna salasana: ")

    if(kt_arvaus != kt or ss_arvaus != ss):
        if(arvaukset >= 4):
            print("Pääsy evätty.")
        else:
            print("Väärin. Yritä uudelleen.")
        arvaukset = arvaukset + 1
        continue
    elif(kt_arvaus == kt and ss_arvaus == ss):
        print("Tervetuloa!")
        break

    print("Pääsy evätty.")