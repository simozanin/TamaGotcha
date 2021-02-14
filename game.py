from TamaGotcha import Tama
import random
import threading
import time
import sys 



class Game:
    def print_intro_message(self):
        print("###################################\n",
          "Welcome to TamaGotcha\n",
          "###################################\n")
    def __init__(self):

        self.print_intro_message()
    
    def play(self):
        name = input("What do you want to name me?\n")
        self.my_pet = Tama(name)
        x = threading.Thread(target=self.my_pet.start_living)
        x.daemon = True
        try:
            # We need two threads
            # one for receiving inputs
            # and one for checking that
            # the TamaGotcha is alive etc.
            x.start()
            self.monitor_condition()
        except KeyboardInterrupt:
            x.join()
            
    def monitor_condition(self):
        while True:
            try:
                # Every two seconds, check on the TamaGotcha
                time.sleep(2)
                self.my_pet.check_on_me()
            except KeyboardInterrupt:
                return



