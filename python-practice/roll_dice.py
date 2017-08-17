from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

@app.route('/')
def hello():
	return "Jello World"

@app.route('/roll')
def rollling():
	
	roll = {}
	roll['a'] = random.randint(1,7)
	roll['b'] = random.randint(1,7)

	print(json.dumps(roll))

	# return json.dumps(roll)
	return jsonify(roll)


if __name__ == "__main__":
	app.debug = True
	app.run(host="127.0.0.1", port=8000)