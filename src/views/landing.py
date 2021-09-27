#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier représente l'interface de lancement de l'application.
    Cette interface contient 3 zones distinctes :
        - Le header de notre application
        - La liste de nos différents channels/groupes
        - La zone de contenu de nos channels après sélection d'un channel.
"""
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from src.config import config
from src.models.screens_manager import ScreensManager
from src.views.channels_container import ChannelsContainer
from src.views.widgets import RoomsContainer, ConversationContainer, InputsContainer

Builder.load_file("{0}/header.kv".format(config.VIEWS_DIR))
Builder.load_file("{0}/participants.kv".format(config.VIEWS_DIR))
Builder.load_file("{0}/conversation.kv".format(config.VIEWS_DIR))
Builder.load_file("{0}/rooms.kv".format(config.VIEWS_DIR))
Builder.load_file("{0}/channels.kv".format(config.VIEWS_DIR))
Builder.load_file("{0}/landing.kv".format(config.VIEWS_DIR))


class LandingScreen(Screen):
    def __init__(self):
        super(LandingScreen, self).__init__()
        self.name = "landing"
        self.sm = ScreensManager()
        self.conv_box = self.ids.conversation_box
        self.rooms_box = self.ids.rooms_box
        self.channels_container = None

    def redirect_to_href(self, href):
        """
            Gestion des évènements de redirection du Screen.
        """
        self.sm.redirect(href)

    def display_rooms(self, channel_id):
        """
            Permet la mise à jour de la liste des rooms après un clic sur le nom d'un channel.
            :param channel_id: L'identifiant du channel concerné.
        """
        self.conv_box.clear_widgets()
        self.rooms_box.clear_widgets()
        self.rooms_box.add_widget(RoomsContainer(channel_id))

    def display_conversation(self, room_id):
        """
            Permet la mise à jour de la conversation active après un clic sur le nom d'une room.
            :param room_id: L'identifiant de la room concernée.
        """
        self.conv_box.clear_widgets()
        self.conv_box.add_widget(ConversationContainer(room_id))
        self.conv_box.add_widget(InputsContainer())

    def set_channels_list(self):
        self.channels_container = ChannelsContainer()
        self.ids.channels_box.add_widget(self.channels_container)
