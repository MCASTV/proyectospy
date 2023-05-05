import requests
from bs4 import BeautifulSoup

markup = requests.get(f'http://www.economia-sniim.gob.mx/Consolidados.asp?dqdia=12&dqmes=12&dqanio=2022&aqdia=10&aqmes=01&aqanio=2023&Prod=&Edo=&punto=140&det=').text
#markup = requests.get(f'https://www.amazon.com.mx/').text
soup = BeautifulSoup(markup,'html.parser')
#print(markup)
print(soup)
print("codigo listo")