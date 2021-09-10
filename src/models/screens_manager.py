#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier représente la classe permettant la navigation entre différentes interfaces.
"""

from kivy.uix.screenmanager import ScreenManager, NoTransition, ScreenManagerException


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class ScreensManager(ScreenManager):
    """
        Cette classe est utilisée afin de naviguer entre différentes fenêtres du programme.
        Sachant que cette classe est un "Singleton", elle ne sera instanciée qu'une seule fois
        lors de la première instanciation.
    """

    def __init__(self):
        super(ScreenManager, self).__init__()
        self.transition = NoTransition()

    def instanciate_screen(self, href):
        """
            Permet d'instancier une interface si elle ne l'est pas encore.
            :param href: Le nom de l'interface concernée.
            :return:
        """
        obj_screen = None

        if href == "login":
            from src.views.login import Login
            obj_screen = Login()
        elif href == "subscribe":
            from src.views.subscribe import Subscribe
            obj_screen = Subscribe()
        elif href == "profile":
            from src.views.profile import Profile
            obj_screen = Profile()
        elif href == "help":
            from src.views.help import Help
            obj_screen = Help()

        return obj_screen

    def redirect(self, href):
        """
            Redirige vers l'interface concernée si elle existe.
            Sinon, créée une instance et redirige vers celle-ci.
            :param href: le nom de l'interface concernée.
        """
        try:
            res = self.get_screen(href)
            self.current = href
        except ScreenManagerException:
            obj_screen = self.instanciate_screen(href)

            if obj_screen is None:
                return False

            self.add_widget(obj_screen)
            self.current = href
