from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandMeasureInformationPayload(Entity):

    def __init__(
            self,
            data: float,
            disbandMac: str,
            sentAt: float):
        self.data = data
        self.disbandMac = disbandMac
        self.sentAt = sentAt


