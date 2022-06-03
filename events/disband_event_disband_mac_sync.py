import logging
from models.messaging import Messaging
from payloads.disband_sync_information_payload import DisbandSyncInformationPayload

class DisbandActionDisbandMacSync:
    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received json: ' + jsonString)
        disbandSyncInformationPayload = DisbandSyncInformationPayload.from_json(jsonString)
        self.load_tilebox(disbandSyncInformationPayload)

    def load_tilebox(self, payload):
        # cargar codigo en el micro
        logging.info('Received message: ' + str(payload))