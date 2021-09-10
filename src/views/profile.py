#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier contient la classe Profile contenant l'ensemble du profil de l'utilisateur.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""
from kivy.uix.screenmanager import Screen


class Profile(Screen):

    def __init__(self):
        super(Profile, self).__init__()
        self.name = 'profile'
