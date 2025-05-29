def keszit_diagram_sort(nap_szama, homerseklet):
# Függvény létrehozása
    csillagok_szama = int(homerseklet)
#a hőmérsékletet egész számra konvertáljuk
    csillagok = '*' * csillagok_szama
#generálunk egy csillag karakterekből álló sort
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
# a nap számát, a csillagok számát és a hőmérsékletet szöveggé alakítjuk
    return sor
# a sor visszaadása


def rajzolj_diagram(homersekletek):
# a rajzolj_diagram végigmegy a hőmérsékleteken
    print("Napi átlaghőmérséklet diagram (°C)")
# üzenet a diagram elején
    print("-" * 40)
# a diagram tetején egy elválasztó vonal kiírása

    for i in range(len(homersekletek)):
# a napi hőmérséklet listáján végighaladunk
        nap = i + 1  # Napok számozása 1-től indul
# elkezdjük a napokat szémolni
        sor = keszit_diagram_sort(nap, homersekletek[i])
# a diagram sort készít a napról és az adott hőmérsékletről
        print(sor)
#kiírja a sort


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]
# megadjuk a napi átlaghőmérsékleteket

rajzolj_diagram(napi_atlaghomersekletek)
# meghívjuk a függvényt


