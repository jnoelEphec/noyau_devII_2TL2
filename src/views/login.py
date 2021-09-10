#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier contient la classe Login permettant la gestion de la connexion utilisateur.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""
from kivy.uix.screenmanager import Screen


class Login(Screen):

    def __init__(self):
        super(Login, self).__init__()
        self.name = 'login'
