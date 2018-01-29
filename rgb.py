#!/usr/bin/python

import serial
import pygame, sys
from pygame.locals import *

s = serial.Serial("/dev/ttyACM0")
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('RGB Switcher')

while(True):
   l = s.readline()
   x = l.rstrip().split(",")
   try:
     rgb = [int(val) for val in x]
   except ValueError:
      pass
   print x
   try:
     DISPLAYSURF.fill((rgb[0],rgb[1],rgb[2]))
     pygame.display.update()
   except IndexError:
      pass
