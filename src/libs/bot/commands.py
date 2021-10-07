import sys
from inspect import getmembers, isfunction


class Commands:
    def __init__(self, command):
        self.command = command[1:]

        try:
            self.result = getattr(sys.modules[__name__], "%s" % self.command)()
        except Exception as e:
            self.result = "Cette commande n'existe pas !"


def hello():
    """
        /hello
        Dis 'Hello' à l'utilisateur.
        :return: string : Une simple texte 'Hello'
    """
    return "Hello !!"


def help():
    """
        /help
        Cette commande permet d'afficher les différentes commandes utilisables.
        :return: string : Les commandes ainsi que leurs documentations.
    """
    txt = "Je suis l'aide, voici ce que je peux faire !"

    commands = display_all_ask_names()

    for command in commands:
        if command is not None:
            txt += "\n==========================================================================\n"
            txt += "==========================================================================\n"
            txt += command

    return txt


def display_all_ask_names():
    """
        Retourne l'ensemble des commandes que le bot accepte.
        :return: list : la liste des commandes documentées par leurs docstring.
    """
    forbidden_names = ["isfunction", "getmembers"]

    current_module = sys.modules[__name__]

    modules_list = getmembers(current_module, isfunction)

    modules_list = [obj.__doc__ for name, obj in modules_list if name not in forbidden_names]

    return modules_list


if __name__ == "__main__":
    while True:
        cmd = input("Entrez une commande :")

        if cmd == "q":
            break

        cmd_obj = Commands(cmd)
        print(cmd_obj.result)

