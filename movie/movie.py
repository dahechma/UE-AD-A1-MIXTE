from flask import Flask, request, jsonify, make_response
from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
import resolvers as r

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

type_defs = load_schema_from_path('movie.graphql')
query = QueryType()
mutation = ObjectType('Mutation')
movie = ObjectType('Movie')


query.set_field("allMovies", r.all_movies)
query.set_field("movieById", r.movie_by_id)
query.set_field("movieByTitle", r.movie_by_title)
mutation.set_field("addMovie", r.add_movie)
mutation.set_field("updateMovieRating", r.update_movie_rating)
mutation.set_field("deleteMovie", r.delete_movie)

schema = make_executable_schema(type_defs, query, mutation,movie)

@app.route('/graphql', methods=['POST'])
def graphql_server(): 
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    print(f"Server running on port {PORT}")
    app.run(host=HOST, port=PORT)
