import math
import time
from models.messaging import Messaging
from payloads.pair_disband_information_payload import PairDisbandInformationPayload
from utils.topics import TopicsPublications

class DisbandActionPair:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, mac, model, version, userId):
        payload = PairDisbandInformationPayload(mac, model, version, userId, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, mac, model, version, userId):
        payloadJson = self.create_payload(mac, model, version, userId)
        self.action.publish(self.topic, payloadJson)
    