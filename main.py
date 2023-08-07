import grpc

from book import book_route_pb2,book_route_pb2_grpc

def run():
    conn = grpc.insecure_channel('127.0.0.1:8088')
    client = book_route_pb2_grpc.BookServiceStub(channel=conn)
    reqeust = book_route_pb2.RequestData(name='jingtao')
    respnse = client.check(reqeust)
    print("received name:", respnse.name)
    print("received auther:", respnse.auther)
    print("received:", respnse.price)

if __name__ == '__main__':
    run()