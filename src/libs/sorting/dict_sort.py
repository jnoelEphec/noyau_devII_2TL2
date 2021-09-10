#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    Ce fichier contient les fonctions permettant de trier une liste, un dictionnaire et d'autres.
    ----- CODE A IMPLEMENTER -----
"""


def dict_sort(data, key, order="ASC"):
    """
        Trie un dictionnaire en fonction d'une clé et un ordre.

        :param data: Le dictionnaire a trier.
        :param key: La clé sur laquelle le tri doit s'effectuer.
        :param order: Ordre du tri, croissant = ASC et décroissant = DESC.
        :return: dict : Le dictionnaire - data - trié selon la clé et l'ordre définis.
    """

    if order == "DESC":
        sort = [(key, value) for (key, value) in sorted(data.items(), key=lambda x: x[1][key], reverse=True)]
    else:
        sort = [(key, value) for (key, value) in sorted(data.items(), key=lambda x: x[1][key])]

    return dict(sort)
