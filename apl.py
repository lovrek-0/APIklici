import requests

def uvod():

    url = "https://restcountries.com/v3.1/all?fields=name"
    odgovor = requests.get(url)
    drzave = odgovor.json()
    dr = []


    for d in drzave[:5]:
        dr.append(d.get("name").get("official"))


    for d in dr:
        c = requests.get(f"https://restcountries.com/v3.1/all?fields=name/{d}").json()
        print(c[0].get("capital"))


def vaja1():
    # 1: Poišči državo z največ sosedi (borders)
    # Namig: Nekatere države so otoki in nimajo ključa "borders"!
    max_bordersbf = 0
    max_bordersaf = 0
    list =  [max_bordersbf, None]


    url = "https://restcountries.com/v3.1/all?fields=name"
    odgovor = requests.get(url)
    drzave = odgovor.json()
    dr = []

    for d in drzave[:5]:
        dr.append(d.get("name").get("official"))
    
    for d in dr:
        c = requests.get(f"https://restcountries.com/v3.1/name/{d}").json()
        if c[0].get("borders") != None:
            max_bordersaf = len(c[0].get("borders"))
            if max_bordersbf < max_bordersaf:
                max_bordersbf = max_bordersaf
                list.pop(1)
                list.append(c[0].get("common"))

        print(list)
            


        

    


    
vaja1()



# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!

# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"

# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0

# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone

# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države

# 6: Izpiši število držav, ki imajo za uradni jezik angleščino

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()

# 9: Katera država ima najdaljše ime?

# 10: Izračunaj še eno statistiko po želji.
