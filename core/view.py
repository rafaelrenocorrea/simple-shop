import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

class View:
    def __init__(self, controller):
        self.__controller = controller

        # faz a janela
        self.root = tk.Tk()
        #

        # configura a janela
        self.root.title('$imple $hop')
        self.root.minsize(400, 300)
        self.root.resizable(False, False)
        self.centrazile()
        #

        # menu
        self.__menu = tk.Menu(self.root)
        
        self.__app_menu = tk.Menu(self.__menu, tearoff = 0)
        self.__app_menu.add_command(label = 'Preferências', command = self.open_settings)
        self.__app_menu.add_command(label = 'Créditos', command = self.show_credits)
        self.__app_menu.add_separator()
        self.__app_menu.add_command(label = 'Sair', command = self.safe_exit)

        self.__menu.add_cascade(menu = self.__app_menu, label = 'App')

        self.root.configure(menu = self.__menu)
        #

        # inicia a janela
        self.root.mainloop()
        #
    
    # faz a janela aparecer no meio da tela
    def centrazile(self):
        x = int((self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2) # média da largura da tela com a largura da janela
        y = int((self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2) # média da altura da tela com a altura da janela

        self.root.geometry(f'+{x}+{y}')
    #

    # rotina de encerramento do programa
    def safe_exit(self):
        if messagebox.askyesno(title = 'Confirmação', message = 'Deseja encerrar o programa?', icon = 'warning'):
            self.__controller.safe_exit()

            self.root.destroy()
    #

    # inicia a janela de preferências
    def open_settings(self):
        self.__controller.open_settings(self.root)
    #

    # mostra a janela de créditos
    def show_credits(self):
        root = tk.Toplevel(self.root)

        root.title("Créditos")
        #root.minsize(200, 150)
        root.resizable(False, False)

        top = tk.Frame(root)
        bot = tk.Frame(root)

        # mantém uma referência da imagem na instância
        # (impede que o garbage collector do Python a remova)
        self.__img = tk.PhotoImage(file = 'assets/yumiowari.png')
        label_img = tk.Label(top, image = self.__img)
        #

        by = 'Todos os direitos reservados\n'   \
             ' © 2024 Rafael Renó Corrêa. \n\n' \
             'Github: '
        text_by = tk.Text(top, wrap = 'word', height = 4, width = 28)
        text_by.insert('1.0', by)

        # configura o link para o github
        text_by.insert('end', 'github.com/yumiowari', 'link')

        text_by.tag_configure('link', foreground = 'blue', underline = True)
        text_by.tag_bind('link', '<Button-1>', lambda e: self.open_link('https://github.com/yumiowari'))
        
        text_by.configure(state = 'disabled') # desativa a edição
        #

        # altera o cursor quando o mouse passa sobre a área do link
        text_by.bind('<Enter>', lambda e: text_by.config(cursor='heart'))
        text_by.bind('<Leave>', lambda e: text_by.config(cursor=''))
        #
        
        label_img.pack()
        text_by.pack()

        ok_btn = tk.Button(bot, text = 'OK', command = root.destroy)
        ok_btn.pack()

        top.pack(side = tk.TOP)
        bot.pack(side = tk.BOTTOM)
    #

    # função para abrir link do navegador
    def open_link(self, url):
        webbrowser.open_new(url)
    #