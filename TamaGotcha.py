

class Tama:
    def __init__(self, name = "TamaGotcha"):
        self.name = name
        self.age = 0
        self.commands = {'f': self.feed,
                        's': self.sleep,
                        'c': self.clean,
                        'v': self.vitals,
                        'h': self.help_me}

    def start_living(self):

        print("Hello! My name is {self.name}!\n\n")
        self.print_instructions()
        while True:
            command = input().strip().lower()
            execute_command = self.commands.get(command, "Not sure what you want me to do there! Enter [h] if you need to see the instructions again!")
            print(execute_command())

    def feed(self):

        self.last_fed = time.now()
        return "feed"
    
    def sleep(self):
        return "sleep"
    
    def clean(self):
        return "clean"    

    def vitals(self):
        return "vitals"     

    def help_me(self):
        return "help"   

    @staticmethod
    def print_instructions():
        print("Use the following commands to keep me alive and happy! :D\n",\
        "f:  Feed me!",
        "s:  Put me to bed... z Z z Z",
        "c:  Clean up my droppings @",
        "v:  Check my vitals!"
        "h:  Ask me for help to show these instructions again!", sep="\n")

