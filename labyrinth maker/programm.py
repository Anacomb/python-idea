#!/usr/bin/python3

# -*- coding: utf-8 -*-


from tkinter import * 
#from numpy import *
from random import *

resolution = 25

def recupere():
	drawGrid(resolution)

def drawGrid(x):
	canvas = Canvas(window,width="450",height="450", background='white')
	x = int(x)
	for i in range(x):
		for j in range(x):
			canvas.create_rectangle(25+j*400/x, 25+i*400/x, 25+400/x+j*400/x, 25+400/x+i*400/x)

	# for i in range(x*2):
	# 	for j in range(x*2):
	# 		if(rand()>0.7):
	# 			canvas.create_line(25+j*400/x, 25+i*400/x, )
			
	canvas.pack()			

def updateLabelX(x):
	global resolution
	resolution=x
	labelX.configure(text='La taille du labyrinthe est de: ' + x + 'x' + x)


window = Tk()
window.title("Laby Construct")
window.geometry("700x600")

drawGrid(resolution)


labSize = Scale(window, length=250, orient=HORIZONTAL, label='Taille du labyrinthe entre 10 et 50: ', troughcolor='dark grey', sliderlength=20, showvalue=25, from_=10, to=50, tickinterval=5, command=updateLabelX).pack()

labelX = Label(window)
labX=labelX.pack()

button = Button(window, text="Valider", command=recupere)
button.pack()

window.mainloop()