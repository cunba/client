import math
import time
from models.messaging import Messaging
from payloads.disband_measure_information_payload import DisbandMeasureInformationPayload
from utils.topics import TopicsPublications

class DisbandActionTemperature:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, data, disbandMac):
        payload = DisbandMeasureInformationPayload(data, disbandMac, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, data, disbandMac):
        payloadJson = self.create_payload(data, disbandMac)
        self.action.publish(self.topic, payloadJson)
    