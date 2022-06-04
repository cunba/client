#!/usr/bin/env python3
import configparser
import logging
import time
from events import *
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

    connection = ConnectRaspberryTilebox()

    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    # Creating the messaging for publications
    
    DisbandActionAmbientNoise(config)
    DisbandActionHeartRate(config)
    DisbandActionHumidity(config)
    DisbandActionLightning(config)
    DisbandActionOxygen(config)
    DisbandActionPressure(config)
    DisbandActionTemperature(config)
    DisbandActionPair(config)
    DisbeacActionLocation(config)
    DisbeacActionPair(config)

    # Subscribing to the topics

    DisbandEventDisbandMacSync(config, TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_SYNC)
    DisbandEventDisbandMacSyncAlarm(config, TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_SYNC_ALARM)
    DisbandEventDisbandMacSyncMeasureTimes(config, TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_SYNC_MEASURE_TIMES)
    DisbandEventDisbandMacVibrate(config, TopicsSubscriptions.DISBANDS_EVENT_DISBAND_MAC_VIBRATE)
    DisbeacEventDisbandMacActiveDisbandMac(config, TopicsSubscriptions.DISBEACS_EVENT_DISBEAC_MAC_ACTIVE_DISBAND_MAC)

    while (True):
        time.sleep(1)

if __name__ == '__main__':
    main()

