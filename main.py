########################################################
#                   Turtle Kart PC                     #
#      Code by Caleb Buening and Dayton Molendorp      #
#               Music by Adam Buening                  #
#                       main.py                        #
########################################################

import turtle as trtl
import controller, leaderboard as lb

# Load ctrl, which is what manages what is on the screen
ctrl = controller.Controller()
# A turtle for drawing the leaderboard
t = trtl.Turtle()
# Variables for storing leaderboard data
leader_names = []
leader_scores = []

# Load the titlescreen, which will continue until the user presses play
if ctrl.titleScreen(): # If this returns false the player doesn't want to continue and the program can end
    ctrl.chooseGameMode() # Not really in use right now as single player is the only option
    ctrl.chooseCars() # Selects player 1's car
    score = ctrl.runGame() # Runs the game and returns a score for the leaderboard to use
    name = trtl.textinput("Name", "Please input your name") # Get a name for the leaderboard
    lb.load_leaderboard("leaderboard_data.txt", leader_names, leader_scores) # Get leaderboard data
    lb.update_leaderboard("leaderboard_data.txt", leader_names, leader_scores, name, score) # Update leaderboard data
    lb.draw_leaderboard(leader_names, leader_scores, t) # Render the leaderboard
    trtl.mainloop()