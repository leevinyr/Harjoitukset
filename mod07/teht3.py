def litroiksi(maara):
    return maara * 3.785

while(True):
    gallonat = float(input("Anna bensiinin määrä gallonoina: "))
    if(gallonat < 0):
        break
    else:
        print(litroiksi(gallonat))
