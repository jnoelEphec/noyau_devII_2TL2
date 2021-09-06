#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Projet EpheCom
    ===================================

    Ce logiciel a été développé dans le cadre scolaire.
    EpheCom est un logiciel de communications - vocale et écrite - en temps réel.
    Il a pour but d'améliorer la communication au sein de l'établissement scolaire.

    Version de Python : 3.9
    Système d'exploitation : Windows, OSX, Linux
    Type : Application de bureau
    Langue utilisé pour coder : Anglais
    Documentation Framework : https://kivy.org/doc/stable/api-kivy.html
    Source unique des icons : https://remixicon.com/

    Convention de nommage :
        https://www.python.org/dev/peps/pep-0008/

"""
from kivy.app import App
from kivy.lang import Builder

import src.config.config as config
from src.models.screens_manager import ScreensManager

Builder.load_file("{0}/common.kv".format(config.VIEWS_DIR))


class Main(App):
    title = 'EpheCom'

    def build(self):
        from src.views.landing import LandingScreen

        sm = ScreensManager()
        landing_screen = LandingScreen()
        sm.add_widget(landing_screen)
        sm.current = "landing"
        landing_screen.set_channels_list()
        return sm


if __name__ == '__main__':
    print("Bienvenue sur notre projet commun !")
    Main().run()
