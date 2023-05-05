import requests
import csv
from bs4 import BeautifulSoup
print("Bienvenido")
opcion = '0'
while not(opcion=='3'):
    print("MENU")
    print(' 1. EJECUTAR SCRAPEO')
    print(' 2. GENERAR EN CSV') 
    print(' 3. SALIR')
    opcion=input('  ¿QUE DESEAS PAPI?: ')
    if (opcion=='1'):
        print("OPCION 1")
        print("HACIENDO EL SCRAPEO")
        print()
        url = "http://www.economia-sniim.gob.mx/Consolidados.asp?dqdia=12&dqmes=12&dqanio=2022&aqdia=10&aqmes=01&aqanio=2023&Prod=&Edo=&punto=140&det="
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        quotes_html = html.find_all('td', class_="Datos")
        quotes2_html = html.find_all('td',class_="TotRes")
        quotes3_html = html.find_all('td',class_="Datos")
        quotes = list()
        for quote in quotes_html:
             quotes.append(quote.text)
        for t in zip(quotes):
            print(t)
    elif (opcion=='2'):
        print("OPCION2")
        print("GUARDADO EN CSV")
        with open('./org.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerows(quotes)      
    elif (opcion=='3'):
        print('SALIR DEL MENU')
  
    else:
        print('NO HAY OPCION')