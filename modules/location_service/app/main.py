import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
from kafka import KafkaProducer
from app.services import LocationService


class LocationService(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(request_value)

        TOPIC_NAME = 'location_topic'
        KAFKA_SERVER = 'localhost:9092'
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        producer.send(TOPIC_NAME, json.dumps(request_value).encode())
        producer.flush()
        return location_pb2.LocationResponse(**request_value)

    def Getter(self,request, context):
        location_id = request.location_id
        location = LocationService.retrieve(location_id)
        return location_pb2.LocationResponse(
                    id = location.id,
                    person_id = location.person_id,
                    longitude = location.longitude,
                    latitude = location.latitude,
                    creation_time = location.creation_time,
                )

    

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

