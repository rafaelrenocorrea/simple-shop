from core.settings.model import Model
from core.settings.view import View

class Controller:
    def __init__(self, root):
        self.__model = Model()
        self.__view = View(self, root)

    # atualiza definições de conta do banco de dados
    def update_acc(self, acc_name, acc_psswd):
        self.__model.update_acc(acc_name, acc_psswd)
    #