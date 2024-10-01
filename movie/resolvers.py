import json

            
with open('databases/movies.json', 'r') as f:
    movies = json.load(f)["movies"]

def all_movies(_, info):
    return movies

def movie_by_id(_, info, id):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return None

def movie_by_title(_, info, title):
    for movie in movies:
        if movie["title"] == title:
            return movie
    return None

def add_movie(_, info, id, title, director, rating):
    for movie in movies:
        if movie["id"] == id:
            return "Movie ID already exists."
    
    new_movie = {"id": id, "title": title, "director": director, "rating": rating}
    movies.append(new_movie)
    write_movies()
    return "Movie added successfully."

def update_movie_rating(_, info, id, rating):
    for movie in movies:
        if movie["id"] == id:
            movie["rating"] = rating
            write_movies()
            return "Movie rating updated successfully."
    return "Movie ID not found."

def delete_movie(_, info, id):
    global movies
    movies = [movie for movie in movies if movie["id"] != id]
    write_movies()
    return "Movie deleted successfully."

def write_movies():
    with open('databases/movies.json', 'w') as f:
        json.dump({"movies": movies}, f)
           