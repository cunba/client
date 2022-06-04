import math
import time
from models.messaging import Messaging
from payloads.pair_disband_information_payload import PairDisbandInformationPayload
from utils.timestamp import Timestamp

class DisbandActionPair:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, mac, model, version, userId):
        payload = PairDisbandInformationPayload(mac, model, version, userId, Timestamp().get_now_timestamp_miliseconds())
        return payload.to_json()

    def public_disband(self, mac, model, version, userId):
        print(self.topic)
        payloadJson = self.create_payload(mac, model, version, userId)
        self.action.publish(self.topic, payloadJson)
    