import math
import time
from models.messaging import Messaging
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload
from utils.timestamp import Timestamp

class DisbeacActionPair:

    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, mac, model, version, userId):
        payload = PairDisbeacInformationPayload(mac, model, version, userId, Timestamp().get_now_timestamp_miliseconds())
        return payload.to_json()

    def public_disbeac(self, mac, model, version, userId):
        payloadJson = self.create_payload(mac, model, version, userId)
        self.action.publish(self.topic, payloadJson)
    