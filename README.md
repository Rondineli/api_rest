# api_rest
api_rest servers


#Install package:
________________
|pip install -r requirements
________________
|python manage.py syncdb or python manage.py syncdb --migrate
________________
|yes
________________
|create your username and password

_____
#Running project:

|python manage.py runserver 0.0.0.0:8000
___________
#Access the api
________________
|http://localhost:8000/api-auth/login <- Authenticate your user
________________

|http://localhost:8000/api-auth?format=json <-- Get the json infos

________________
|http://localhost:8000/api-auth?format=api <-- Get the api cruds

________________
|http://localhost:8000/servers/?format=json <-- Get list all server in json

________________
|http://localhost:8000/servers/?format=api <-- Get list all server in api

________________
|http://localhost:8000/aplications/?format=json <-- Get list all aplications in json

________________
|http://localhost:8000/aplications/?format=api <-- Get list all aplications in api

________________


* Manipule Servers on the api rest
________________

#For create Server:

________________
|Method: POST
________________
|http://localhost:8000/servers/?format=json&server_name='server_fooo'&is_active=True&ip='192.168.0.1' <-- return 201
_____
#For delete Server:
________________
|Method: POST
________________
|http://localhost:8000/server/1/?format=json <-- Return 204
________________
________________
#For detail specific server and aplications:
________________
|Method: GET
________________
|http://localhost:8000/servers/1 or http://localhost:8000/servers/server_fooo
________________
_____
#For update server
________________
|Methos: POST
________________
|http://localhost:8000/servers/1?format=json&server_name='new_server_foo'&ip='new_ip'&is_active=True
________________
________________

* Manipule aplications on the api rest

#For create Server:
________________
|Method: POST
________________
|http://localhost:8000/servers/?format=json&aplication='aplication_fooo'&server=1 <-- return 201
_____
#For delete Server:
________________
|Method: POST
________________
|http://localhost:8000/aplications/1/?format=json <-- Return 204
________________

#For detail specific aplications:
________________
|Method: GET
________________
|http://localhost:8000/aplications/1 or http://localhost:8000/aplications/aplication_foo

________________

#For update aplication
________________

|Methos: POST
________________

|http://localhost:8000/aplications/1?format=json&server_name='new_server_foo'&ip='new_ip'&is_active=True
