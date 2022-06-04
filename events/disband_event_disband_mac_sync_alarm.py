import logging
from models.messaging import Messaging
from payloads.disband_alarm_information_payload import DisbandAlarmInformationPayload

class DisbandEventDisbandMacSyncAlarm:
    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.event)
        self.messenger.loop_start()
    
    def event(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received json: ' + jsonString)
        disbandAlarmInformationPayload = DisbandAlarmInformationPayload.from_json(jsonString)
        self.load_tilebox(disbandAlarmInformationPayload)

    def load_tilebox(self, payload):
        # cargar codigo en el micro
        logging.info('Received message: ' + str(payload))