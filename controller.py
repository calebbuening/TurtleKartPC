import turtle as trtl

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
        self.windowxy = (750, 500)

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
                if self.player1car == "": self.player1car == "blue"
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

        trtl.clearscreen()
        trtl.mainloop()

    def singlePlayer():
        gameOver = False



        # while not gameOver:

    def runGame(self):
        if self.gamemode == 1:
            self.singlePlayer()
        if self.gamemode == 2:
            self.twoPlayer()