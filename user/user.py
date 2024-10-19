from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
import grpc
import booking_pb2
import booking_pb2_grpc

# Initialisation de l'application Flask
app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'

# Charger les utilisateurs depuis le fichier JSON
with open('{}/data/users.json'.format("."), "r") as jsf:
    users = json.load(jsf)["users"]

# Route pour récupérer les films via GraphQL
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
    response = requests.post("http://127.0.0.1:3200/graphql", json={'query': query})
    return response.json()

@app.route("/bookings", methods=['GET'])
def get_bookings():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        bookings_dict = {}
        response = stub.GetBookings(booking_pb2.Empty())

        for booking in response:
            # Conversion des dates et des films en une liste de dictionnaires
            dates = [{"date": d.date, "movies": list(d.movies)} for d in booking.dates]
            
            # Stocker chaque réservation dans un dictionnaire avec l'ID utilisateur comme clé
            bookings_dict[booking.userid] = {
                "dates": dates
            }
    
    print(bookings_dict)
    return jsonify(bookings_dict)


from werkzeug.exceptions import NotFound

@app.route("/bookings/<userid>", methods=['GET'])
def get_bookings_byuserid(userid):
    print ("user id: ",userid)
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        response = stub.GetBookingsByUserId(booking_pb2.UserId(userid=userid))
        print(response)
        # Vérification si l'utilisateur existe
        if response.userid == "Not Found":
            
            raise NotFound("User ID not found")
        
        # Initialisation du dictionnaire des réservations
        bookings_dict = {}

        # Conversion des dates et des films en une liste de dictionnaires
        dates = [{"date": d.date, "movies": list(d.movies)} for d in response.dates]
        
        # Stocker chaque réservation dans un dictionnaire avec l'ID utilisateur comme clé
        bookings_dict[response.userid] = {
            "dates": dates
        }
    print("for the user id: ",userid)
    print(bookings_dict)
    return jsonify(bookings_dict)







# Lancer l'application Flask
if __name__ == "__main__":
    print("Server running on port %s" % (PORT))
    app.run(host=HOST, port=PORT)
