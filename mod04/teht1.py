kuhan_pituus = float(input("Anna pyydystämäsi kuhan pituus senttimetreinä: "))

if(kuhan_pituus < 37):
    print("Kuha on alimittainen. Laske se takaisin järveen. Tarvitset kuhan, joka on", round(37 - kuhan_pituus, 2), "senttimetriä pidempi.")
else:
    print("Onneksi olkoon, sait hyvän kokoisen kuhan.")