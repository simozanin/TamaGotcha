from datetime import datetime
import random
import sys

class Tama:
    def __init__(self, name = "TamaGotcha"):
        self.name = name
        self.born = datetime.now()
        self.last_fed = None
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
        if self.is_sleeping:
            return "Shhh! I'm not hungry, I'm sleeping!"
        if not self.last_fed:
            message = "My tummy is happy now!"
        elif (datetime.now() - self.last_fed).seconds < 10:
            self.health = max(0, self.health-1)
            message = 'But my tummy hurts now...'
        else:
            self.health = min(10, self.health+1)
            message = "My tummy is happy now!"

        self.last_fed = datetime.now()
        self.seconds_till_next_meal = random.randint(20,30)


        return "Gotcha! "+ message
    
    def sleep(self):
        
        if self.is_sleeping:
            return "Shhh! I'm already sleeping!"
        else:
            self.is_sleeping = True
            self.started_sleeping = datetime.now()
            self.sleep_time = random.randint(15,25) + 10 * (self.is_baby or self.is_elderly)
            self.health = min(10, self.health+1)

        return "Gotcha... z Z z Z"
    
    def clean(self):
        if self.poops_around == 0:
            return "Nothing to clean, but thanks for asking!"
        self.poops_around -= 1
        return "Thanks for cleaning!"  

    def vitals(self):
        metrics = self.get_metrics()
        return ", ".join([k + ": " + str(metrics[k]) + "/10" for k in metrics])

    def help_me(self):
        return "\n".join(self.instructions()) 
    
    def get_metrics(self):
        return {"Health": self.health,
                "Feeding":  self.feed_status }
    
    def update(self):
        if self.no_orders_yet:
            if (datetime.now() - self.born).seconds > 30:
                print("It's been 30 seconds since I was born but I haven't been fed... Such a tragedy :-(")
                sys.exit(1)
            return
        
        if not self.is_sleeping:
            feed_status = float((datetime.now() - self.last_fed).seconds )/  self.seconds_till_next_meal
            self.feed_status = max(0, 10 - int(feed_status*100) //10 )
            if self.feed_status <= 2:
                print("My tummy is grumbling...")

            if self.poops_around > 3:
                print("Ewww, this place is stinky!")
                self.health = max(0, self.health -1)
        else:
            if (datetime.now() - self.started_sleeping).seconds > self.sleep_time:
                print("Yaaaaawn! Hello! I had a great sleep!")
                self.is_sleeping = False
                self.health = 10


        


    
    def check_on_me(self):
        self.update()




    def instructions(self):
        return ["#################################################################################",
        "",
        "Use the following commands to keep me alive and happy! :D\n",\
        "f:  Feed me!",
        "s:  Put me to bed... z Z z Z",
        "c:  Clean up my droppings @",
        "v:  Check my vitals!",
        "h:  Ask me for help to show these instructions again!",
        "\n\nIn order to give me the best life, feed me at least twice a minute,",
        "but not too often or I'll get sick! Feeding me increases my health!",
        "Sleeping also replenishes my health! I need to get some sleep every minute!",
        "While I'm asleep I don't get hungry, and I don't poop!",
        "Oh yeah, about that... I do need to poop sometimes, and you'll need to clean up.",
        "If the place gets too dirty I might start feeling sick...",
        "#################################################################################"]

