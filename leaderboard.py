#   leaderboard.py
# The leaderboard module to be used in a122 solution.
import turtle as trtl

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 26

# load leaderboard from file
def load_leaderboard(file_name, leader_names, leader_scores):

  leaderboard_file = open(file_name, "r")  # need to create the file ahead of time in same folder

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  for line in leaderboard_file:
    leader_name = ""
    leader_score = ""    

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    leader_name = line[0:line.find(",")]
    if(leader_name == ""): leader_name = "Unknown Player"

    # TODO 2: add the leader name to the list
    leader_names.append(leader_name)
    
    # Read the player score using a similar loop
    leader_score = line[line.find(",")+1:line.find("\n")]
    
    # Add the player score to the list
    leader_scores.append(leader_score)

  leaderboard_file.close()


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

  # Bonus code:
  if player_name == "":
    player_name = "Unknown Player"

  leader_index = 0
  # TODO 5: loop through all the scores in the existing leaderboard list
  while leader_index < len(leader_scores):
    # TODO 6: check if this is the position to insert new score at
    if (int(leader_scores[leader_index]) < int(player_score)):
      break
    else:
      leader_index = leader_index + 1

  # TODO 7: insert the new player and score at the appropriate position
  if leader_index == len(leader_scores):
    leader_scores.append(player_score)
    leader_names.append(player_name)
  else:
    leader_scores.insert(leader_index, player_score)
    leader_names.insert(leader_index, player_name)

  # TODO 8: keep both lists at 5 elements only (top 5 players)
  leader_names = leader_names[0:4]
  leader_scores = leader_scores[0:4]
  
  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
  leader_index = 0
  # TODO 9: loop through all the leaderboard elements and write them to the file
  while leader_index < len(leader_names):
    leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
    leader_index = leader_index + 1
  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(leader_names, leader_scores, turtle_object):
  trtl.clearscreen()
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.hideturtle()
  turtle_object.goto(-200,100)
  turtle_object.down()
  leader_index = 0

  # Draw the labels for the leaderboard
  turtle_object.write("Place\tName\t\tScore", font=font_setup)
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.down()

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while leader_index < len(leader_names):
    turtle_object.write(str(leader_index + 1) + "\t" + leader_names[len(leader_names) - leader_index - 1] + "\t" + str(leader_scores[len(leader_scores) - leader_index - 1]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
    leader_index = leader_index + 1

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()