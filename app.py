import requests

def teorija():
    #API klici (spletni klici)
    baseUrl = "https://www.google.com/" #če javi napako je to da, nima https ja spredi
    klic = requests.get(baseUrl)

    #print(klic)     #200 do 300 response je kao ok, 400 so napakan na našem clientu, 500 pa server error+
    print(klic.text) #text pridobi raw data klica

    #scrape.

    #API klici: ne vrača html ampak vrača JSON, XML


def api():
    #ce hoces vec klicev itd, das for i in range(value)
    print("\n")
    baseUrl = "https://api.chucknorris.io/jokes/random"
    klic = requests.get(baseUrl) #.json
    print(klic.text)
    #print(klic) = ugotovimo ce so JSON

    #ko smo 100% da so podatk tipa JSON
    js = klic.json()
    print(js.get("value")) #vn dobis vse kar pise pod "value: iz https://api.chucknorris.io/jokes/random "

def nation():
    baseUrl = "https://api.nationalize.io/?name="
    name = "Lovro Habjan"

    call = requests.get(baseUrl + name).json()
    #print(call.url) #preverimo generiran URL. ne dela ce je call .json

    print(call.get("count"))
    print(call.get("name"))
    country = call.get("country")

    for d in country:
        print(d.get("country_id"), d.get("probability")*100)


def jokes():
    baseUrl = "https://official-joke-api.appspot.com/random_joke"


    for d in range(10):
        call = requests.get(baseUrl).json()
        id = call.get("id")
        print("\n", id)
        print(call.get("setup"), call.get("punchline"))

def f1():
    url = f"https://f1api.dev/api/drivers/"
    call = requests.get(url).json()

    drivers = (call.get("drivers"))

    for driver in drivers:
        print(f"{driver.get("name")}, {driver.get("surname")}, {driver.get("nationality")}, {driver.get("birthday")}, {driver.get("number")}, {driver.get("shortName")}, {driver.get("url")}")


#teorija()
#api()
#nation()
#jokes()
f1()