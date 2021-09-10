#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier représente une vue contenant la liste des channels disponible à l'utilisateur.
"""
from kivy.uix.screenmanager import ScreenManagerException
from kivy.uix.scrollview import ScrollView

from src.libs.sorting.dict_sort import dict_sort
from src.models.channel import Channel
from src.models.screens_manager import ScreensManager
from src.views.widgets import ChannelsListButton, EmptyChannels


class ChannelsContainer(ScrollView):

    def __init__(self):
        super(ChannelsContainer, self).__init__()
        self.content = self.ids.channels_content
        self.sm = ScreensManager()

        self.init_channels_list()

    def init_channels_list(self):
        """
            [BASE]
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
                channel_label.bind(on_press=lambda a: landing_screen.display_rooms(channel.identifier))
                self.content.add_widget(channel_label)
        else:
            self.content.add_widget(EmptyChannels())

    def get_channels_list(self):
        """
            [BASE]
            Récupère la liste des channels depuis la banque de données.
            :return: list : La liste des Channel (objets) auxquels nous appartenons, triés par leurs noms.
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

            # Trier sur le nom
            data_from_db = dict_sort(data_from_db, "name")

            for channel_id in data_from_db:
                channel_name = data_from_db[channel_id]["name"]
                icon_path = data_from_db[channel_id]["icon_path"]
                participants = data_from_db[channel_id]["participants"]

                inst = Channel(channel_id, channel_name, icon_path=icon_path, participants=participants)
                list_of_channels.append(inst)

            return list_of_channels

        return None
