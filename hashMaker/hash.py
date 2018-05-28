#!/usr/bin/python3

# -*- coding: utf-8 -*-

from random import *

str = input("sentence to hash : ")

def mapValue(val,x1,y1,x2,y2):
	z = x1/x2
	w = y1/y2
	return val * z/w


def keyGen(str):
	key=""
	for i in range(256):
		char = randint(1,9)
		moy=0
		for k in str:
			moy = moy + ord(k)
		moy = moy / len(str)
		char = int(mapValue(char,1,9,21,moy))
		key = key + chr(char)
	return key	


def algo(str,clé):
	pass

def hash(str,algo):
	pass


print(keyGen(str))