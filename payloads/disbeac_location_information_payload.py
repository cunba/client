from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbeacLocationInformationPayload(Entity):

    def __init__(
            self,
            latitude: str,
            longitude: str,
            sentAt: float):
        self.latitude = latitude
        self.longitude = longitude
        self.sentAt = sentAt


