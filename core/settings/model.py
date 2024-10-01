import pickle as pkl
import os

class Model:
    def __init__(self):
        self.__acc = {
            'name': '',
            'psswd': ''
        }

    def update_acc(self, acc_name, acc_psswd):
        self.__acc['name'] = acc_name
        self.__acc['psswd'] = acc_psswd

        if not os.path.exists('data'):
            os.makedirs('data')

        with open('data/acc.pkl', 'wb') as f:
            pkl.dump(self.__acc, f)