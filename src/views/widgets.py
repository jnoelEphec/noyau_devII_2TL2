#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier contient les déclarations des différents widgets déclarés dans les kv.files.
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class ChannelsListButton(Button):
    pass


class EmptyChannels(Label):
    pass


class ConversationContainer(ScrollView):

    def __init__(self, room_id):
        super(ConversationContainer, self).__init__()
        self.room_id = room_id


class RoomsContainer(ScrollView):
    def __init__(self, channel_id):
        super(RoomsContainer, self).__init__()
        self.channel_id = channel_id


class InputsContainer(BoxLayout):
    pass
