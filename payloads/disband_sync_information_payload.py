from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandSyncInformationPayload(Entity):

    class Measures(Entity):

        def __init__(
                self):
            pass


    def __init__(
            self,
            measures: Measures,
            sentAt: float):
        self.measures = measures
        self.sentAt = sentAt


