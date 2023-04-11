sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadejte kód součástky: ")
mnozstvi = int(input("Zadejte množství: "))

if kod_soucastky not in sklad:
    print(f"Součástka {kod_soucastky} není skladem.")
else:
    if sklad[kod_soucastky] < mnozstvi:
        print(f"Součástky {kod_soucastky} lze prodat jen omezené množství {sklad[kod_soucastky]}.")
        sklad.pop(kod_soucastky)
    else:
        print(f"Poptávku lze uspokojit v plné výši.")
        sklad[kod_soucastky] -= mnozstvi