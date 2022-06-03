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


"""node

The node module is responsible for managing a Bluetooth Low Energy (BLE) device/
node and allocating the needed resources.
"""


# IMPORT

from abc import ABCMeta, abstractmethod

# CLASSES

class NodeListener(object):
    """Interface used by the :class:`blue_st_sdk.node.Node` class to notify
    changes of a node's status.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_connect(self, node):
        """To be called whenever a node connects to a host.

        Args:
            node (:class:`blue_st_sdk.node.Node`): Node that has connected to a
                host.

        Raises:
            :exc:`NotImplementedError` if the method has not been implemented.
        """
        raise NotImplementedError('You must implement "on_connect()" to '
                                  'use the "NodeListener" class.')

    @abstractmethod
    def on_disconnect(self, node, unexpected=False):
        """To be called whenever a node disconnects from a host.

        Args:
            node (:class:`blue_st_sdk.node.Node`): Node that has disconnected
            from a host.
            unexpected (bool, optional): True if the disconnection is unexpected,
            False otherwise (called by the user).

        Raises:
            :exc:`NotImplementedError` if the method has not been implemented.
        """
        raise NotImplementedError('You must implement "on_disconnect()" to '
                                  'use the "NodeListener" class.')
