#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier contient la classe Help contenant l'ensemble des directives pour l'aide utilisateur.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""
from kivy.uix.screenmanager import Screen


class Help(Screen):

    def __init__(self):
        super(Help, self).__init__()
        self.name = 'help'
