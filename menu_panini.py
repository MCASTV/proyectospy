import requests
import csv
from bs4 import BeautifulSoup

print("Bienvenido @usuario")
print("Vamos a scrapear el siguiente pagina")
print("https://tiendapanini.com.mx/figuras")
print("----------")
opcion = '0'
while not(opcion=='4'):
    print("Menu")
    print("----------")
    print(' 1. Correr scrapeo')
    print(' 2. Guardar en un csv')
    print(' 3. Guardar en una base de datos')
    print(' 4. Salir')

    opcion=input('  --- ¿Cuál opcion?: ')

          
    if (opcion=='1'):
        print("-----Menu opcion 1-----")
        print("Escogiste la opcion de correr el scrapeo")
        print()
        url = "https://tiendapanini.com.mx/figuras"

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
            url = "https://tiendapanini.com.mx/figuras?p=2"
     
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
        print("-----Menu opcion 2-----")
        print("Escogiste la opcion de guardarlo en un csv")
        print("Archivo creado ")
        print("Revisa tu explorador de archivos")
        with open('./panifina4l.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerows(quotes)
        print("------------------")
        
    elif (opcion=='3'):
        print(' **** menu opcion 03 ****')
        print("Por desarrollarse")            
    elif (opcion=='4'):
        print(' **** Saliendo del menu  ****')
  
    else:
        print('No existe la opcion')