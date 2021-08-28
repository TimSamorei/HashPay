# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import HashPay_pb2 as HashPay__pb2


class HashPayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createAccount = channel.unary_unary(
                '/de.samorei.hashpay.HashPay/createAccount',
                request_serializer=HashPay__pb2.CreationRequest.SerializeToString,
                response_deserializer=HashPay__pb2.ServerReply.FromString,
                )
        self.refreshHash = channel.unary_unary(
                '/de.samorei.hashpay.HashPay/refreshHash',
                request_serializer=HashPay__pb2.RefreshRequest.SerializeToString,
                response_deserializer=HashPay__pb2.ServerReply.FromString,
                )
        self.payment = channel.unary_unary(
                '/de.samorei.hashpay.HashPay/payment',
                request_serializer=HashPay__pb2.PaymentRequest.SerializeToString,
                response_deserializer=HashPay__pb2.ServerReply.FromString,
                )
        self.deposit = channel.unary_unary(
                '/de.samorei.hashpay.HashPay/deposit',
                request_serializer=HashPay__pb2.DepositRequest.SerializeToString,
                response_deserializer=HashPay__pb2.ServerReply.FromString,
                )
        self.getBalance = channel.unary_unary(
                '/de.samorei.hashpay.HashPay/getBalance',
                request_serializer=HashPay__pb2.BalanceRequest.SerializeToString,
                response_deserializer=HashPay__pb2.ServerReply.FromString,
                )


class HashPayServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def refreshHash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def payment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HashPayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.createAccount,
                    request_deserializer=HashPay__pb2.CreationRequest.FromString,
                    response_serializer=HashPay__pb2.ServerReply.SerializeToString,
            ),
            'refreshHash': grpc.unary_unary_rpc_method_handler(
                    servicer.refreshHash,
                    request_deserializer=HashPay__pb2.RefreshRequest.FromString,
                    response_serializer=HashPay__pb2.ServerReply.SerializeToString,
            ),
            'payment': grpc.unary_unary_rpc_method_handler(
                    servicer.payment,
                    request_deserializer=HashPay__pb2.PaymentRequest.FromString,
                    response_serializer=HashPay__pb2.ServerReply.SerializeToString,
            ),
            'deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.deposit,
                    request_deserializer=HashPay__pb2.DepositRequest.FromString,
                    response_serializer=HashPay__pb2.ServerReply.SerializeToString,
            ),
            'getBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.getBalance,
                    request_deserializer=HashPay__pb2.BalanceRequest.FromString,
                    response_serializer=HashPay__pb2.ServerReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'de.samorei.hashpay.HashPay', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HashPay(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.samorei.hashpay.HashPay/createAccount',
            HashPay__pb2.CreationRequest.SerializeToString,
            HashPay__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def refreshHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.samorei.hashpay.HashPay/refreshHash',
            HashPay__pb2.RefreshRequest.SerializeToString,
            HashPay__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def payment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.samorei.hashpay.HashPay/payment',
            HashPay__pb2.PaymentRequest.SerializeToString,
            HashPay__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.samorei.hashpay.HashPay/deposit',
            HashPay__pb2.DepositRequest.SerializeToString,
            HashPay__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.samorei.hashpay.HashPay/getBalance',
            HashPay__pb2.BalanceRequest.SerializeToString,
            HashPay__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
