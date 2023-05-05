# Importar módulos
import requests
import csv
from bs4 import BeautifulSoup
# Dirección de la página web 
url = "http://www.economia-sniim.gob.mx/Consolidados.asp?dqdia=12&dqmes=12&dqanio=2022&aqdia=10&aqmes=01&aqanio=2023&Prod=&Edo=&punto=140&det="

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
quotes_html = html.find_all('td', class_="Datos")
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)

for t in zip(quotes):
	print(t)
# Guardar las citas y los autores en un archivo CSV en el directorio actual
# Abrir el archivo con Excel / LibreOffice, etc.
with open('./orga.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerows(quotes)