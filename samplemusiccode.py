from playsound import playsound
from threading import Thread
 
def play_music():
    playsound('wooboost.mp3')
 
# Play Music on Separate Thread (in background)
music_thread = Thread(target=play_music)
music_thread.start()
 
print("Does playsound block the main thread?")
user_input = input("What is your guess?: ")
print("You guessed: " + user_input)