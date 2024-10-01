import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    def __init__(self, controller, root):
        self.__controller = controller

        self.root = tk.Toplevel(root)

        # configura a janela
        self.root.title('Preferências')
        self.root.minsize(400, 300)
        self.root.resizable(False, False)
        #

        ## notebook
        self.__notebook = ttk.Notebook(self.root)

        self.__set_acc = ttk.Frame(self.__notebook) # primeira página

        # definições de conta
        self.acc_name = tk.StringVar(value = '')
        self.acc_name.trace_add('write', self.verify_acc_name)
        self.__acc_name_entry = tk.Entry(self.__set_acc, textvariable = self.acc_name)
        self.__acc_name_label = tk.Label(self.__set_acc, text = 'Nome de usuário')

        self.acc_psswd = tk.StringVar(value = '')
        self.acc_psswd.trace_add('write', self.verify_acc_psswd)
        self.__acc_psswd_entry = tk.Entry(self.__set_acc, textvariable = self.acc_psswd)
        self.__acc_psswd_label = tk.Label(self.__set_acc, text = 'Senha')

        self.__confirm_btn = tk.Button(self.__set_acc, text = 'Confirmar', command = self.update_acc)

        self.__acc_name_label.pack()
        self.__acc_name_entry.pack()
        self.__acc_psswd_label.pack()
        self.__acc_psswd_entry.pack()

        self.__confirm_btn.pack()
        #

        self.__notebook.add(self.__set_acc, text = 'Conta')

        self.__notebook.pack()
        ##

    # self.acc_name observer
    def verify_acc_name(self, var, index, mode):
        aux = self.acc_name.get()

        if len(aux) > 15:
            aux = aux[:15]

        self.acc_name.set(aux)
    #

    # self.acc_psswd observer
    def verify_acc_psswd(self, var, index, mode):
        aux = self.acc_psswd.get()

        if len(aux) > 15:
            aux = aux[:15]

        self.acc_psswd.set(aux)
    #

    def update_acc(self):
        acc_name = self.acc_name.get()
        acc_psswd = self.acc_psswd.get()

        if messagebox.askyesno(title = 'Confirmação', message = 'Deseja atualizar os dados de login no banco de dados?', icon = 'warning'):
            if acc_name == '' and acc_psswd != '':
                messagebox.showerror('Falha', 'Um nome de usuário precisa ser informado.')
            elif acc_psswd == '' and acc_name != '':
                messagebox.showerror('Falha', 'Uma senha precisa ser informada.')
            elif acc_name == '' and acc_psswd == '':
                messagebox.showerror('Falha', 'As credenciais de login precisam ser informadas.')
            else:
                self.__controller.update_acc(acc_name, acc_psswd)

                messagebox.showinfo('Sucesso', 'As credenciais de login foram atualizadas.')