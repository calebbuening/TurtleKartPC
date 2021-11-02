import turtle
import controller, leaderboard as lb

# Load the renderer, which is what manages what is on the screen
ctrl = controller.Controller()
t = turtle.Turtle()
ct = turtle.Turtle()
leader_names = []
leader_scores = []

# Load the titlescreen, which will continue until the user presses play
if ctrl.titleScreen(): # If this returns false the player doesn't want to continue
    # while True:
    gameMode = ctrl.chooseGameMode()
    ctrl.chooseCars()
    score = ctrl.runGame()
    lb.load_leaderboard("leaderboard_data.txt", leader_names, leader_scores)
    lb.update_leaderboard(leader_names, leader_scores, True, t, score, ct)