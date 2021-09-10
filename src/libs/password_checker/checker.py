#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    Ce fichier contient les fonctions permettant de vérifier si un mot de passe réponds aux différents critères
        de sécurité.
    ----- CODE A IMPLEMENTER -----
"""


def complete_check(password):
    """
        [BASE]
        Teste le mot de passe grâce à l'ensemble des critères de validation.
        :param password: Le mot de passe a analyser.
        :return: dict : Un dictionnaire contenant le 'status' de l'exécution et la liste des erreurs si nécessaire.
                        status = 1 si le mot de passe a passé tous les critères.
                        status = 0 si un critère n'est pas validé.
                        errors = {}, une liste de dictionnaires d'erreurs avec le critère 'type' et le message 'msg'.

    """
    pass


def check_length(password):
    """
        [BASE]
        Vérifier le nombre de caractères présents dans le mot de passe.
        :param password: Le mot de passe a analyser.
        :return: un dictionnaire contenant le type de critère 'type' et d'éventuelles erreurs 'error'.
    """
    response = {
        "type": "length",
        "error": None
    }
    error_msg = "Le mot de passe est trop court"
    result = len(password) >= 8

    if not result:
        response["error"] = error_msg
        return response

    return response


def check_special_characters(password):
    pass


def check_uppercase(password):
    pass


if __name__ == "__main__":
    res = check_length("Pis Pan Douille")
    print(res)
