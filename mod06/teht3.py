luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if(luku <= 1):
    print("Luku ei ole alkuluku.")
else:
    for i in range(2, luku):
        if(luku % i == 0):
            on_alkuluku = False
            break

if(on_alkuluku):
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")