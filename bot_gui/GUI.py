import tkinter as tk
from support_classes import *
import tkinter.messagebox as messagebox
import json
import os

#This class initialize the tkinter app
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Initializing thing we need, config file, the StringVar variable for entrys, and the widgets function
        self.title = ("RaidenBot GUI")

        self.db = DB_pymysql()
        self.cursor = self.db.cur()
        self.path_file = os.path.join(r"C:\Users\wearethewarriors\Downloads\Proyectos_personales\Bot de curiosidades\discord music bot\cogs", "config.json")
        self.file = open(self.path_file, "r")
        self.config = json.load(self.file)

        #Button for close the app
        self.CloseLabel = tk.Button(self, text="Salir", command=self.CloseApp)
        self.CloseLabel.pack(fill="both")

        self.music = tk.StringVar(self)
        self.curiosidad = tk.StringVar(self)
        self.chistedare = tk.StringVar(self)
        self.meme = tk.StringVar(self)
        self.mascot = tk.StringVar(self)

        self.init_Widgets()

    #Function for close the app
    def CloseApp(self):
        self.destroy()

    #Function that adds the curiosity of the entry label in database and sum +1 to curiositys numbers for choosing
    def add_curiosity(self):
        curiosidad = self.curiosidad.get()
        try:
            self.cursor.execute("insert into curiositys (curiosity) value ('{}')".format(curiosidad))
            self.db.comm()
            self.config["values_choose"]["curiosidades"]["max"] += 1
            with open(self.path_file, "w") as file:
                json.dump(self.config, file)
            
        except Exception as e:
            messagebox.showinfo("Error al añadir curiosidad", e)
        messagebox.showinfo("Añadida", "¡Curiosidad añadida correctamente!")

    #Function that adds the joke of the entry label in database and sum +1 to jokes numbers for choosing
    def add_chiste(self):
        chiste = self.chistedare.get()
        try:
            self.cursor.execute("insert into chistesnegros (chiste) values ('{}')".format(chiste))
            self.db.comm()
            self.config["values_choose"]["chistes"]["max"] += 1
            with open(self.path_file, "w") as file:
                json.dump(self.config, file)

        except Exception as e:
            messagebox.showinfo("Error al añadir chiste", e)
        messagebox.showinfo("Añadido", "¡Chiste añadido correctamente!")

    #Function that adds the meme path of the entry label in database and sum +1 to memes numbers for choosing
    def add_meme(self):
        meme = self.meme.get()
        try:
            self.cursor.execute("insert into memepaths (memepath) value ('{}')".format(meme))
            self.db.comm()
            self.config["values_choose"]["memes"]["max"] += 1
            with open(self.path_file, "w") as file:
                json.dump(self.config, file)

        except Exception as e:
            messagebox.showinfo("Error al añadir meme", e)
        messagebox.showinfo("Añadido", "¡Meme añadido correctamente!")

    #Function that adds the music path of the entry label in database and sum +1 to music numbers for choosing
    def add_music(self):
        music = self.music.get()
        try:
            self.cursor.execute("insert into musicpaths (musicpath) value ('{}')".format(music))
            self.db.comm()
            self.config["values_choose"]["musica"]["max"] += 1
            with open(self.path_file, "w") as file:
                json.dump(self.config, file)

        except Exception as e:
            messagebox.showinfo("Error al añadir musica", e)
        messagebox.showinfo("Añadida", "¡Musica añadida correctamente!")

    #Function that adds the mascot of the entry label in database 
    def add_mascot(self):
        mascot = self.mascot.get()
        try:
            self.cursor.execute("insert into mascotasDisponibles (mascota) value ('{}')".format(mascot))
            self.db.comm()

        except Exception as e:
            messagebox.showinfo("Error al añadir mascota", e)
        messagebox.showinfo("Añadida", "¡Mascota añadida correctamente!")
    
    #Function for widgets, all widgets are in diferent frames
    def init_Widgets(self):

        #Creates the add_curiositys widget!
        add_curiositys = tk.Frame(self)
        add_curiositys.configure(background="black")
        add_curiositys.pack(side=tk.LEFT, fill=tk.Y, expand=True, pady=22)

        tk.Label(
            add_curiositys,
            text="Añade una curiosidad!",
            justify=tk.CENTER,
        ).pack(
            side=tk.TOP,
            fill=tk.Y,
            padx=22,
            pady=22
        )

        tk.Entry(
            add_curiositys,
            textvariable=self.curiosidad,
            selectborderwidth=3,
            highlightcolor="#FFFFFF",
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=22
        )

        tk.Button(
            add_curiositys,
            command=self.add_curiosity,
            text="Añadir!",
            highlightcolor="#FFFFFF",
            justify=tk.CENTER
        ).pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=22,
            pady=22
        )

        #Creates the add_chistes widget!
        add_chistes = tk.Frame(self)
        add_chistes.configure(background="black")
        add_chistes.pack(side=tk.LEFT, fill=tk.Y, expand=True, pady=22)

        tk.Label(
            add_chistes,
            text="Añade un chiste!",
            justify=tk.CENTER,
        ).pack(
            side=tk.TOP,
            fill=tk.Y,
            padx=22,
            pady=22
        )

        tk.Entry(
            add_chistes,
            textvariable=self.chistedare,
            selectborderwidth=3,
            highlightcolor="#FFFFFF",
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=22
        )

        tk.Button(
            add_chistes,
            command=self.add_chiste,
            text="Añadir!",
            highlightcolor="#FFFFFF",
            justify=tk.CENTER
        ).pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=22,
            pady=22
        )

        #Make the add_music widget!
        add_music = tk.Frame(self)
        add_music.configure(background="black")
        add_music.pack(side=tk.LEFT, fill=tk.Y, expand=True, pady=22)

        tk.Label(
            add_music,
            text="Añade una cancion!",
            justify=tk.CENTER,
        ).pack(
            side=tk.TOP,
            fill=tk.Y,
            padx=22,
            pady=22
        )

        tk.Entry(
            add_music,
            textvariable=self.music,
            selectborderwidth=3,
            highlightcolor="#FFFFFF",
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=22
        )

        tk.Button(
            add_music,
            command=self.music,
            text="Añadir!",
            highlightcolor="#FFFFFF",
            justify=tk.CENTER
        ).pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=22,
            pady=22
        )

        #Creates the add_memes widget!
        add_memes = tk.Frame(self)
        add_memes.configure(background="dark slate gray")
        add_memes.pack(side=tk.LEFT, fill=tk.Y, expand=True, pady=22)

        tk.Label(
            add_memes,
            text="Añade un meme!",
            justify=tk.CENTER,
        ).pack(
            side=tk.TOP,
            fill=tk.Y,
            padx=22,
            pady=22
        )

        tk.Entry(
            add_memes,
            textvariable=self.music,
            selectborderwidth=3,
            highlightcolor="#FFFFFF",
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=22
        )

        tk.Button(
            add_memes,
            command=self.add_meme,
            text="Añadir!",
            highlightcolor="#FFFFFF",
            justify=tk.CENTER
        ).pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=22,
            pady=22
        )

        #Creates the add_mascots widget!
        add_mascots = tk.Frame(self)
        add_mascots.configure(background="dark slate gray")
        add_mascots.pack(side=tk.LEFT, fill=tk.Y, expand=True, pady=22)

        tk.Label(
            add_mascots,
            text="Añade una mascota!",
            justify=tk.CENTER,
        ).pack(
            side=tk.TOP,
            fill=tk.Y,
            padx=22,
            pady=22
        )

        tk.Entry(
            add_mascots,
            textvariable=self.mascot,
            selectborderwidth=3,
            highlightcolor="#FFFFFF",
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=22
        )

        tk.Button(
            add_mascots,
            command=self.add_mascot,
            text="Añadir!",
            highlightcolor="#FFFFFF",
            justify=tk.CENTER
        ).pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=22,
            pady=22
        )