# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import showtime_pb2 as showtime__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in showtime_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class showtimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTimes = channel.unary_stream(
                '/showtime.showtime/GetTimes',
                request_serializer=showtime__pb2.EmptySchedule.SerializeToString,
                response_deserializer=showtime__pb2.Schedule.FromString,
                _registered_method=True)
        self.GetMoviebyDate = channel.unary_unary(
                '/showtime.showtime/GetMoviebyDate',
                request_serializer=showtime__pb2.Date.SerializeToString,
                response_deserializer=showtime__pb2.Schedule.FromString,
                _registered_method=True)


class showtimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTimes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMoviebyDate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_showtimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTimes': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTimes,
                    request_deserializer=showtime__pb2.EmptySchedule.FromString,
                    response_serializer=showtime__pb2.Schedule.SerializeToString,
            ),
            'GetMoviebyDate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMoviebyDate,
                    request_deserializer=showtime__pb2.Date.FromString,
                    response_serializer=showtime__pb2.Schedule.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'showtime.showtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('showtime.showtime', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class showtime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/showtime.showtime/GetTimes',
            showtime__pb2.EmptySchedule.SerializeToString,
            showtime__pb2.Schedule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMoviebyDate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/showtime.showtime/GetMoviebyDate',
            showtime__pb2.Date.SerializeToString,
            showtime__pb2.Schedule.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
