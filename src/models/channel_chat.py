#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient une classe représentant un channel de conversation écrite entre deux membres.
"""
from src.models.channel import Channel


class ChannelChat(Channel):
    def __init__(self, name):
        super().__init__(name)
