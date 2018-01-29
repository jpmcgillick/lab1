#!/usr/bin/python

import serial
import pygame, sys
from pygame.locals import *

s = serial.Serial("/dev/ttyACM0")
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('RGB Test')

while(True):
   l = s.readline()
   x = l.rstrip().split(",")
   rgb = [int(val) for val in x]
   print x
   #pygame.Color(rgb)
   pygame.display.update()
