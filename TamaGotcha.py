from datetime import datetime
import random
import sys

class Tama:
    def __init__(self, name = "TamaGotcha"):
        self.name = name
        self.born = datetime.now()
        self.last_fed = None
        self.last_slept = None
        self.commands = {'f': self.feed,
                        's': self.sleep,
                        'c': self.clean,
                        'v': self.vitals,
                        'h': self.help_me}
        self.health = 10
        self.feed_status = 10
        self.is_baby = True
        self.is_adult = False
        self.is_elderly = False
        self.is_sleeping = False
        self.poops_around = 0
        self.no_orders_yet = True
        self.notified_hungry, self.notified_dirty = False, False

    def start_living(self):

        print("Hello! My name is {0}!\n\n".format(self.name))
        print("\n".join(self.instructions()))
        while True:
            try:
                command = input().strip().lower()
                if command in self.commands:
                    if command != "h":
                        self.no_orders_yet = False
                    execute_command = self.commands.get(command)
                    print(execute_command())
                else:
                    print("Not sure what you want me to do there! Enter [h] if you need to see the instructions again!")
            except KeyboardInterrupt:
                return

    def feed(self):
        self.notified_hungry = False
        if self.is_sleeping:
            return "Shhh! I'm not hungry, I'm sleeping!"
        if not self.last_fed:
            message = "My tummy is happy now!"
        elif (datetime.now() - self.last_fed).seconds < 10:
            self.health = max(0, self.health-1)
            message = 'But my tummy hurts now...'
        else:
            self.health = min(10, self.health+6)
            message = "My tummy is happy now!"

        self.last_fed = datetime.now()
        self.seconds_till_next_meal = random.randint(20,30)
        self.feed_status = 10

        return "Gotcha! "+ message
    
    def sleep(self):
        
        if self.is_sleeping:
            return "Shhh! I'm already sleeping!"
        else:
            self.is_sleeping = True
            self.started_sleeping = datetime.now()
            self.sleep_time = random.randint(10,15) + 5 * (self.is_baby or self.is_elderly)
            self.health = min(10, self.health+1)

        return "Gotcha... z Z z Z"
    
    def clean(self):
        if self.poops_around == 0:
            return "Nothing to clean, but thanks for being proactive!"
        self.poops_around -= 1
        self.notified_dirty = False
        return "Thanks for cleaning!"  

    def vitals(self):
        metrics = self.get_metrics()
        return ", ".join([k + ": " + str(metrics[k]) + "/10" for k in metrics])

    def help_me(self):
        return "\n".join(self.command_help()) 
    
    def get_metrics(self):
        return {"Health": self.health,
                "Feeding":  self.feed_status }
    
    def update(self):
        if self.no_orders_yet:
            if (datetime.now() - self.born).seconds > 30:
                print("It's been more than 30 seconds since I was born but I haven't been fed... Such a tragedy :-(")
                sys.exit(1)
            return
        
        if not self.is_sleeping:
            feed_status = float((datetime.now() - self.last_fed).seconds )/  self.seconds_till_next_meal
            self.feed_status = max(0, 10 - int(feed_status*100) //10 )

            if random.random() > .85:
                self.poops_around += 1
                print("Ooops, sorry, I had to poop!")

            if self.feed_status <= 2:
                self.health = max(0, self.health - 1)
                if not self.notified_hungry:
                    print("My tummy is grumbling...")
                    self.notified_hungry = True

            if self.poops_around > 2:
                self.health = max(0, self.health -1)
                if not self.notified_dirty:
                    print("Ewww, this place is stinky!")
                    self.notified_dirty = True
            
            if self.health == 3:
                print("I'm not feeling very well...")
            elif self.health == 2:
                print("I'm really not feeling well at all!")
            elif self.health == 1:
                print("Please do something!")
            elif self.health == 0:
                print("Oh no... Your TamaGotcha {0} died... :-(".format(self.name))
                sys.exit()

            if self.is_baby and (datetime.now() - self.born).seconds > random.randint(100, 150):
                self.is_baby = False
                self.is_adult = True
                print("Hey, I'm not a baby anymore! I'm a full grown TamaGotcha now!")
                return
            elif self.is_adult and (datetime.now() - self.born).seconds > random.randint(200, 300):
                self.is_adult = False
                self.is_elderly = True
                print("I'm getting old!")
                return
            elif self.is_elderly and (datetime.now() - self.born).seconds > random.randint(300, 350):
                print("Your TamaGotcha has died of old age. Thanks for taking such good care of {0}".format(self.name))
                sys.exit()


            if not self.last_slept:
                if (datetime.now() - self.born).seconds > 30:
                    print("Going to sleep now...")
                    self.sleep()
            else:
                if (datetime.now() - self.last_slept).seconds > 60:
                    print("Going to sleep now...")
                    self.sleep()



        else:
            if (datetime.now() - self.started_sleeping).seconds > self.sleep_time:
                print("Yaaaaawn! Hello! I had a great sleep!")
                self.is_sleeping = False
                self.health = 10
                self.last_slept = datetime.now()
                self.notified_dirty = False
                self.notified_hungry = False


        


    
    def check_on_me(self):
        self.update()


    def command_help(self):
        return ["Use the following commands to keep me alive and happy! :D\n",\
        "f:  Feed me!",
        "s:  Put me to bed... z Z z Z",
        "c:  Clean up my droppings @",
        "v:  Check my vitals!",
        "h:  Ask me for help to show these instructions again!",]

    def instructions(self):
        return ["#################################################################################",
        "\n\nIn order to give me the best life, feed me at least twice a minute,",
        "but not too often or I'll get sick! Feeding me increases my health!",
        "Sleeping also replenishes my health! I need to get some sleep every minute,",
        "and I'll go to sleep on my own if I'm feeling too tired.",
        "While I'm asleep I don't get hungry, and I don't poop!",
        "Oh yeah, about that... I do need to poop sometimes, and you'll need to clean up.",
        "If the place gets too dirty I might start feeling sick...",
        "\n".join(self.command_help()),
        "#################################################################################"]

