import json
import requests
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# @app.route('/api/pokemon')
# def index():
# 	data = {}
# 	name = ["bulbasaur", "charmander", "squirtle"]
# 	data["pokemon"] = name
# 	json_data = json.dumps(data)
# 	return json_data

# @app.route('/api/pokemon/pokedex/<name>')
# def pokedex(name):
#     return render_template("pokedex.html",name=name)
@app.route('/api/pokemon/<id>')
def index(id):
	data = {}
	if int(id) > 807 or int(id) < 1:
		data['pokemon'] = "Missing"
		json1 = json.dumps(data)
		return json1
	rout = "https://pokeapi.co/api/v2/pokemon/"+ id
	response = requests.get(url = rout)
	response = response.json()
	data['id'] = response['id']
	data['name'] = response['name']
	data['sprite'] = response['sprites']['front_default']
	pokemon = {}
	pokemon['pokemon'] = data
	json1 = json.dumps(pokemon)

	return json1
    

if __name__ == '__main__':
    app.run(host='localhost' ,port=8006)