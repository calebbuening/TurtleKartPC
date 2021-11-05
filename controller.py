import turtle as trtl, leaderboard as lb

# TODO: Add boundaries so that the turtle can't get lost from going off the screen

class Controller:

    def __init__(self):
        self.wn = trtl.Screen()
        self.wn.title("Turtle Kart PC")
        self.wn.setup(width=750, height=500)
        self.wn.tracer(0, 0)

        self.lapTurtle = trtl.Turtle()
        self.lapTurtle.pu()
        self.lapTurtle.ht()
        self.lapTurtle.goto(-350, 150) # -250,300
        self.lapTurtle.pd()

        self.counterTurtle = trtl.Turtle()
        self.counterTurtle.pu()
        self.counterTurtle.ht()
        self.counterTurtle.goto(-350, 125)
        self.counterTurtle.pd()

        self.gameOver = False
    
        self.buttonPressed = False
        self.cont = True
        self.gamemode = 0
        self.player1car = ""
        self.player2car = ""
        self.elcarro1 = None
        self.elcarro2 = None
        self.car1speed = 0
        self.car2speed = 0
        self.car1laps = 0
        self.car2laps = 0
        self.windowxy = (750, 500)
        self.finishLine = False
        self.time = -1
        self.prevTime = -1

        self.buttonW = False
        self.buttonA = False
        self.buttonS = False
        self.buttonD = False

        self.cv = trtl.getcanvas()
    
    def titleScreenClickHandler(self, x, y):
        if x > -12 and x < 310:
            if y < 105 and y > -4:
                self.buttonPressed = True
            if y > -164 and y < -49:
                self.buttonPressed = True
                self.cont = False

    def gamemodeClickHandler(self, x, y):
        if y > -164 and y < 134:
            if x > -330 and x < -30:
                self.buttonPressed = True
                self.gamemode = 1
            if x > 3 and x < 312:
                self.buttonPressed = True
                self.gamemode = 2
    
    def chooseCarClickHandler(self, x, y):
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

        if self.gamemode == 1:
            self.wn.bgpic("backgrounds/car_selection_1player.png")
        
        # Wait for selection
        self.wn.onclick(self.chooseCarClickHandler)
        self.wn.listen()

        while not self.buttonPressed:
            trtl.update()
            trtl.delay(10)

        # Reset stuff
        self.wn.onclick(None)
        self.wn.listen()
        self.buttonPressed = False

    def timer(self):
        if not self.gameOver:
            self.time += 1
            self.counterTurtle.clear()
            self.counterTurtle.write("Time: " + str(int(self.time)), font=("Arial", 12, "normal"))
            trtl.ontimer(self.timer, 1000)

    def lap(self):
        self.lapTurtle.clear()
        self.lapTurtle.write("Lap: " + str(self.car1laps) + "/3", font=("Arial", 12, "normal"))
        self.finishLine = True
        if self.car1laps == 1:
            trtl.ontimer(self.timer, 1000)

    def singlePlayer(self):
        gameOver = False

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
                    self.car1speed += 15
                elif self.buttonS:
                    self.car1speed -= 8
                else:
                    self.car1speed *= .5

            if self.player1car == "green":
                if self.buttonW:
                    self.car1speed += 10
                elif self.buttonS:
                    self.car1speed -= 5
                else:
                    self.car1speed *= .5

            if self.player1car == "blue":
                if self.buttonW:
                    self.car1speed += 5
                elif self.buttonS:
                    self.car1speed -= 2
                else:
                    self.car1speed *= .5

            # Max out the speeds
            if self.player1car == "red" and self.car1speed > 1000:
                self.car1speed = 1000
            if self.player1car == "green" and self.car1speed > 1500:
                self.car1speed = 1500
            if self.player1car == "blue" and self.car1speed > 2000:
                self.car1speed = 2000

            self.car1speed *= .1

            # Update displacements
            if self.buttonA:
                self.elcarro1.seth(self.elcarro1.heading() + 10)
            if self.buttonD:
                self.elcarro1.seth(self.elcarro1.heading() - 10)

            self.elcarro1.fd(self.car1speed)

            if(self.elcarro1.xcor() > 16 and self.elcarro1.xcor() < 18 \
                and self.elcarro1.ycor() > 138 and self.elcarro1.ycor() < 188):
                self.car1laps += 1 and not self.finishLine
                if (self.car1laps > 2):
                    self.gameOver = True
                else:
                    self.lap()
            else:
                self.finishLine = False


            # if(self.elcarro1.xcor() > 12 and self.elcarro1.xcor() < 14 \
            #     and self.elcarro1.ycor() > -121 and self.elcarro1.ycor() < -181):
                
            # Update stuff
            trtl.update()
            self.prevTime = self.time

    def runGame(self):
        trtl.clearscreen()
        self.wn.bgpic("backgrounds/basic_track.png")

        if self.gamemode == 1:
            self.singlePlayer()
        return self.time