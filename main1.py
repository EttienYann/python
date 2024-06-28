import requests
import pandas as pd

api_url="https://jsonplaceholder.typicode.com/todos/"

response =requests.get(api_url)
#transformer la reponse en dictionnaire python
todos= response.json()
df= pd.DataFrame(todos, columns= ['userId','id','title','completed'])

print(df.head())

df.to_csv('todos.csv',index=False)
