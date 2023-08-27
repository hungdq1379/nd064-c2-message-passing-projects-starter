import grpc
import locations_pb2
import locations_pb2_grpc

 
channel = grpc.insecure_channel("localhost:5005")
stub = locations_pb2_grpc.LocationServiceStub(channel)

location = locations_pb2.Location(
    id="123",
    person_id="123",
    creation_time="2023-08-27",
    latitude="123456789",
    longitude="123456789"
)

response = stub.CreateLocation(location)