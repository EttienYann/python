import os

import requests

from dotenv import load_dotenv
import pandas as pd

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv('API_KEY')


#  
# Vérification que la clé API a bien été chargée
if not api_key:
    raise ValueError("La clé API n'a pas été trouvée. Assurez-vous que le fichier .env est correctement configuré.")


# url de la requetes
api_url='https://api.nasa.gov/planetary/apod'

# Paramètres de la requête
params = {
    'api_key': api_key,
    'date': '2024-06-26'  
}
# recupere les donnee 
response = requests.get(api_url,params= params)


#afficher la reponse 
print(response.json())

#afficher le code de la rrequets
#print(response.status_code)


#stocker la requete dans un dataframe
image=response.json()
df=pd.DataFrame([image], columns=['date','explanation','hdurl','media_type','service_version','title','url'])
print(df.head())

#df.to_csv('nasa.c