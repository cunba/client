import logging
from models.messaging import Messaging
from payloads.disband_measure_times_information_payload import DisbandMeasureTimesInformationPayload

class DisbandEventDisbandMacSyncMeasureTimes:
    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.event)
        self.messenger.loop_start()
    
    def event(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received json: ' + jsonString)
        disbandMeasureTimesInformationPayload = DisbandMeasureTimesInformationPayload.from_json(jsonString)
        self.load_tilebox(disbandMeasureTimesInformationPayload)

    def load_tilebox(self, payload):
        # cargar codigo en el micro
        logging.info('Received message: ' + str(payload))