import os
import requests 
from bs4 import BeautifulSoup 

with open ("busqueda.txt", "r") as file:
    for i in file:
        busqueda= i

Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} 

Carpeta = 'ImagenesDescargada'

def carpetafotos():
    if not os.path.exists(Carpeta):
        os.mkdir(Carpeta)
    descarga_imagenes()

def descarga_imagenes():
    try:
        data = busqueda
        num_images = input('Numero de imagenes: ')
        while(num_images == str() or num_images.isspace() or num_images.isalpha() or int(num_images)<3):
            print("Valor no válido, ingrese número entero mayor a 3")
            num_images = input('Numero de imagenes: ')
            
        print('Buscando...')
        
        busqueda_url = Google_Image + 'q=' + data 
        
        response = requests.get(busqueda_url, headers=u_agnt)
        html = response.text 
        
        
        b_soup = BeautifulSoup(html, 'html.parser') 
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
        
        count = 0
        imagelinks= []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= int(num_images)):
                    break
                
            except KeyError:
                continue
        
        print(f'{len(imagelinks)} imagenes encontradas')
        print('Descargando...')

        for i, imagelink in enumerate(imagelinks):
            response = requests.get(imagelink)
            
            imagename = Carpeta + '/' + data + str(i+1) + '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)

        print('Descarga Completa')
    except ValueError:
        descarga_imagenes()