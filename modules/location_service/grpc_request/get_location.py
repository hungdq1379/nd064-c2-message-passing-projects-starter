import grpc
import locations_pb2
import locations_pb2_grpc


channel = grpc.insecure_channel("localhost:5005")
stub = locations_pb2_grpc.LocationServiceStub(channel)

response = stub.GetLocation(locations_pb2.LocationId(location_id="1"))
print(response)