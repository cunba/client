from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandLightningInformationPayload(Entity):

    def __init__(
            self,
            lightning: float,
            redLightning: float,
            greenLightning: float,
            blueLightning: float,
            disbandMac: str,
            sentAt: float):
        self.lightning = lightning
        self.redLightning = redLightning
        self.greenLightning = greenLightning
        self.blueLightning = blueLightning
        self.disbandMac = disbandMac
        self.sentAt = sentAt


