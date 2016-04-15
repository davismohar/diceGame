import pyglet
from pyglet.window import key
import random
from pyglet.gl import *
import csv


#declaring global variables
window = pyglet.window.Window()
#dice 1 and dice 2
dice1 = None
dice2 = None
dice2Roll = 0
dice1Roll = 0
guessValue = 6
winConditon = False

#Loads money array from bank.csv, and saves it as playerMoney array
playerMoney = []
def loadMoney():
    with open("bank.csv", "rb") as bank:
        bankReader = csv.reader(bank)
        for row in bankReader:
            playerMoney = row
        print playerMoney

#The text of the guessValue
guessValueLabel = pyglet.text.Label(str(guessValue), x=525, y=75,
                                                    anchor_x='center',
                                                    anchor_y='center',
                                                    color = (0,0,0,255))
guessValueLabelLabel = pyglet.text.Label("Guess: ", x = 490, y = 75,
                                                    anchor_x='center',
                                                    anchor_y='center',
                                                    color = (0,0,0,255))
#sets vertex list for triangles
vlist1 = pyglet.graphics.vertex_list(3, ('v2f', [500,100, 550,100, 525,150]))
vlist2 = pyglet.graphics.vertex_list(3, ('v2f', [500,50, 550,50, 525,0]))
#set background color
pyglet.gl.glClearColor(255,255,255,255)
#loads array of images
images = [
    pyglet.image.load("dice1.png"),
    pyglet.image.load("dice2.png"),
    pyglet.image.load("dice3.png"),
    pyglet.image.load("dice4.png"),
    pyglet.image.load("dice5.png"),
    pyglet.image.load("dice6.png"),
]
winLabel = pyglet.text.Label("You Win!",
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=(window.height//2)+100,
                          anchor_x='center', anchor_y='center',
                          color=(0,0,0,255))

def diceRoll():
    global dice1
    global dice2
    global dice1Roll
    global dice2Roll
    global winConditon
    roll1 = random.randint(0,5)
    roll2 = random.randint(0,5)
    #loads the sprite by accessing the random number in the array
    dice1 = pyglet.sprite.Sprite(images[roll1])
    dice1Roll = roll1 + 1
    dice2 = pyglet.sprite.Sprite(images[roll2],x = 125,y = 0)
    dice2Roll = roll2 + 1
    if guessValue == (dice1Roll + dice2Roll):
        winConditon = True
    else:
        winConditon = False


@window.event
def on_draw():
    window.clear()
    dice1.draw()
    dice2.draw()
    glColor3f(1,0,0)
    vlist1.draw(GL_TRIANGLES)
    vlist2.draw(GL_TRIANGLES)
    guessValueLabel.draw()
    guessValueLabelLabel.draw()
    print (str(guessValue) + " " + str(dice1Roll+dice2Roll))
    if winConditon is True:
        winLabel.draw()



def on_window_close(window):
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        diceRoll()

@window.event
def on_mouse_release(x, y, button, modifiers):
    global guessValue
    global guessValueLabel
    if (x > 500 and x < 550) and (y > 100 and y < 150) and guessValue < 12:
        guessValue += 1
        guessValueLabel = pyglet.text.Label(str(guessValue), x=525, y=75,
                                                            anchor_x='center',
                                                            anchor_y='center',
                                                            color = (0,0,0,255))
    elif (x > 500 and x <550) and (y > 0 and y < 50) and guessValue > 2:
        guessValue -= 1
        guessValueLabel = pyglet.text.Label(str(guessValue), x=525, y=75,
                                                            anchor_x='center',
                                                            anchor_y='center',
                                                            color = (0,0,0,255))

def main():
    loadMoney()
    diceRoll()
    pyglet.app.run()



main()
