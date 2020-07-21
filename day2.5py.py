# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:55:02 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    
    r = mc.getBlock(x+1,y-1,z)
    l = mc.getBlock(x-1,y-1,z)
    f = mc.getBlock(x,y-1,z+1)
    b = mc.getBlock(x,y-1,z+1)
    
    if r == 9 or l == 9 or f == 9 or b == 9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,79)