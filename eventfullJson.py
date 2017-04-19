from sys import argv
from bottle import *
import json
import requests

@route('/')
def consulta():
	return template('formulario.tpl')

@post('/resultado')
def resultado():
    city = request.forms.get('city')
    cate = request.forms.get('cate')
    url_base = "http://api.eventful.com/json"
    k=open("key.txt","r")
    key = k.readline()
    k.close()
    payload = {'app_key':key, 'keywords':cate,'location':city,'date':'Future'}
    r = requests.get(url_base + '/events/search', params=payload)
    if r.status_code == 200:
    	doc = json.loads(r.text)
    	return template("resultadojson.tpl",doc=doc,city=city,cate=cate)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(host='0.0.0.0',port=argv[1])
