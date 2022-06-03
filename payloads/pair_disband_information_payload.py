from enum import Enum
from typing import Sequence
from models.entity import Entity



class PairDisbandInformationPayload(Entity):

    def __init__(
            self,
            model: str,
            version: str,
            userId: str,
            sentAt: float):
        self.model = model
        self.version = version
        self.userId = userId
        self.sentAt = sentAt


