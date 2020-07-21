# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:09:26 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time

while True:
    x,y,z=mc.player.getTilePos()
    color = random.randrange(0,16)
    mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,95,color)
    time.sleep(0)