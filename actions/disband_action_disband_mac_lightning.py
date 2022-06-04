import math
import time
from models.messaging import Messaging
from payloads.disband_lightning_information_payload import DisbandLightningInformationPayload
from utils.timestamp import Timestamp

class DisbandActionLightning:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, lightningData, redData, greenData, blueData, disbandMac):
        payload = DisbandLightningInformationPayload(lightningData, redData, greenData, blueData, disbandMac, Timestamp().get_now_timestamp_miliseconds())
        return payload.to_json()

    def public_measure(self, lightningData, redData, greenData, blueData, disbandMac):
        payloadJson = self.create_payload(lightningData, redData, greenData, blueData, disbandMac)
        self.action.publish(self.topic, payloadJson)
    