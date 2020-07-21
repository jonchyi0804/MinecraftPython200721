# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:12:41 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

username = input("請輸入名字:")
while True:
    message = input("輸入訊息:")

    mc.postToChat("["+username+"]"+message)