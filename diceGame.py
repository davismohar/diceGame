import pyglet
from pyglet.window import key
import random
from pyglet.gl import *
import csv
#TODO add money system
#TODO add account system

#declaring global variables
window = pyglet.window.Window()
#dice 1 and dice 2
dice1 = None
dice2 = None
dice2Roll = 0
dice1Roll = 0
guessValue = 6
winConditon = False
playerMoney = 0
betValue = 5

#Loads money array from bank.csv, and saves it as playerMoney array
playerMoney = []
def loadMoney():
    global playerMoney
    with open("bank.csv", "rb") as bank:
        bankReader = csv.reader(bank)
        for row in bankReader:
            playerMoney = row

def saveMoney():
    with open("bank.csv", "wb") as bank:
        bankWriter = csv.writed(bank)
        bankWriter.writerow(playerMoney)

#adds x to betvalue and subtracts that amount from playerMoney
#TODO playerMoney is out of bounds
def bet(bet):
    global betValue
    global playerMoney
    betValue += bet
    playerMoney[0] = int(playerMoney[0]) - bet


#The text of the guessValue
guessValueLabel = pyglet.text.Label("Guess: "+str(guessValue), x = 525, y = 75,
                                                    anchor_x='center',
                                                    anchor_y='center',
                                                    color = (0,0,0,255))

#The text of betValue
betValueLabel = pyglet.text.Label("Bet: "+str(betValue), x = 600, y= 75,
                                                    anchor_x='center',
                                                    anchor_y='center',
                                                    color = (0,0,0,255))
#sets vertex list for triangles
valueUpTriangle = pyglet.graphics.vertex_list(3, ('v2f', [500,100, 550,100, 525,150]))
valueDownTriangle = pyglet.graphics.vertex_list(3, ('v2f', [500,50, 550,50, 525,0]))
betUpTriangle = pyglet.graphics.vertex_list(3, ('v2f', [575,100, 625,100, 600,150]))
betDownTriangle = pyglet.graphics.vertex_list(3, ('v2f', [575,50, 625,50, 600,0]))
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
    valueUpTriangle.draw(GL_TRIANGLES)
    valueDownTriangle.draw(GL_TRIANGLES)
    betUpTriangle.draw(GL_TRIANGLES)
    betDownTriangle.draw(GL_TRIANGLES)
    guessValueLabel.draw()
    betValueLabel.draw()
    print (str(guessValue) + " " + str(dice1Roll+dice2Roll)+ " " + str(betValue) + " " + str(playerMoney[0]))
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
    global betValue
    global betValueLabel

    #tests if mouseclick is on increase guess value triangle
    if (x > 500 and x < 550) and (y > 100 and y < 150) and guessValue < 12:
        guessValue += 1
        guessValueLabel.text = "Guess: " + str(guessValue)
    #tests if mouseclick is on decrease guess value triangle
    elif (x > 500 and x <550) and (y > 0 and y < 50) and guessValue > 2:
        guessValue -= 1
        guessValueLabel.text = "Guess :" + str(guessValue)
    #tests if mouseclick is on increase bet value triangle
    elif (x > 575 and x < 625) and (y > 100 and y < 150) and playerMoney[0] > 5:
        bet(5)
        betValueLabel.text = "Bet: " + str(betValue)
    #tests if mouseclick is on decrease bet value triangle
    elif (x > 575 and x < 625) and (y > 0 and y < 50) and betvalue > 0:
        bet(-5)
        betValueLabel.text = "Bet: " + str(betValue)


def main():
    diceRoll()
    loadMoney()
    print playerMoney
    pyglet.app.run()





main()
