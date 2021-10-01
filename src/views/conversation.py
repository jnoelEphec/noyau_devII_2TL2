#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier représente une zone de conversation.
"""

from datetime import datetime

from kivy.uix.relativelayout import RelativeLayout

from src.libs.bot.commands import Commands
from src.models.message import Message
from src.views.widgets import ConversationContainer, InputsContainer


class Conversation(RelativeLayout):
    def __init__(self, channel_id):
        super(Conversation, self).__init__()
        self.messages_container = ConversationContainer(channel_id)
        self.inputs_container = InputsContainer()

        self.add_widget(self.messages_container)
        self.add_widget(self.inputs_container)

    def send_message(self):
        txt = self.inputs_container.ids.message_input.text

        if txt:
            msg = Message(datetime.now(), txt, "Moi")
            self.messages_container.add_message(msg)
            msg.send_to_db()

            if txt[0] == "/":
                bot = Commands(txt)
                response_from_bot = bot.result
                msg_res = Message(datetime.now(), response_from_bot, "E-Bot")
                self.messages_container.add_message(msg_res, pos="right")

            self.inputs_container.ids.message_input.text = ""

