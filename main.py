#!/usr/bin/env python3
import configparser
import logging
import time
from events import *
from events import disband_event_disband_mac_sync
from utils.topics import *
from actions import *

from connect_raspberry_tilebox import ConnectRaspberryTilebox

# Config has the connection properties.
def getConfig():
    configParser = configparser.ConfigParser()
    configParser.read('config.ini')
    config = configParser['DEFAULT']
    return config


def main():

    disbeacMac = ''
    disbandMac = ConnectRaspberryTilebox()

    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    # Creating the messaging for publications
    
    disband_action_ambient_noise = DisbandActionAmbientNoise(config)
    disband_action_heart_rate = DisbandActionHeartRate(config)
    disband_action_humidity = DisbandActionHumidity(config)
    disband_action_lightning = DisbandActionLightning(config)
    disband_action_oxygen = DisbandActionOxygen(config)
    disband_action_pressure = DisbandActionPressure(config)
    disband_action_temperature = DisbandActionTemperature(config)
    disband_action_pair = DisbandActionPair(config)
    disbeac_action_location = DisbeacActionLocation(config)
    disbeac_action_pair = DisbeacActionPair(config)

    # Subscribing to the topics

    disband_event_sync_topic = str(TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_SYNC)
    disband_event_sync_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSync(config, disband_event_sync_topic)

    disband_event_sync_alarm_topic = str(TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_SYNC_ALARM)
    disband_event_sync_alarm_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSyncAlarm(config, disband_event_sync_alarm_topic)

    disband_event_sync_measure_times_topic = str(TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_SYNC_MEASURE_TIMES)
    disband_event_sync_measure_times_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSyncMeasureTimes(config, disband_event_sync_measure_times_topic)

    disband_event_vibrate_topic = str(TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_VIBRATE)
    disband_event_vibrate_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacVibrate(config, disband_event_vibrate_topic)

    disbeac_event_active_topic = str(TopicsSubscriptions.DISBEACS_EVENT_DISBEAC_MAC_ACTIVE_DISBAND_MAC)
    disbeac_event_active_topic.format(disbeacMac = disbeacMac, disbandMac = disbandMac)
    DisbeacEventDisbandMacActiveDisbandMac(config, disbeac_event_active_topic)

    while (True):
        time.sleep(1)

if __name__ == '__main__':
    main()

