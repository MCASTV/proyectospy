import requests #Libreria para hacer peticiones 
from bs4 import BeautifulSoup
import csv
def scrap():
    page = 0 #contador de paginas 
    pags = [1,2,3,4,5,7,8,9,10,11,12,15,16,30,34,35,36,39,41]
    rows = []
    x = len(pags)

    while(page < 1 ):
        markup = requests.get(f'https://www.unedl.edu.mx/carreras/carreras.php?univ=unedl&idCarrera={pags[page]}').text
        soup = BeautifulSoup(markup,'html.parser')
        row = {}
        mats = {}
        for t in soup.select('.col-md-4'):
            #print(t)
            titulo = t.select_one('.color-til-carrera').get_text()
            print(titulo)
        for item in soup.select('.row'):
            #print(item)
            for i in item.select('.col-md-6 .col-sm-6'):
                #print(i)
                y = i.select_one('.description').get_text()
                print(y)
        
        page = page + 1
        print(f'Numero de paginas{page}')#Imprime el numero de paginas
        
        with open('./s_unedl.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerows(zip(col-md-4))
            csv_writer.writerows(zip(row))

        
    return rows
rows = scrap()