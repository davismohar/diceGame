import pyglet
from pyglet.window import key
import random
from pyglet.gl import *

#TODO add mouseclick in range of triangle

#declaring global variables
sprite1 = None
sprite2 = None

window = pyglet.window.Window()
#sets vertex list for triangles
vlist = pyglet.graphics.vertex_list(3, ('v2f', [500,100, 550,100, 525,150]))
#set background color
pyglet.gl.glClearColor(255, 255, 255, 255)
#loads array of images
images = [
    pyglet.image.load("dice1.png"),
    pyglet.image.load("dice2.png"),
    pyglet.image.load("dice3.png"),
    pyglet.image.load("dice4.png"),
    pyglet.image.load("dice5.png"),
    pyglet.image.load("dice6.png"),
]

def diceRoll():
    global sprite1
    global sprite2
    roll1 = random.randint(0,5)
    roll2 = random.randint(0,5)
    #loads the sprite by accessing the random number in the array
    sprite1 = pyglet.sprite.Sprite(images[roll1])
    sprite2 = pyglet.sprite.Sprite(images[roll2],x = 125,y = 0)

@window.event
def on_draw():
    window.clear
    sprite1.draw()
    sprite2.draw()
    glColor3f(1,0,0)
    vlist.draw(GL_TRIANGLES)

def on_window_close(window):
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        diceRoll()


def main():
    diceRoll()
    pyglet.app.run()



main()
