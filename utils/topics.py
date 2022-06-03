from enum import Enum

class TopicsPublications(Enum):
    # PUBLICATIONS
    DISBANDS_ACTION_DISBAND_MAC_AMBIENT_NOISE = 'disbands/action/{disbandMac}/ambient-noise'
    DISBANDS_ACTION_DISBAND_MAC_HEART_RATE = 'disbands/action/{disbandMac}/heart-rate'
    DISBANDS_ACTION_DISBAND_MAC_HUMIDITY = 'disbands/action/{disbandMac}/humidity'
    DISBANDS_ACTION_DISBAND_MAC_LIGHTNING = 'disbands/action/{disbandMac}/lightning'
    DISBANDS_ACTION_DISBAND_MAC_OXYGEN = 'disbands/action/{disbandMac}/oxygen'
    DISBANDS_ACTION_DISBAND_MAC_PRESSURE = 'disbands/action/{disbandMac}/pressure'
    DISBANDS_ACTION_DISBAND_MAC_TEMPERATURE = 'disbands/action/{disbandMac}/temperature'
    DISBEACS_ACTION_DISBEAC_MAC_LOCATION = 'disbeacs/action/{disbeacMac}/location'
    DISBANDS_ACTION_USER_ID_PAIR= 'disbands/action/{userId}/pair'
    DISBEACS_ACTION_USER_ID_PAIR= 'disbeacs/action/{userId}/pair'

class TopicsSubscriptions(Enum):
    # SUBSCRIPTIONS
    DISBANDS_EVENT_DISBAND_MAC_SYNC = 'disbands/event/{disbandMac}/sync'
    DISBANDS_EVENT_DISBAND_MAC_SYNC_ALARM = 'disbands/event/{disbandMac}/sync/alarm'
    DISBANDS_EVENT_DISBAND_MAC_SYNC_MEASURE_TIMES = 'disbands/event/{disbandMac}/sync/measure-times'
    DISBEACS_EVENT_DISBEAC_MAC_ACTIVE_DISBAND_MAC = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    DISBANDS_EVENT_DISBAND_MAC_VIBRATE = 'disbands/event/{disbandMac}/vibrate'
    