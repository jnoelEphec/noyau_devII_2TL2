#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier contient les déclarations des différents widgets déclarés dans les kv.files.
"""
import json

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManagerException
from kivy.uix.scrollview import ScrollView

from src.config import config
from src.models.screens_manager import ScreensManager


class TeamsListButton(Button):
    pass


class EmptyTeams(Label):
    pass


class GroupTitleRow(BoxLayout):
    pass


class GroupLabel(Label):
    pass


class GroupAddButton(Button):
    pass


class ChannelsListButton(Button):
    pass


class ChannelsContainer(ScrollView):
    def __init__(self, channels_list):
        super(ChannelsContainer, self).__init__()
        self.channels_list = channels_list
        self.channels_container = self.ids.channels_content
        self.sm = ScreensManager()
        self.landing_screen = self.get_landing_screen()

        self.generate_list_rows()

    def get_landing_screen(self):
        try:
            landing_screen = self.sm.get_screen("landing")
            return landing_screen
        except ScreenManagerException:
            return None

    def generate_list_rows(self):
        groups = {}

        for channel in self.channels_list:
            group_name = channel.group.name
            if group_name not in groups:
                group = BoxLayout(orientation="vertical", size_hint_y=None)
                title_row = GroupTitleRow()
                title_label = GroupLabel(text=group_name)
                title_add_btn = GroupAddButton(on_press=lambda a, _grp=group_name: self.add_new_channel(_grp))
                title_row.add_widget(title_label)
                title_row.add_widget(title_add_btn)
                group.add_widget(title_row)
                self.channels_container.add_widget(group)

                groups[channel.group.name] = group

            channel_name_row = ChannelsListButton(text=channel.name,
                                                  on_press=lambda a, _id=channel.identifier:
                                                  self.landing_screen.display_conversation(_id))
            groups[group_name].add_widget(channel_name_row)

    def add_new_channel(self, group_name):
        content = RelativeLayout()

        content.add_widget(Label(text="Le nom du nouveau channel et d'autres éléments"))
        content.add_widget(
            Button(text="Ajouter", size_hint=(None, None), size=(150, 40), pos_hint={'center_x': .4, 'center_y': .1}))
        cancel = Button(text="Annuler", size_hint=(None, None), size=(150, 40), pos_hint={'center_x': .6, 'center_y': .1})
        content.add_widget(cancel)

        popup = Popup(title="Ajouter un nouveau channel à {0}".format(group_name),
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5},
                      content=content,
                      auto_dismiss=False)

        cancel.bind(on_press=lambda a: popup.dismiss())

        popup.open()


class MessageLabel(Label):
    pass


class MessageSent(MessageLabel):
    pass


class MessageReceived(MessageLabel):
    pass


class ConversationContainer(ScrollView):

    def __init__(self, channel_id):
        super(ConversationContainer, self).__init__()
        self.channel_id = channel_id
        self.messages_box = self.ids.messages_container

        # Démarrer la mise à jour régulière de la conversation
        self.constant_update()

    def constant_update(self):
        self.init_conversation()
        # time.sleep(1)

    def init_conversation(self):
        conv_file_path = config.PUBLIC_DIR + "/tmp_conversations/basic.json"
        with open(conv_file_path) as json_file:
            conv = json.load(json_file)

        for message in conv["data"]:
            msg = MessageSent(text=message["timestamp"] + " - " + message["sender"] + "\n" + message["msg"])
            self.messages_box.add_widget(msg, len(self.messages_box.children))

    def add_message(self, msg_obj, pos="left"):
        msg = MessageSent()

        if pos == "right":
            msg = MessageReceived()

        msg.text = str(msg_obj.timestamp) + " - " + msg_obj.sender + "\n" + msg_obj.msg
        self.messages_box.add_widget(msg, len(self.messages_box.children))


class InputsContainer(BoxLayout):
    pass
