from googlesearch import search
import re
import requests
from bs4 import BeautifulSoup as bs

linkwik = re.compile(r'https://e(n)?(s)?.wikipedia.org/')
linkyou = re.compile(r'https://www.youtube.com/')
linkfb = re.compile(r'https://www.facebook.com/')
linktw = re.compile(r'https://twitter.com/')
linkig = re.compile(r'https://www.instagram.com/')
linkvalid=re.compile(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})')
links=[]

def clear():      #limpiar output
	import os
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def busquedalinks():
	clear()

	busqueda = input("Nombre del Artista/Banda: ")

	while(busqueda == str() or busqueda.isspace()):
		print("Error, Busqueda invalida")
		busqueda = input("Nombre del Artista/Banda: ")
	clear()
	print("Cargando...")

	try:
		for i in search(busqueda, tld='com', lang='en', num=15, start=0, stop=15, pause=2.0):
			if not linkwik.search(i):
				if not linkyou.search(i):
					if not linkfb.search(i):
						if not linktw.search(i):
							if not linkig.search(i):
								links.append(i)
	except TimeoutError:
		busquedalinks()

	
	introlink()

	file=open("links.txt","w")
	for renglon in range(0,len(links)):
		file.write(links[renglon]+" ")
	file.close()
		

	file=open("busqueda.txt","w")
	file.write(busqueda)
	file.close()
	print("URL's Descargados")

	with open ("links.txt", "r") as file:
		for i in file: 	
			mo=linkvalid.findall(i)

	for e in range(0, len(mo)):	
			page = requests.get(mo[e])
			print("Url de trabajo "+str(e+1)+":", mo[e])
			print ("Estado de conexión", page.status_code)
			soup = bs(page.content,"html.parser")
			souppretty = soup.prettify()
			#print(souppretty)
			fo = open("ejemplo_"+str((e+1))+".txt", "w", encoding = 'UTF-8')
			fo. write(souppretty)
			fo.close()

def introlink():
	
	resp=input("¿Desea agregar un url? s/n: ")
	while (resp =="s" or resp == "S"):
		linkuser = input("Introducir url: ")
		uservalid = linkvalid.search(linkuser)
		if (uservalid == None):
			print("Error: url no es valido")
		else:
			links.append(linkuser)
		resp=input("Desea agregar un url? s/n ")