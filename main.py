#!/usr/bin/env python3
import configparser
import logging
import time

from models.messaging import Messaging

from payloads.disband_measure_information_payload import DisbandMeasureInformationPayload
from payloads.disband_lightning_information_payload import DisbandLightningInformationPayload
from payloads.pair_disband_information_payload import PairDisbandInformationPayload
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload
from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload
from payloads.disband_sync_information_payload import DisbandSyncInformationPayload
from payloads.disband_alarm_information_payload import DisbandAlarmInformationPayload
from payloads.disband_measure_times_information_payload import DisbandMeasureTimesInformationPayload
from models.sent_at import SentAt



# Config has the connection properties.
def getConfig():
    configParser = configparser.ConfigParser()
    configParser.read('config.ini')
    config = configParser['DEFAULT']
    return config


def disbandsEventDisbandMacSync(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandSyncInformationPayload = DisbandSyncInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandSyncInformationPayload))


def disbandsEventDisbandMacSyncAlarm(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandAlarmInformationPayload = DisbandAlarmInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandAlarmInformationPayload))


def disbandsEventDisbandMacSyncMeasureTimes(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMeasureTimesInformationPayload = DisbandMeasureTimesInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMeasureTimesInformationPayload))


def disbeacsEventDisbeacMacActiveDisbandMac(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    # payload = Payload.from_json(jsonString)
    # logging.info('Received message: ' + str(payload))


def disbandsEventDisbandMacVibrate(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    # payload = Payload.from_json(jsonString)
    # logging.info('Received message: ' + str(payload))



def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    disbandsEventDisbandMacSyncMessenger = Messaging(config, 'disbands/event/+/sync', disbandsEventDisbandMacSync)
    disbandsEventDisbandMacSyncMessenger.loop_start()
    disbandsEventDisbandMacSyncAlarmMessenger = Messaging(config, 'disbands/event/+/sync/alarm', disbandsEventDisbandMacSyncAlarm)
    disbandsEventDisbandMacSyncAlarmMessenger.loop_start()
    disbandsEventDisbandMacSyncMeasureTimesMessenger = Messaging(config, 'disbands/event/+/sync/measure-times', disbandsEventDisbandMacSyncMeasureTimes)
    disbandsEventDisbandMacSyncMeasureTimesMessenger.loop_start()
    disbeacsEventDisbeacMacActiveDisbandMacMessenger = Messaging(config, 'disbeacs/event/+/active/+', disbeacsEventDisbeacMacActiveDisbandMac)
    disbeacsEventDisbeacMacActiveDisbandMacMessenger.loop_start()
    disbandsEventDisbandMacVibrateMessenger = Messaging(config, 'disbands/event/+/vibrate', disbandsEventDisbandMacVibrate)
    disbandsEventDisbandMacVibrateMessenger.loop_start()

    # Example of how to publish a message. You will have to add arguments to the constructor on the next line:
    # payload = DisbandMeasureInformationPayload()
    # payloadJson = payload.to_json()

    while (True):
        # disbandsActionDisbandMacAmbientNoiseMessenger.publish('disbands/action/{disbandMac}/ambient-noise', payloadJson)
        time.sleep(1)

if __name__ == '__main__':
    main()

