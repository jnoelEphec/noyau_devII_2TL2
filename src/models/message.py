#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient une classe représentant un message textuel envoyé dans un channel.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""
import json

from src.config import config


class Message:
    def __init__(self, timestamp, msg, sender):
        self.timestamp = timestamp
        self.msg = msg
        self.sender = sender

    def db_formatting(self):
        return {
            "timestamp": str(self.timestamp),
            "msg": self.msg,
            "sender": self.sender
        }

    def send_to_db(self):
        conv_file_path = config.PUBLIC_DIR + "/tmp_conversations/basic.json"
        with open(conv_file_path) as json_file:
            conv = json.load(json_file)

        conv["data"].append(self.db_formatting())

        with open(conv_file_path, 'w') as outfile:
            json.dump(conv, outfile)
