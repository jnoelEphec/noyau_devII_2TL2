#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient une classe représentant une équipe.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""


class Team:
    def __init__(self, identifier, name, channels, icon_path=None, participants=None):
        self.identifier = identifier
        self.name = name
        self.channels = channels
        self.icon_path = icon_path
        self.participants = participants

    def join(self):
        """
            Méthode permettant à un utilisateur de rejoindre cette équipe.
        """
        pass

    def leave(self):
        """
            Méthode permettant à un utilisateur de quitter cette équipe.
        """
        pass

    def get_participants_status(self):
        pass
