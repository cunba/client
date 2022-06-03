from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandMeasureInformationPayload(Entity):

    def __init__(
            self,
            data: float,
            sentAt: float):
        self.data = data
        self.sentAt = sentAt


