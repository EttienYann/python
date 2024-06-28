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
api_url='https://api.nasa.gov/neo/rest/v1/feed'

# Paramètres de la requête
params = {
    'api_key': api_key,
    'start_date': '2024-06-20',  
    'end_date': '2024-06-25'
}
# recupere les donnee 
response = requests.get(api_url,params= params)


#afficher la reponse 
print(response.json())

#afficher le code de la rrequets
#print(response.status_code)


#stocker la requete dans un dataframe
todos=response.json()

#print (todos)

# Extraire les données sur les astéroïdes pour la date spécifique
neo_data = todos['near_earth_objects']['2024-06-25']

asteroid_ids = []
asteroid_names = []
min_diameters_km = []
absolute_magnitudes = []
relative_velocities = []

for neo in neo_data:
    asteroid_ids.append(neo['id'])
    asteroid_names.append(neo['name'])
    min_diameters_km.append(neo['estimated_diameter']['kilometers']['estimated_diameter_min'])
    absolute_magnitudes.append(neo['absolute_magnitude_h'])
    relative_velocities.append(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])

df = pd.DataFrame({
    'ID Astéroïde': asteroid_ids,
    'Nom Astéroïde': asteroid_names,
    'Diamètre Minimal Estimé (km)': min_diameters_km,
    'Magnitude Absolue': absolute_magnitudes,
    'Vitesse Relative (km/s)': relative_velocities
})
print(df)
#df.to_csv('data.csv')