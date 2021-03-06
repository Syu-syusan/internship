# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: echo/v1/echo.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import echo.v1.echo_pb2


class EchoBase(abc.ABC):

    @abc.abstractmethod
    async def Echo(self, stream: 'grpclib.server.Stream[echo.v1.echo_pb2.EchoRequest, echo.v1.echo_pb2.EchoResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/skeleton.echo.v1.Echo/Echo': grpclib.const.Handler(
                self.Echo,
                grpclib.const.Cardinality.UNARY_UNARY,
                echo.v1.echo_pb2.EchoRequest,
                echo.v1.echo_pb2.EchoResponse,
            ),
        }


class EchoStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Echo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/skeleton.echo.v1.Echo/Echo',
            echo.v1.echo_pb2.EchoRequest,
            echo.v1.echo_pb2.EchoResponse,
        )
