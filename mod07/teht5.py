lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parittomat = []

def poista_parittomat(lista):
    for i in lista:
        if(i % 2 == 0):
            parittomat.append(i)
        else:
            continue
    return parittomat

print(poista_parittomat(lista1))
