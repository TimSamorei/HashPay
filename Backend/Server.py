from concurrent import futures
import grpc
import HashPay_pb2
import HashPay_pb2_grpc
import Database
import Helper



class Identification:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def printID(self):
        print('Username: ' + self.username)
        print('Hashindex: ' + str(self.password.hashIndex))
        print('Hash: ' + str(self.password.hash))
        

class Password:

    def __init__(self, *args, **kwargs):
        self.hashIndex = kwargs.get('hashIndex')
        self.hash = kwargs.get('hash')


class HashPayServer(HashPay_pb2_grpc.HashPayServicer):

    def createAccount(self, request, context):
        status = Database.createAccount(con, request.requestor.username, request.requestor.password.hashIndex, request.requestor.password.hash)
        return HashPay_pb2.ServerReply(balance=0, Status=status)

    def refreshHash(self, request, context):
        return HashPay_pb2.ServerReply(balance=0, Status="REFRESHFAILURE")

    def payment(self, request, context):
        return HashPay_pb2.ServerReply(balance=0, Status="PAYMENTFAILURE")

    def deposit(self, request, context):
        return HashPay_pb2.ServerReply(balance=0, Status="DEPOSITFAILURE")
    
    def getBalance(self, request, context):
        return HashPay_pb2.ServerReply(balance=0, Status="BALANCEFAILURE")


        

    
        


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    HashPay_pb2_grpc.add_HashPayServicer_to_server(HashPayServer, server)
    server.add_insecure_port("[::]:1337")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()