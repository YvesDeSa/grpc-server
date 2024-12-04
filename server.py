from concurrent import futures
import grpc
import offers_pb2
import offers_pb2_grpc

class OfferService(offers_pb2_grpc.OfferServiceServicer):
    def GetOffers(self, request, context):
        # Dados mock para ofertas
        offers = [
            offers_pb2.Offer(id="1", title="Offer 1", image="/images/offer1.jpg", price=19.99),
            offers_pb2.Offer(id="2", title="Offer 2", image="/images/offer2.jpg", price=29.99),
            offers_pb2.Offer(id="3", title="Offer 3", image="/images/offer3.jpg", price=39.99),
        ]
        return offers_pb2.OfferResponse(offers=offers[:request.limit])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    offers_pb2_grpc.add_OfferServiceServicer_to_server(OfferService(), server)
    server.add_insecure_port("[::]:50051")
    print("Server started at [::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
