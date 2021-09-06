#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier représente l'interface de lancement de l'application.
    Cette interface contient 3 zones distinctes :
        - Le header de notre application
        - La liste de nos différents channels/groupes
        - La zone de contenu de nos channels après sélection d'un channel.
"""
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManagerException
from kivy.uix.scrollview import ScrollView

from src.config import config
from src.models.channel import Channel
from src.models.screens_manager import ScreensManager

Builder.load_file("{0}/landing.kv".format(config.VIEWS_DIR))


class ChannelsListButton(Button):
    pass


class EmptyChannels(Label):
    pass


class ConversationContainer(ScrollView):

    def __init__(self, channel_id):
        super(ConversationContainer, self).__init__()
        self.channel_id = channel_id


class InputsContainer(BoxLayout):
    pass


class ChannelsContainer(ScrollView):

    def __init__(self):
        super(ChannelsContainer, self).__init__()
        self.content = self.ids.channels_content
        self.sm = ScreensManager()

        self.init_channels_list()

    def init_channels_list(self):
        """
            Initialise la liste des channels disponibles.
            Si l'utilisateur fait partie de channels, les affiche dans le container concerné.
            Sinon, un message s'affiche précisant que l'utilisateur ne fait partie d'aucun channel.
        """
        self.content.clear_widgets()

        channels_list = self.get_channels_list()
        landing_screen = None

        try:
            landing_screen = self.sm.get_screen("landing")
        except ScreenManagerException:
            pass

        if channels_list:
            for channel in channels_list:
                channel_label = ChannelsListButton(text=channel.name)
                channel_label.bind(on_press=lambda a: landing_screen.display_conversation(channel.identifier))
                self.content.add_widget(channel_label)
        else:
            self.content.add_widget(EmptyChannels())

    def get_channels_list(self):
        """
            Récupère la liste des channels depuis la banque de données.
            :return: list : La liste des channels (objets) auxquels nous appartenons.
        """

        list_of_channels = []

        data_from_db = {
            "ABCDEF": {
                "name": "Pis",
                "icon_path": "",
                "participants": {}
            },
            "GHIJKL": {
                "name": "Pan",
                "icon_path": "",
                "participants": {}
            },
            "THIRD_UNIQUE_IDENTIFIER": {
                "name": "Douille",
                "icon_path": "",
                "participants": {}
            }
        }

        if data_from_db:

            for channel_id in data_from_db:
                channel_name = data_from_db[channel_id]["name"]
                icon_path = data_from_db[channel_id]["icon_path"]
                participants = data_from_db[channel_id]["participants"]

                inst = Channel(channel_id, channel_name, icon_path=icon_path, participants=participants)
                list_of_channels.append(inst)

            return list_of_channels

        return None


class LandingScreen(Screen):
    def __init__(self):
        super(LandingScreen, self).__init__()
        self.name = "landing"
        self.sm = ScreensManager()
        self.conv_box = self.ids.conversation_box
        self.channels_container = None

    def redirect_to_href(self, href):
        self.sm.redirect(href)

    def display_conversation(self, channel_id):
        self.conv_box.clear_widgets()
        self.conv_box.add_widget(ConversationContainer(channel_id))
        self.conv_box.add_widget(InputsContainer())

    def set_channels_list(self):
        self.channels_container = ChannelsContainer()
        self.ids.channels_box.add_widget(self.channels_container)
