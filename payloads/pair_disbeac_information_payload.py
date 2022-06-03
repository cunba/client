from enum import Enum
from typing import Sequence
from models.entity import Entity



class PairDisbeacInformationPayload(Entity):

    def __init__(
            self,
            mac: str,
            model: str,
            version: str,
            userId: str,
            sentAt: float):
        self.mac = mac
        self.model = model
        self.version = version
        self.userId = userId
        self.sentAt = sentAt


