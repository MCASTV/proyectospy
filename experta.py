import requests
import csv
from bs4 import BeautifulSoup


opcion = '0'
while not(opcion=='3'):
    print("Menu")
    print(' 1. Hacer prueba de h1n1')
    print(' 2. Hacer prueba covid')
    print(' 3. Salir')

    opcion=input('  --- ¿Cuál opcion?: ')

          
    if (opcion=='1'):
      print("1-Diagnosticarte")
      print("2-Centro de salud mas cercano")
      opc=input('-Dime la opcion')
      if(opc=='1'):
        print("Dime tus sintomas")
        print("Tienes tos")
        oc=input("1-Si 2-No")
        if(oc=='1'):
         print("Tiene un sintoma\t")
        if(oc=='2'):
         print("Estas normal\n")
        ot=("1-Si o 2-No\t")
        if(ot=='1'):
         print("Tienes un sintoma") 
         

         if(ot=="1"||oc=="1")
         print("ERES POSITIVO")
    elif (opcion=='2')
       print('Por desarrollarse')
       
        
               
    elif (opcion=='3'):
        print('Adios ...')
  
    else:
        print('No existe la opcion')