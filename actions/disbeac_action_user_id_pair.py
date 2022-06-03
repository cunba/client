import math
import time
from models.messaging import Messaging
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload
from utils.topics import TopicsPublications

class DisbeacActionPair:

    def __init__(self, config):
        self.action = Messaging(config)

    def create_payload(self, mac, model, version, userId):
        payload = PairDisbeacInformationPayload(mac, model, version, userId, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, mac, model, version, userId):
        topic = str(TopicsPublications.DISBEACS_ACTION_USER_ID_PAIR)
        topic = topic.format(userId = userId)
        payloadJson = self.create_payload(mac, model, version, userId)
        self.action.publish(topic, payloadJson)
    