from TamaGotcha import Tama
import random
import threading
import time

class Game:
    def print_intro_message(self):
        print("Welcome to TamaGotcha\n",
          "###################################\n")
    def __init__(self):

        self.print_intro_message()
    
    def play(self):

        self.my_pet = Tama()
        x = threading.Thread(target=self.my_pet.start_living)
        x.start()
        self.monitor_condition()

    def monitor_condition(self):
        while True:
            time.sleep(1)
            # print("It's been 10 seconds")


