luvut = []

while(True):
    luku = input("Anna luku: ")
    if(luku == ""):
        break
    else:
        luvut.append(int(luku))

luvut.sort(reverse = True)

for i in luvut:
    print(i)