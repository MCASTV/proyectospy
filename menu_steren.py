import requests
import csv
from bs4 import BeautifulSoup


opcion = '0'
while not(opcion=='3'):
    print("Menu")
    print("----------")
    print(' 1. Hacer scrapeo rapido')
    print(' 2. Guardar en un csv')
    print(' 3. Salir')

    opcion=input('  --- ¿Cuál opcion?: ')

          
    if (opcion=='1'):
        print("-----Menu opcion 1-----")
        print("Escogiste la opcion de correr el scrapeo")
        print()
        url = "https://www.steren.com.mx/propositos"
# Ejecutar GET-Request
        response = requests.get(url)
# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
        html = BeautifulSoup(response.text, 'html.parser')

# Extraer todas las citas y autores del archivo HTML
        quotes_html = html.find_all('div', class_="product-item-info")
#authors_html = html.find_all('div', class_="product details product-item-details")
# Crear una lista de las citas
        quotes = list()
        for quote in quotes_html:
             quotes.append(quote.text)
# Crear una lista de los autores
#authors = list()
#for author in authors_html:
   # authors.append(author.text) 
# Para hacer el test: combinar y mostrar las entradas de ambas listas
        for t in zip(quotes):
            print(t)

        print("------------------")
    elif (opcion=='2'):
        print("Opcion 2")
        print("Archivo creado ")
        with open('./steren.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerows(quotes)
       
        
               
    elif (opcion=='3'):
        print('Adios ...')
  
    else:
        print('No existe la opcion')