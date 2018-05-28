#!/usr/bin/python3

# -*- coding: utf-8 -*-

import os
import tkinter as tk 

content = ""

def mapValue(val,x1,y1,x2,y2):
	z = x1/x2
	w = y1/y2
	return val * z/w

def reverseString(string):
	return string[::-1]

def writeHash(keyhash):
	file = open("DB.txt", "a")
	file.write(keyhash)
	file.close()

def readHash():
	file = open("DB.txt", "r")
	keyhash = file.read()
	file.close()
	return keyhash

def delHash():
	if (os.path.isfile("./DB.txt")):
		os.remove("./DB.txt")
	open("./DB.txt", 'a')

def isHashSet():
	if(readHash() == ""):
		return False
	else:
		return True

def keyGen(string):
	key=""
	val=ord(string[0])^ord(string[-1]) 
	while len(key)<256:
		for k in string:
			char = ord(k)^val
			val = mapValue(ord(k),1,126,1,9)
			val = int(val * char / 2)
			key = key + str(val)
	if(len(key)>256):
		key = key[:256]		
	return key

def hashProcess(string):
	key = int(keyGen(string))
	reverseKey = int(keyGen(reverseString(string)))
	rotg = key<<len(string)
	rotd = reverseKey>>len(string)
	merge = str(rotg)+str(rotd)
	if(len(merge)>256):
		merge = merge[:256]
	return merge

def compare(string, keyhash):
	toComp = hash(string)
	if(toComp == keyhash):
		return True
	else:
		return False	

def showDB():
	content = readHash()
	labelDB.configure(text='content')		

def process():
	if isHashSet():
		keyhash = readHash()
		if compare(inText.get(), keyhash):
			labelStatus.configure(text='Password is good', fg="green")
		else:
			labelStatus.configure(text='Password is incorrect !', fg="red")
	else:
		keyhash = inText.get()
		if not keyhash == "":
			writeHash(keyhash)
			labelStatus.configure(text='Password has been set !', fg="green")
		else:
			labelStatus.configure(text='Text is empty, please try to re-enter you password', fg="red")

window = tk.Tk()
window.title("Hash Maison")
window.geometry("300x500")

labelInfo = tk.Label(window, text="Please enter your password below").pack()

inText = tk.Entry(window, show="*").pack()

buttonValid = tk.Button(window, text="Validate", command=process).pack()

labelStatus = tk.Label(window, text="Hash Not Set ! Please start typing your password", fg="red").pack()

buttonDB = tk.Button(window, text="Show DB", command=showDB).pack()

buttonDel = tk.Button(window, text="Delete Hash", command=delHash).pack()

buttonQuit = tk.Button(window, text="Quitter l'application", command=window.quit).pack()

labelDB = tk.Label(window, text=content).pack()

window.mainloop()