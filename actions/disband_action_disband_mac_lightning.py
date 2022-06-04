import math
import time
from models.messaging import Messaging
from payloads.disband_lightning_information_payload import DisbandLightningInformationPayload
from utils.topics import TopicsPublications

class DisbandActionLightning:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic

    def create_payload(self, lightningData, redData, greenData, blueData, disbandMac):
        payload = DisbandLightningInformationPayload(lightningData, redData, greenData, blueData, disbandMac, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, lightningData, redData, greenData, blueData, disbandMac):
        payloadJson = self.create_payload(lightningData, redData, greenData, blueData, disbandMac)
        self.action.publish(self.topic, payloadJson)
    