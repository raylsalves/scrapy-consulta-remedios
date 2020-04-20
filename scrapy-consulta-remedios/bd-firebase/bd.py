from firebase import firebase
import json

path = ''
firebase = firebase.FirebaseApplication('https://[nome-do-projeto].firebaseio.com/', None)


with open(path, 'r', encoding='utf-8') as json_file:
    data = json_file.read()

json_obj = json.loads(data)
result = firebase.post('/[nome-do-projeto]/[nome-tabela]', json_obj)