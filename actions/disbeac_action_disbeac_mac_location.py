import math
import time
from models.messaging import Messaging
from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload

class DisbeacActionLocation:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, data, disbeacMac):
        payload = DisbeacLocationInformationPayload(data, disbeacMac, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, data, disbeacMac):
        payloadJson = self.create_payload(data, disbeacMac)
        self.action.publish(self.topic, payloadJson)
    