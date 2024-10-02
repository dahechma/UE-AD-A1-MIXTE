import json

with open('databases/users.json', 'r') as f:
    users = json.load(f)["users"]

with open('databases/movies.json', 'r') as f:
    movies = json.load(f)["movies"]

with open('databases/bookings.json', 'r') as f:
    bookings = json.load(f)["bookings"]

def resolve_users(*_):
    return users

def resolve_user_by_id(_, info, id):
    for user in users:
        if user['id'] == id:
            return user
    return None

def resolve_movies(*_):
    return movies

def resolve_bookings(_, info, userId):
    for booking in bookings:
        if booking['userId'] == userId:
            return booking
    return None

def resolve_movies_info(_, info, userId):
    user_booking = resolve_bookings(_, info, userId)
    if not user_booking:
        return None

    movie_ids = []
    for date in user_booking['dates']:
        movie_ids.extend(date['movies'])

    movie_info = [movie for movie in movies if movie['id'] in movie_ids]
    return movie_info
