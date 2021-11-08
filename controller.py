########################################################
#                   Turtle Kart PC                     #
#      Code by Caleb Buening and Dayton Molendorp      #
#               Music by Adam Buening                  #
#                   controller.py                      #
########################################################

import turtle as trtl, leaderboard as lb
from threading import Thread
from playsound import playsound
import time

class Controller:

    def __init__(self):
        # Configure the screen
        self.wn = trtl.Screen()
        self.wn.title("Turtle Kart PC")
        self.wn.setup(width=750, height=500)
        self.wn.tracer(0, 0)

        # Configure the turtle that prints out the lap
        self.lapTurtle = trtl.Turtle()
        self.lapTurtle.pu()
        self.lapTurtle.ht()
        self.lapTurtle.goto(-350, 150) # -250,300
        self.lapTurtle.pd()

        # Configure the turtle that prints out the time
        self.counterTurtle = trtl.Turtle()
        self.counterTurtle.pu()
        self.counterTurtle.ht()
        self.counterTurtle.goto(-350, 125)
        self.counterTurtle.pd()

        self.gameOver = False
        self.buttonPressed = False # For loops that wait for a button to be pressed
        self.cont = True # Stores titlescreen choice
        self.gamemode = 0 # Unused
        self.player1car = "" # Car color
        self.player2car = "" # Unused
        self.elcarro1 = None # The car object
        self.elcarro2 = None # Unused
        self.car1speed = 0
        self.car2speed = 0
        self.car1laps = 0
        self.car2laps = 0
        self.windowxy = (750, 500)
        self.finishLine = False # For when the car is on the finish line
        self.time = 0 # For storing the current time
        self.startTime = 0
        self.prevTime = -1 # For keeping track of if the time has changed or not

        # Button state variables
        self.buttonW = False
        self.buttonA = False
        self.buttonS = False
        self.buttonD = False

        # A canvas for fancy effects if necessary (Unused)
        self.cv = trtl.getcanvas()

    def makeMusic(self):
        # Play the music until the code stops
        while True:
            playsound("sounds/TurtleGroove.wav")
    
    def titleScreenClickHandler(self, x, y):
        # If a button has been pressed, set the buttonPressed variable and store cont = True if the game is to be played
        if x > -12 and x < 310:
            if y < 105 and y > -4:
                self.buttonPressed = True
            if y > -164 and y < -49:
                self.buttonPressed = True
                self.cont = False

    def gamemodeClickHandler(self, x, y):
        # Same as above code buton with different button locations and action variables
        if y > -164 and y < 134:
            if x > -330 and x < -30:
                self.buttonPressed = True
                self.gamemode = 1
            if x > 3 and x < 312:
                self.buttonPressed = True
                self.gamemode = 2
    
    def chooseCarClickHandler(self, x, y):
        # See the commentary for the function above
        if x > -342 and x < 331:
            if y > 45 and y < 151:
                self.buttonPressed = True
                if self.player1car == "": self.player1car = "red"
                else: self.player2car = "red"
            if y > -83 and y < 16:
                self.buttonPressed = True
                if self.player1car == "": self.player1car = "green"
                else: self.player2car == "green"
            if y > -214 and y < -118:
                self.buttonPressed = True
                if self.player1car == "": self.player1car = "blue"
                else: self.player2car = "blue"

    def chooseGameMode(self):
        # We dont have a second gamemode because of time restrictions
        self.gamemode = 1
        return

        trtl.clearscreen()

        self.wn.bgpic("backgrounds/gamemode_selection.png")
        self.wn.onclick(self.gamemodeClickHandler)
        self.wn.listen()

        while not self.buttonPressed:
            trtl.update()
            trtl.delay(10)

        # Reset click handler
        self.wn.onclick(None)
        self.wn.listen()
        self.buttonPressed = False
        return self.gamemode

        # Go fullscreen and store dimensions
        # self.wn.setup(width=1.0, height = 1.0)
        # self.windowxy = self.wn.screensize()

    # Callback functions for setting button state variables
    def buttonWPressed(self): self.buttonW = True
    def buttonAPressed(self): self.buttonA = True
    def buttonSPressed(self): self.buttonS = True
    def buttonDPressed(self): self.buttonD = True

    def buttonWReleased(self): self.buttonW = False
    def buttonAReleased(self): self.buttonA = False
    def buttonSReleased(self): self.buttonS = False
    def buttonDReleased(self): self.buttonD = False

    def titleScreen(self):
        # Listen for the click on either button
        self.wn.onclick(self.titleScreenClickHandler)
        self.wn.listen()

        self.wn.bgpic("backgrounds/title_screen.png")

        # Choose each bg based off of mouse location
        while not self.buttonPressed:
            # x, y = self.cv.winfo_pointerxy()
            # if x > 364+595 and x < 685+595:
            #     if y > 144+325 and y < 255+325:
            #         self.wn.bgpic("backgrounds/title_screen_select_top.png")
            #     elif y > 301+325 and y < 413+325:
            #         self.wn.bgpic("backgrounds/title_screen_select_bottom.png")
            #     else:
            #         self.wn.bgpic("backgrounds/title_screen.png")
            # else:
            #     self.wn.bgpic("backgrounds/title_screen.png")
            trtl.update()
            trtl.delay(10)
        self.buttonPressed = False # Reset the value

        # Clear the listener
        self.wn.onclick(None)
        self.wn.listen()
        return self.cont

    def chooseCars(self):
        trtl.clearscreen()

        self.wn.bgpic("backgrounds/car_selection_1player.png")
        
        # Wait for selection
        self.wn.onclick(self.chooseCarClickHandler)
        self.wn.listen()

        # Wait for a button press
        while not self.buttonPressed:
            trtl.update()
            trtl.delay(10)

        # Reset stuff
        self.wn.onclick(None)
        self.wn.listen()
        self.buttonPressed = False

    def startTimer(self):
        # This stores the start time for later use when calculating total race time
        self.startTime = time.time()

    def runTimer(self):
        # As long as the game has not ended
        if not self.gameOver and self.time != str(int(time.time() - self.startTime)):
            # Calculate time string
            self.time = str(int(time.time() - self.startTime))
            # Print the time
            self.counterTurtle.clear()
            self.counterTurtle.write("Time: " + str(int(time.time() - self.startTime)), font=("Arial", 12, "normal"))
            # Repeat 1 second from now
            trtl.ontimer(self.runTimer, 1000)

    def lap(self):
        # Print out what lap we are now on
        self.lapTurtle.clear()
        self.lapTurtle.write("Lap: " + str(self.car1laps) + "/3", font=("Arial", 12, "normal"))
        self.finishLine = True

        # Start the timer when the race starts
        if self.car1laps == 1:
            self.startTimer()
            trtl.ontimer(self.runTimer, 1000)

    def singlePlayer(self):
        # Create the first car
        self.elcarro1 = trtl.Turtle(shape="square") 
        self.elcarro1.ht()
        self.elcarro1.seth(180)
        self.elcarro1.color(self.player1car)
        self.elcarro1.shapesize(stretch_wid= .5, stretch_len= .875)
        self.elcarro1.pu()
        self.elcarro1.goto(30, 150)
        self.elcarro1.st()

        # Movement callbacks
        self.wn.onkeypress(self.buttonWPressed, "w")
        self.wn.onkeypress(self.buttonAPressed, "a")
        self.wn.onkeypress(self.buttonSPressed, "s")
        self.wn.onkeypress(self.buttonDPressed, "d")

        self.wn.onkeyrelease(self.buttonWReleased, "w")
        self.wn.onkeyrelease(self.buttonAReleased, "a")
        self.wn.onkeyrelease(self.buttonSReleased, "s")
        self.wn.onkeyrelease(self.buttonDReleased, "d")
        self.wn.onclick(print)
        self.wn.listen()

        while not self.gameOver:
            # Update speeds
            if self.player1car == "red":
                if self.buttonW:
                    self.car1speed += .015
                elif self.buttonS:
                    self.car1speed -= .08
                else:
                    self.car1speed *= .05

            if self.player1car == "green":
                if self.buttonW:
                    self.car1speed += .010
                elif self.buttonS:
                    self.car1speed -= .05
                else:
                    self.car1speed *= .05

            if self.player1car == "blue":
                if self.buttonW:
                    self.car1speed += .005
                elif self.buttonS:
                    self.car1speed -= .003
                else:
                    self.car1speed *= .05

            # Max out the speeds
            if self.player1car == "red" and self.car1speed > 1:
                self.car1speed = 1
            if self.player1car == "green" and self.car1speed > 1.5:
                self.car1speed = 1.5
            if self.player1car == "blue" and self.car1speed > 2:
                self.car1speed = 2

            if self.player1car == "red" and self.car1speed < -1:
                self.car1speed = -1
            if self.player1car == "green" and self.car1speed < -1.5:
                self.car1speed = -1.5
            if self.player1car == "blue" and self.car1speed < -2:
                self.car1speed = -2

            # Update displacements
            if self.buttonA:
                self.elcarro1.seth(self.elcarro1.heading() + 10)
            if self.buttonD:
                self.elcarro1.seth(self.elcarro1.heading() - 10)

            # Apply displacements
            self.elcarro1.fd(self.car1speed)

            # Detect if the car has crossed the finish line, and if it was already on the finish line or not
            if(self.elcarro1.xcor() > 16 and self.elcarro1.xcor() < 18 \
                and self.elcarro1.ycor() > 138 and self.elcarro1.ycor() < 188): # Finish line boundaries
                self.car1laps += 1 and not self.finishLine # Add a lap to the counter
                if (self.car1laps > 3): # Finish the game on the last lap
                    self.gameOver = True
                else:
                    self.lap() # Run the lap code
            else:
                self.finishLine = False # If we aren't on the finish line, keep this variable set to false


            # if(self.elcarro1.xcor() > 12 and self.elcarro1.xcor() < 14 \
            #     and self.elcarro1.ycor() > -121 and self.elcarro1.ycor() < -181):
                
            # Update stuff
            trtl.update()

    def runGame(self):
        # Load background
        trtl.clearscreen()
        self.wn.bgpic("backgrounds/basic_track.png")

        # Run background music (Daemon causes the music to stop when the rest of the code does)
        musicThread = Thread(target=self.makeMusic, daemon=True)
        musicThread.start()

        self.singlePlayer()

        return int(time.time() - self.startTime) # Returns the car's finish time