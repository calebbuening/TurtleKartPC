import turtle as trtl
import controller, leaderboard as lb

# Load the renderer, which is what manages what is on the screen
ctrl = controller.Controller()
t = trtl.Turtle()
ct = trtl.Turtle()
leader_names = []
leader_scores = []

# Load the titlescreen, which will continue until the user presses play
if ctrl.titleScreen(): # If this returns false the player doesn't want to continue
    # while True:
    ctrl.chooseCars()
    score = ctrl.runGame()
    name = trtl.textinput("Name", "Please input your name")
    lb.load_leaderboard("leaderboard_data.txt", leader_names, leader_scores)
    lb.update_leaderboard("leaderboard_data.txt", leader_names, leader_scores, name, score)
    lb.draw_leaderboard(leader_names, leader_scores, t)
    trtl.mainloop()