import controller

# Load the renderer, which is what manages what is on the screen
ctrl = controller.Controller()

# Load the titlescreen, which will continue until the user presses play
if ctrl.titleScreen(): # If this returns false the player doesn't want to continue
    # while True:
    gameMode = ctrl.chooseGameMode()
    ctrl.chooseCars(gameMode)

    # playAgain = True
    # while playAgain:
    #     map = ctrl.chooseMap()
    #     playAgain = ctrl.runGame(gameMode, map)