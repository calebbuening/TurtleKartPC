import turtle as trtl

class Controller:
    def clickHandler(self, x, y):
        if x > -12 and x < 310:
            if y < 105 and y > -4:
                self.buttonPressed = True
            if y > -164 and y < -49:
                self.buttonPressed = True
                self.cont = False

    def __init__(self):
        self.wn = trtl.Screen()
        self.wn.title("Turtle Kart PC")
        self.wn.setup(width=750, height=500)

        self.buttonPressed = False
        self.cont = True
        self.windowxy = (750, 500)

        self.cv = trtl.getcanvas()
    
    def chooseGameMode(self):
        trtl.clearscreen()
        # Go fullscreen and store dimensions
        self.wn.setup(width=1.0, height = 1.0)
        self.windowxy = self.wn.screensize()
        trtl.mainloop()

    def titleScreen(self):
        # Listen for the click on either button
        self.wn.onclick(self.clickHandler)
        self.wn.listen()

        # Choose each bg based off of mouse location
        while not self.buttonPressed:
            x, y = self.cv.winfo_pointerxy()
            if x > 364+595 and x < 685+595:
                if y > 144+325 and y < 255+325:
                    self.wn.bgpic("backgrounds/title_screen_select_top.png")
                elif y > 301+325 and y < 413+325:
                    self.wn.bgpic("backgrounds/title_screen_select_bottom.png")
                else:
                    self.wn.bgpic("backgrounds/title_screen.png")
            else:
                self.wn.bgpic("backgrounds/title_screen.png")
            trtl.update()
            trtl.delay(10)

        # Clear the listener
        self.wn.onclick(None)
        self.wn.listen()
        return self.cont