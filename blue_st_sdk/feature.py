################################################################################
# COPYRIGHT(c) 2018 STMicroelectronics                                         #
#                                                                              #
# Redistribution and use in source and binary forms, with or without           #
# modification, are permitted provided that the following conditions are met:  #
#   1. Redistributions of source code must retain the above copyright notice,  #
#      this list of conditions and the following disclaimer.                   #
#   2. Redistributions in binary form must reproduce the above copyright       #
#      notice, this list of conditions and the following disclaimer in the     #
#      documentation and/or other materials provided with the distribution.    #
#   3. Neither the name of STMicroelectronics nor the names of its             #
#      contributors may be used to endorse or promote products derived from    #
#      this software without specific prior written permission.                #
#                                                                              #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"  #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE    #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE   #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE    #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR          #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF         #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS     #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN      #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)      #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE   #
# POSSIBILITY OF SUCH DAMAGE.                                                  #
################################################################################


"""feature

The feature module represents a feature exported by a Bluetooth Low Energy (BLE)
device.
"""


# IMPORT

from abc import ABCMeta, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from blue_st_sdk.utils.blue_st_exceptions import (
    BlueSTInvalidDataException, BlueSTInvalidOperationException)
from blue_st_sdk.utils.python_utils import lock

# CLASSES

class FeatureListener(object):
    """Interface used by the :class:`blue_st_sdk.feature.Feature` class to
    notify changes of a feature's data.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_update(self, feature, sample):
        """To be called whenever the feature updates its data.

        Args:
            feature (:class:`blue_st_sdk.feature.Feature`): Feature that has
            updated.
            sample (:class:`blue_st_sdk.feature.Sample`): Sample data extracted
            from the feature.

        Raises:
            :exc:`NotImplementedError` if the method has not been implemented.
        """
        raise NotImplementedError(
            'You must implement "on_update()" to use the "FeatureListener" class.')


class Sample(object):
    """Class that contains the last data from the node."""

    def __init__(self, data, description, timestamp = 0):
        """Constructor.

        Args:
            data (list): Feature's data.
            description (list): Description of the data of the feature (list
            of :class:`blue_st_sdk.features.field.Field` objects).
            timestamp (int): Data's timestamp.
        """
        self._data = data
        self._description = description
        self._timestamp = timestamp
        self._notification_time = datetime.now()

    @classmethod
    def from_sample(self, copy_me):
        """Make a copy of a sample.
    
        Args:
            copy_me (:class:`blue_st_sdk.feature.Sample`): A given sample.
        """
        sample = Sample(
            list(copy_me._data),
            list(copy_me._description),
            copy_me._timestamp)
        sample._notification_time = copy_me._notification_time
        return sample

    def equals(self, sample):
        """Check the equality of the sample w.r.t. the given one.
    
        Args:
            sample (:class:`blue_st_sdk.feature.Sample`): A sample object.

        Returns:
            bool: True if the objects are equal (timestamp and data), False
            otherwise.
        """
        if sample is None:
            return False
        if isinstance(sample, self.Sample):
            return sample._timestamp == self._timestamp \
                and sorted(sample._data) == sorted(self._data)
        return False

    def get_data(self):
        """Get the data.

        Returns:
            The data of the sample.
        """
        return self._data

    def get_description(self):
        """Get the description.

        Returns:
            list: A list of :class:`blue_st_sdk.features.field.Field` describing
            the sample.
        """
        return self._description

    def get_timestamp(self):
        """Get the timestamp.

        Returns:
            int: The timestamp of the sample.
        """
        return self._timestamp

    def get_notification_time(self):
        """Get the notification time.

        Returns:
            int: The notification time.
        """
        return self._notification_time

    def __str__(self):
        """Get a string representing the last sample.

        Return:
            str: A string representing the last sample.
        """
        return "Timestamp: " + str(self._timestamp) + " Data: " + str(self._data)
