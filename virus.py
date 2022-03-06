from asyncio.tasks import _enter_task
from time import sleep
from tkinter import CENTER
from turtle import *   

def virus():
    speed(20)
    color('green')
    bgcolor('black')
    b=200
    while(b>0):
        left(b)
        forward(b*3)
        b=b - 1
    done()

virus()