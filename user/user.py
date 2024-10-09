# REST API
from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound


# CALLING GraphQL requests
# todo to complete

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]
   

@app.route("/movies", methods=['GET'])
def get_movies():
     
      query = '''
    query {
        allMovies {
            id
            title
            director
            rating
        }
    }
    '''
      response  = requests.post("http://127.0.0.1:3200/graphql",json={'query':query })
      return response.json()   

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
   
   
