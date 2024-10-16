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

# Route pour récupérer toutes les réservations via gRPC
@app.route("/bookings", methods=['GET'])
def get_bookings():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        bookings = []
        for booking in stub.GetBookings(booking_pb2.Empty()):
            bookings.append({
                "userid": booking.userid,
                "dates": booking.dates
            })
    return jsonify(bookings)

# Route pour récupérer les réservations par ID utilisateur via gRPC
@app.route("/bookings/<user_id>", methods=['GET'])
def get_bookings_by_user_id(user_id):
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        response = stub.GetBookingsByUserId(booking_pb2.UserId(userid=user_id))
        if response.userid == "Not Found":
            return make_response(jsonify({"error": "Bookings not found for user ID: {}".format(user_id)}), 404)
        return jsonify({"userid": response.userid, "dates": response.dates})

# Lancer l'application Flask
if __name__ == "__main__":
    print("Server running on port %s" % (PORT))
    app.run(host=HOST, port=PORT)
