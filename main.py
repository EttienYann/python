import requests


api_url ="https://jsonplaceholder.typicode.com/todos/1"

#response =  requests.get(api_url)
#print(response.json())


#print(response.status_code)


#FORMAT DE LA REPONSE
todo={'userId': 1, 'id': 1, 'title': 'wash car', 'completed': True}
response =  requests.put(api_url,todo)
print(response.json())


print(response.status_code)