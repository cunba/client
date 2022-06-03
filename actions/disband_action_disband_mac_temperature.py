import math
import time
from models.messaging import Messaging
from payloads.disband_measure_information_payload import DisbandMeasureInformationPayload
from utils.topics import TopicsPublications

class DisbandActionTemperature:

    def __init__(self, config):
        self.action = Messaging(config)

    def create_payload(self, data, disbandMac):
        payload = DisbandMeasureInformationPayload(data, disbandMac, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, data, disbandMac):
        topic = str(TopicsPublications.DISBANDS_ACTION_DISBAND_MAC_PRESSURE)
        topic = topic.format(disbandMac = disbandMac)
        payloadJson = self.create_payload(data, disbandMac)
        self.action.publish(topic, payloadJson)
    