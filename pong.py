import tkinter 
from tkinter import *
import time
import random


#Classe de la balle
class Ball:
    def __init__(self, canvas, color):
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.canvas = canvas
        self.id = canvas.create_oval(30, 30, 55, 55, fill = color)
        self.canvas.move(self.id, 540, 300)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    #Mouvement
    def spawn(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.y = -3
        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:
            self.x = -3

#Classe dess joueurs
class raquettes:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(200, 200, 50, 50, fill = color)
        self.canvas.move(self.id 300, 200)


#Support du jeu
tk = Tk()
tk.title("Pong")
canvas = Canvas(tk, width = 1080, height = 720, bd = 0, bg = "White")
canvas.pack()
tk.update()
ball = Ball(canvas, "Red")


while 1:
    ball.spawn()
    tk.update()
    time.sleep(0.01)