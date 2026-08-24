import math

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (luodit * 13.3) + (naulat * 32 * 13.3) + (leiviskat * 20 * 32 * 13.3)
kilogrammat = math.floor(grammat / 1000)

print("Massa nykyymittojen mukaan:\n" + str(kilogrammat), "kilogrammaa ja", round(grammat - (kilogrammat * 1000), 3), "grammaa")