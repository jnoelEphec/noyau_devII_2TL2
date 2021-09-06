#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient toutes les variables communes au projet
"""

# Couleurs
import os
import sys

MAIN_COLOR = (0.580, 0.533, 0.984)
R, G, B, = MAIN_COLOR
BG_COLOR_LEVEL_1 = (R, G, B, 1)
TEXT_COLOR = (1, 1, 1, 1)

# Chemins
ROOT_DIR = sys.path[1]
PUBLIC_DIR = os.path.join(ROOT_DIR, 'public')
IMG_DIR = os.path.join(PUBLIC_DIR, 'images')
VIEWS_DIR = os.path.join(PUBLIC_DIR, 'views')