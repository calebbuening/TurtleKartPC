import turtle as trtl

# TODO: Add boundaries so that the turtle can't get lost from going off the screen

class Controller:

    def __init__(self):
        self.wn = trtl.Screen()
        self.wn.title("Turtle Kart PC")
        self.wn.setup(width=750, height=500)

        self.buttonPressed = False
        self.cont = True
        self.gamemode = 0
        self.player1car = ""
        self.player2car = ""
        self.elcarro1 = None
        self.elcarro2 = None
        self.windowxy = (750, 500)

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
        if self.gamemode == 2:
            self.wn.bgpic("backgrounds/car_selection_2player_p1.png")
        
        # Wait for selection
        self.wn.onclick(self.chooseCarClickHandler)
        self.wn.listen()

        while not self.buttonPressed:
            trtl.update()
            trtl.delay(10)

        self.buttonPressed = False
        self.wn.bgpic("backgrounds/car_selection_2player_p2.png")

        if(self.gamemode == 2):
            while not self.buttonPressed:
                trtl.update()
                trtl.delay(10)
        
        # Reset stuff
        self.wn.onclick(None)
        self.wn.listen()
        self.buttonPressed = False

    def singlePlayer(self):
        gameOver = False

        # Create the first car
        self.elcarro1 = trtl.Turtle(shape="square") 
        self.elcarro1.ht()
        self.elcarro1.seth(180)
        self.elcarro1.color(self.player1car)
        self.elcarro1.shapesize(stretch_wid= 1, stretch_len= 1.75)
        self.elcarro1.pu()
        self.elcarro1.goto(30, 150)
        self.elcarro1.st()

        # Movement callbacks
        self.wn.onkeypress(self.buttonWPressed , "w")
        self.wn.onkeypress(self.buttonAPressed, "a")
        self.wn.onkeypress(self.buttonSPressed, "s")
        self.wn.onkeypress(self.buttonDPressed, "d")

        self.wn.onkeyrelease(self.buttonWReleased, "w")
        self.wn.onkeyrelease(self.buttonAReleased, "a")
        self.wn.onkeyrelease(self.buttonSReleased, "s")
        self.wn.onkeyrelease(self.buttonDReleased, "d")

        while True:
            if self.buttonW: self.elcarro1.fd(1)
            if self.buttonA: self.elcarro1.lt(10)
            if self.buttonS: self.elcarro1.fd(-1)
            if self.buttonD: self.elcarro1.rt(10)
            trtl.update()

        # while not gameOver:
    
    def twoPlayer(self):
        gameOver = False
        elcarro = trtl.Turtle(shape ="square")
    def runGame(self):
        trtl.clearscreen()
        self.wn.bgpic("backgrounds/basic_track.png")

        if self.gamemode == 1:
            self.singlePlayer()
        if self.gamemode == 2:
            self.twoPlayer()