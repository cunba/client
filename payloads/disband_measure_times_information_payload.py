from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandMeasureTimesInformationPayload(Entity):

    class Sensors(Entity):

        def __init__(
                self):
            pass


    def __init__(
            self,
            sensors: Sensors,
            sentAt: float):
        self.sensors = sensors
        self.sentAt = sentAt


