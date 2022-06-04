#!/usr/bin/env python

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

################################################################################
# Author:  Davide Aliprandi, STMicroelectronics                                #
################################################################################


# DESCRIPTION
#
# This application example shows how to perform a Bluetooth Low Energy (BLE)
# scan, connect to a device, retrieve its exported features, and get push
# notifications from it.


# IMPORT

from __future__ import print_function

import json
import math
import os
import sys
import time
from abc import abstractmethod

from blue_st_sdk.feature import FeatureListener
from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm import \
    FeatureAudioADPCM
from blue_st_sdk.features.audio.adpcm.feature_audio_adpcm_sync import \
    FeatureAudioADPCMSync
from blue_st_sdk.manager import Manager, ManagerListener
from blue_st_sdk.node import NodeListener
from payloads.disband_measure_information_payload import DisbandMeasureInformationPayload

# PRECONDITIONS
#
# In case you want to modify the SDK, clone the repository and add the location
# of the "BlueSTSDK_Python" folder to the "PYTHONPATH" environment variable.
#
# On Linux:
#   export PYTHONPATH=/home/<user>/BlueSTSDK_Python


# CONSTANTS

# Presentation message.
INTRO = """#####################
# BlueST Connection #
#####################"""

# Bluetooth Scanning time in seconds (optional).
SCANNING_TIME_s = 5

# Number of notifications to get before disabling them.
NOTIFICATIONS = 1
TILEBOX_MAC = 'C0:50:08:32:26:56'
disbandMeasureInformationPayload = DisbandMeasureInformationPayload(0, '', 0)

# FUNCTIONS

#
# Printing intro.
#
def print_intro():
    print('\n' + INTRO + '\n')


# INTERFACES

#
# Implementation of the interface used by the Manager class to notify that a new
# node has been discovered or that the scanning starts/stops.
#
class MyManagerListener(ManagerListener):

    #
    # This method is called whenever a discovery process starts or stops.
    #
    # @param manager Manager instance that starts/stops the process.
    # @param enabled True if a new discovery starts, False otherwise.
    #
    def on_discovery_change(self, manager, enabled):
        print('Discovery %s.' % ('started' if enabled else 'stopped'))
        if not enabled:
            print()

    #
    # This method is called whenever a new node is discovered.
    #
    # @param manager Manager instance that discovers the node.
    # @param node    New node discovered.
    #
    def on_node_discovered(self, manager, node):
        print('New device discovered: %s.' % (node.get_name() + ': ' + node.get_tag()))


#
# Implementation of the interface used by the Node class to notify that a node
# has updated its status.
#
class MyNodeListener(NodeListener):

    #
    # To be called whenever a node connects to a host.
    #
    # @param node Node that has connected to a host.
    #
    def on_connect(self, node):
        print('Device %s connected.' % (node.get_name()))
        print()

    #
    # To be called whenever a node disconnects from a host.
    #
    # @param node       Node that has disconnected from a host.
    # @param unexpected True if the disconnection is unexpected, False otherwise
    #                   (called by the user).
    #
    def on_disconnect(self, node, unexpected=False):
        print('Device %s disconnected%s.' % \
            (node.get_name(), ' unexpectedly' if unexpected else ''))
        if unexpected:
            # Exiting.
            print('\nExiting...\n')
            sys.exit(0)


#
# Implementation of the interface used by the Feature class to notify that a
# feature has updated its data.
#
class MyFeatureListener(FeatureListener):

    _notifications = 0
    """Counting notifications to print only the desired ones."""

    def __init__(self, action):
        self.action = action

    #
    # To be called whenever the feature updates its data.
    #
    # @param feature Feature that has updated.
    # @param sample  Data extracted from the feature.
    #
    def on_update(self, feature, sample):
        if self._notifications < NOTIFICATIONS:
            self._notifications += 1
            if sample.get_data()[0] > 0:
                self.action.public_measure(sample.get_data()[0], TILEBOX_MAC)

class ConnectRaspberryTilebox:

    # def __init__(self):
        # self.device = None
        # self.features = None

    def bluetooth_connection(self):

        # Printing intro.
        print_intro()

        # Creating Bluetooth Manager.
        manager = Manager.instance()
        manager_listener = MyManagerListener()
        manager.add_listener(manager_listener)

        # Synchronous discovery of Bluetooth devices.
        print('Scanning Bluetooth devices...\n')
        manager.discover(SCANNING_TIME_s)

        # Getting discovered devices.
        discovered_devices = manager.get_nodes()

        # Listing discovered devices.
        if not discovered_devices:
            print('No Bluetooth devices found. Exiting...\n')
            sys.exit(0)
            
        for device_discovered in discovered_devices:
            if device_discovered.get_tag().upper() == TILEBOX_MAC:
                self.device = device_discovered
                print('%s found.' % (self.device.get_tag()))
                break
        
        if self.device == None:
            print('%s not found.' % (self.device.get_tag()))

        node_listener = MyNodeListener()
        self.device.add_listener(node_listener)

        # Connecting to the device.
        print('Connecting to %s...' % (self.device.get_tag()))
        if not self.device.connect():
            print('Connection failed.\n')
        else:
            disbandMeasureInformationPayload.disbandMac = self.device.get_tag()
        
        # self.features = self.device.get_features()
        return self.device

    def get_feature(self, feature, action):
        # Getting features.
        # Enabling notifications.
        feature_listener = MyFeatureListener(action)
        feature.add_listener(feature_listener)
        self.device.enable_notifications(feature)
        # Handling audio case (both audio features have to be enabled).
        # if isinstance(feature, FeatureAudioADPCM):
        #     audio_sync_feature_listener = MyFeatureListener()
        #     audio_sync_feature.add_listener(audio_sync_feature_listener)
        #     device.enable_notifications(audio_sync_feature)
        # elif isinstance(feature, FeatureAudioADPCMSync):
        #     audio_feature_listener = MyFeatureListener()
        #     audio_feature.add_listener(audio_feature_listener)
        #     device.enable_notifications(audio_feature)

        # Getting notifications.
        notifications = 0
        while notifications < NOTIFICATIONS:
            if self.device.wait_for_notifications(0.05):
                notifications += 1


            

            # Handling audio case (both audio features have to be disabled).
            # if isinstance(feature, FeatureAudioADPCM):
            #     device.disable_notifications(audio_sync_feature)
            #     audio_sync_feature.remove_listener(audio_sync_feature_listener)
            # elif isinstance(feature, FeatureAudioADPCMSync):
            #     device.disable_notifications(audio_feature)
            #     audio_feature.remove_listener(audio_feature_listener)
