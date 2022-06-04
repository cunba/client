#!/usr/bin/env python3
import configparser
import logging
import time
from events import *
from events import disband_event_disband_mac_sync
from actions import *

from connect_raspberry_tilebox import ConnectRaspberryTilebox
from utils.convert_mac import ConvertMac

# Config has the connection properties.
def getConfig():
    configParser = configparser.ConfigParser()
    configParser.read('config.ini')
    config = configParser['DEFAULT']
    return config


def main():

    disbeacMac = ''
    userId = ''
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
    topicFormat = topic.format(userId = userId)
    disband_action_pair = DisbandActionPair(config, topicFormat)

    topic = 'disbeacs/action/{disbeacMac}/location'
    topicFormat = topic.format(disbeacMac = disbeacMac)
    disbeac_action_location = DisbeacActionLocation(config, topicFormat)

    topic = 'disbeacs/action/{userId}/pair'
    topicFormat = topic.format(userId = userId)
    disbeac_action_pair = DisbeacActionPair(config, topicFormat)

    # Subscribing to the topics

    disband_event_sync_topic = 'disbands/event/{disbandMac}/sync'
    disband_event_sync_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSync(config, disband_event_sync_topic)

    disband_event_sync_alarm_topic = 'disbands/event/{disbandMac}/sync/alarm'
    disband_event_sync_alarm_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSyncAlarm(config, disband_event_sync_alarm_topic)

    disband_event_sync_measure_times_topic = 'disbands/event/{disbandMac}/sync/measure-times'
    disband_event_sync_measure_times_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacSyncMeasureTimes(config, disband_event_sync_measure_times_topic)

    disband_event_vibrate_topic = 'disbands/event/{disbandMac}/vibrate'
    disband_event_vibrate_topic.format(disbandMac = disbandMac)
    DisbandEventDisbandMacVibrate(config, disband_event_vibrate_topic)

    disbeac_event_active_topic = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    disbeac_event_active_topic.format(disbeacMac = disbeacMac, disbandMac = disbandMac)
    DisbeacEventDisbandMacActiveDisbandMac(config, disbeac_event_active_topic)

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

