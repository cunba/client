#!/usr/bin/env python3
import configparser
import logging
import time
from events import *
from actions import *

from connect_raspberry_tilebox import ConnectRaspberryTilebox
from utils.convert_mac import ConvertMac

USER_ID = "c3ae7388-f3c8-43b9-84ea-eba374b72dcd"

# Config has the connection properties.
def getConfig():
    configParser = configparser.ConfigParser()
    configParser.read('config.ini')
    config = configParser['DEFAULT']
    return config


def main():

    disbeacMac = ''
    connect_raspberry_tilebox = ConnectRaspberryTilebox()
    device = connect_raspberry_tilebox.bluetooth_connection()
    features = device.get_features()
    disbandMac = ConvertMac().mac_to_string(device.get_tag().upper())

    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    # Creating the messaging for publications
    
    topic = 'disbands/action/{disbandMac}/ambient-noise'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_ambient_noise = DisbandActionAmbientNoise(config, topicFormat)

    topic = 'disbands/action/{disbandMac}/heart-rate'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_heart_rate = DisbandActionHeartRate(config, topicFormat)

    topic = 'disbands/action/{disbandMac}/humidity'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_humidity = DisbandActionHumidity(config, topicFormat)

    topic = 'disbands/action/{disbandMac}/lightning'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_lightning = DisbandActionLightning(config, topicFormat)

    topic = 'disbands/action/{disbandMac}/oxygen'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_oxygen = DisbandActionOxygen(config, topicFormat)

    topic = 'disbands/action/{disbandMac}/pressure'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_pressure = DisbandActionPressure(config, topicFormat)

    topic = 'disbands/action/{disbandMac}/temperature'
    topicFormat = topic.format(disbandMac = disbandMac)
    disband_action_temperature = DisbandActionTemperature(config, topicFormat)

    topic = 'disbands/action/{userId}/pair'
    topicFormat = topic.format(userId = USER_ID)
    disband_action_pair = DisbandActionPair(config, topicFormat)

    topic = 'disbeacs/action/{disbeacMac}/location'
    topicFormat = topic.format(disbeacMac = disbeacMac)
    disbeac_action_location = DisbeacActionLocation(config, topicFormat)

    topic = 'disbeacs/action/{userId}/pair'
    topicFormat = topic.format(userId = USER_ID)
    disbeac_action_pair = DisbeacActionPair(config, topicFormat)

    # Subscribing to the topics

    topic = 'disbands/event/{disbandMac}/sync'
    topicFormat = topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSync(config, topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/alarm'
    topicFormat = topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSyncAlarm(config, topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/measure-times'
    topicFormat = topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSyncMeasureTimes(config, topicFormat)

    topic = 'disbands/event/{disbandMac}/vibrate'
    topicFormat = topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacVibrate(config, topicFormat)

    topic = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    topicFormat = topic.format(disbeacMac = disbeacMac, disbandMac = disbandMac)
    DisbeacEventDisbandMacActiveDisbandMac(config, topicFormat)

    while (True):
        for feature in features:
            switch = {
                'ambient-noise': disband_action_ambient_noise,
                'heart-rate': disband_action_heart_rate,
                'humidity': disband_action_humidity,
                'lightning': disband_action_lightning,
                'oxygen': disband_action_oxygen,
                'pressure': disband_action_pressure,
                'temperature': disband_action_temperature
            }
            action = switch.get(feature.get_name().lower(), 'Invalid feature')
            connect_raspberry_tilebox.get_feature(feature, action)

        time.sleep(5)

if __name__ == '__main__':
    main()

