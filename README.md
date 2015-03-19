# api_rest
api_rest servers


#Install package:

|pip install -r requirements
|python manage.py syncdb or python manage.py syncdb --migrate
|yes
|create your username and password

_____
#Running project:

|python manage.py runserver 0.0.0.0:8000
_____
#Access the api

|http://localhost:8000/api-auth/login <- Authenticate your user
|http://localhost:8000/api-auth?format=json <-- Get the json infos
|http://localhost:8000/api-auth?format=api <-- Get the api cruds
_____
|http://localhost:8000/servers/?format=json <-- Get list all server in json
|http://localhost:8000/servers/?format=api <-- Get list all server in api

|http://localhost:8000/aplications/?format=json <-- Get list all aplications in json
|http://localhost:8000/aplications/?format=api <-- Get list all aplications in api

* Manipule Servers on the api rest
_____
#For create Server:
|Method: POST
|http://localhost:8000/servers/?format=json&server_name='server_fooo'&is_active=True&ip='192.168.0.1' <-- return 201
_____
#For delete Server:
|Method: POST
|http://localhost:8000/server/1/?format=json <-- Return 204

#For detail specific server and aplications:
|Method: GET
|http://localhost:8000/servers/1 or http://localhost:8000/servers/server_fooo
_____
#For update server
|Methos: POST
|http://localhost:8000/servers/1?format=json&server_name='new_server_foo'&ip='new_ip'&is_active=True

* Manipule aplications on the api rest
_____
#For create Server:
|Method: POST
|http://localhost:8000/servers/?format=json&aplication='aplication_fooo'&server=1 <-- return 201
_____
#For delete Server:
|Method: POST
|http://localhost:8000/aplications/1/?format=json <-- Return 204

#For detail specific aplications:
|Method: GET
|http://localhost:8000/aplications/1 or http://localhost:8000/aplications/aplication_foo
_____
#For update server
|Methos: POST
|http://localhost:8000/aplications/1?format=json&server_name='new_server_foo'&ip='new_ip'&is_active=True
