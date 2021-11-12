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
    Language utilisé pour coder : Anglais
    Language utilisé pour documenter : Français
    Documentation Framework : https://kivy.org/doc/stable/api-kivy.html
    Source unique des icons : https://remixicon.com/

    Convention de nommage :
        https://www.python.org/dev/peps/pep-0008/

"""

from kivy.app import App
from kivy.lang import Builder
from pymongo import MongoClient

import src.config.config as config
import pymongo as pymongo
import os

from src.models.mongo_connector import MongoConnector
from src.models.screens_manager import ScreensManager
from dotenv import load_dotenv

load_dotenv()

Builder.load_file("{0}/common.kv".format(config.VIEWS_DIR))


class Main(App):
    title = 'EpheCom'

    def build(self):
        from src.views.landing import LandingScreen

        sm = ScreensManager()
        landing_screen = LandingScreen()
        sm.add_widget(landing_screen)
        sm.current = "landing"
        landing_screen.set_teams_list()
        return sm


class Personne:
    def __init__(self, nom):
        self.nom = nom
        
        
class Etudiant(Personne):
    def __init__(self, nom):
        super(Etudiant, self).__init__(nom)


if __name__ == '__main__':
    print("Bienvenue sur notre projet commun !")

    Main().run()
