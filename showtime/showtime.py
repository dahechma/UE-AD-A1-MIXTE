import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json

class showtimeServicer(showtime_pb2_grpc.showtimeServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]
    def GetTimes (self, request, context): 
        for time in self.db:
            yield showtime_pb2.Schedule(date=time['date'], movies=time['movies'])
    def GetMoviebyDate(self, request, context):
        print("GetMovie")
        for time in self.db:
            if time['date'] == request.date:
                return showtime_pb2.Schedule(date=time['date'], movies=time['movies'])
        return showtime_pb2.Schedule(date="Not Found", movies=[])
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_showtimeServicer_to_server(showtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
