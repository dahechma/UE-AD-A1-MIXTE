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
        with grpc.insecure_channel('localhost:3002') as channel:
            self.stub = showtime_pb2_grpc.showtimeStub(channel)
    def GetBookings (self, request, context):
        for booking in self.db:
            yield booking_pb2.Bookings(userid=booking['userid'], dates=booking['dates'])
    def GetBookingsByUserId(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.userid:
                return booking_pb2.Bookings(userid=booking['userid'], dates=booking['dates'])
        return booking_pb2.Bookings(userid="Not Found", dates=[])
    def get_movie_by_date(self, stub, thedate):
        movies = stub.GetMoviebyDate(thedate)
        print("test")
        #return movies

    def GetMoviesByDate(self, request, context):
        thedate = showtime_pb2.Date(date=str(request.date))
        self.get_movie_by_date(self.stub, thedate)
        #return booking_pb2.Dates(date=movies.date, movies=movies.movies)
   
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
