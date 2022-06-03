import math
import time
from models.messaging import Messaging
from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload
from utils.topics import TopicsPublications

class DisbeacsActionTemperature:

    def __init__(self, config):
        self.action = Messaging(config)

    def create_payload(self, data, disbeacMac):
        payload = DisbeacLocationInformationPayload(data, disbeacMac, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, data, disbeacMac):
        topic = str(TopicsPublications.DISBEACS_ACTION_DISBEAC_MAC_LOCATION)
        topic = topic.format(disbeacMac = disbeacMac)
        payloadJson = self.create_payload(data, disbeacMac)
        self.action.publish(topic, payloadJson)
    