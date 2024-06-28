#importation des biblitheque
import os

import requests
import pandas as pd

from dotenv import load_dotenv
#enregistrement de l'image
from PIL import Image
from io import BytesIO
#deuxieme methode
from skimage import io

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv('API_KEY')

def call_img_nasa(api_key, date):
    try:
        # url de la requetes
        api_url= "https://api.nasa.gov/planetary/apod"

        #parametres de la requette
        params = {
        'api_key':api_key ,
        'date': date  
        }
        # recuperer l'url de l'image  avec la requette
        image_url = requests.get(api_url, params=params).json()['hdurl']
        #telecharger l'image
        image_response = requests.get(image_url)

        #afficher l'image
        image = Image.open(BytesIO(image_response.content))

        #nommer l'immage
        image_path = f"nasa_apod_image_{date}.jpg"
        #sauvegarder l'image
        image.save(image_path)

        return print('image enregistrer avec succes')
    except:
        print('l\'image n\'as pas ete enregistrer')
#def afficher_image(api_url,date):


#.json()['hdurl']

call_img_nasa(api_key,"2024-06-24")

'''
print("***********")
print(reponse)
print("***********")


image=io.imread(nasa['hdurl'])
io.imshow(image)
io.show()

image_url = nasa['hdurl']

# Télécharger l'image
image_response = requests.get(image_url)
#print(image_response)
#print (image_response.status_code )
#afficher l'image 
image = Image.open(BytesIO(image_response.content))
#print(image)
#enregistrer l'image
image_path = "nasa_apod_image.jpg"
image.save(image_path)
'''