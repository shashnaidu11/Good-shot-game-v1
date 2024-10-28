#importing the libraries
import random
import pgzrun

TITLE="good shot game"
WIDTH=500
HEIGHT=500

msg=""

#Creating the charector
alien=Actor("alien")

def draw():
    screen.clear()
    screen.fill(color=("Red"))
    alien.draw()
    screen.draw.text(msg,center=(300,20),fontsize=30)













pgzrun.go()