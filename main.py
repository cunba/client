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
    disbandMac = device.get_tag().upper()
    disbandMacToTopic = ConvertMac().mac_to_string(device.get_tag().upper())

    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    # Creating the messaging for publications
    
    topic = 'disbands/action/{disbandMac}/ambient-noise'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_ambient_noise = DisbandActionAmbientNoise(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{disbandMac}/heart-rate'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_heart_rate = DisbandActionHeartRate(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{disbandMac}/humidity'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_humidity = DisbandActionHumidity(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{disbandMac}/lightning'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_lightning = DisbandActionLightning(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{disbandMac}/oxygen'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_oxygen = DisbandActionOxygen(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{disbandMac}/pressure'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_pressure = DisbandActionPressure(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{disbandMac}/temperature'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_action_temperature = DisbandActionTemperature(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbands/action/{userId}/pair'
    topicFormat = topic.format(userId = USER_ID)
    disband_action_pair = DisbandActionPair(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbeacs/action/{disbeacMac}/location'
    topicFormat = topic.format(disbeacMac = disbeacMac)
    disbeac_action_location = DisbeacActionLocation(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    topic = 'disbeacs/action/{userId}/pair'
    topicFormat = topic.format(userId = USER_ID)
    disbeac_action_pair = DisbeacActionPair(config, topicFormat)
    print('Subscribed to topic: ', topicFormat)

    # Subscribing to the topics

    topic = 'disbands/event/{disbandMac}/sync'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    DisbandEventDisbandMacSync(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/alarm'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    DisbandEventDisbandMacSyncAlarm(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/measure-times'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    DisbandEventDisbandMacSyncMeasureTimes(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbands/event/{disbandMac}/vibrate'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    DisbandEventDisbandMacVibrate(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    topicFormat = topic.format(disbeacMac = disbeacMac, disbandMac = disbandMacToTopic)
    DisbeacEventDisbandMacActiveDisbandMac(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    print()

    # Pairing the tilebox
    disband_action_pair.public_disband(disbandMac, 'TILEBOX', '0.1', USER_ID)

    while (True):
        # for feature in features:
        #     switch = {
        #         'ambient-noise': disband_action_ambient_noise,
        #         'heart-rate': disband_action_heart_rate,
        #         'humidity': disband_action_humidity,
        #         'lightning': disband_action_lightning,
        #         'oxygen': disband_action_oxygen,
        #         'pressure': disband_action_pressure,
        #         'temperature': disband_action_temperature
        #     }
        #     action = switch.get(feature.get_name().lower(), 'Invalid feature')
        #     connect_raspberry_tilebox.get_feature(feature, action)

        time.sleep(5)

if __name__ == '__main__':
    main()

