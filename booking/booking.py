import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc
import json

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]
        #stub
        channel = grpc.insecure_channel('localhost:3002')
        self.stub = showtime_pb2_grpc.showtimeStub(channel)
    def GetBookings (self, request, context):
        for booking in self.db:
            yield booking_pb2.Bookings(userid=booking['userid'], dates=booking['dates'])
    def GetBookingsByUserId(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.userid:
                return booking_pb2.Bookings(userid=booking['userid'], dates=booking['dates'])
        return booking_pb2.Bookings(userid="Not Found", dates=[])
    def get_movie_by_date(self, thedate):
        times = self.stub.GetMoviebyDate(thedate)
        #times =self.stub.GetTimes(showtime_pb2.EmptySchedule())
        return times

    def GetMoviesByDate(self, request, context):
        thedate = showtime_pb2.Date(date=str(request.date))
        times = self.get_movie_by_date(thedate)
        yield booking_pb2.Dates(date=times.date, movies=times.movies)
    # Write bookings to JSON file
    def write_bookings(self,bookings):
        with open('{}/data/bookings.json'.format("."), 'w') as f:
            json.dump({"bookings":  bookings}, f)

    def AddBookingByUserId(self, request, context):
        bookings = self.db
        userid = request.userid
        new_date = request.date
        new_movie_id = request.movie_id

        # Find if user already exists in bookings
        user_found = False
        for booking in bookings:
            if booking["userid"] == userid:
                user_found = True
                date_found = False

                # Check if the date exists for this user
                for date_entry in booking["dates"]:
                    if date_entry["date"] == new_date:
                        date_found = True

                        # Check if the movie already exists for this date
                        if new_movie_id in date_entry["movies"]:
                            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                            context.set_details('Movie already booked on this date')

                        # Add the movie to the existing date entry
                        date_entry["movies"].append(new_movie_id)
                        self.write_bookings(bookings)
                        return booking_pb2.AddBookingResponse(status="Movie added to the date")

                # If the date does not exist, add a new date entry
                if not date_found:
                    booking["dates"].append({"date": new_date, "movies": [new_movie_id]})
                    self.write_bookings(bookings)
                    return booking_pb2.AddBookingResponse(status="Date and movie added for user")

        # If the user does not exist, return an error or handle it by creating a new user
        if not user_found:
                return booking_pb2.AddBookingResponse(status="User not found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
