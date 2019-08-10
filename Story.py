import lines

class Story:
    def __init__(self):
        self.checkpoint = 0
        self.end = len(lines.lines)-1
        self.ter = False
        self.stories = lines.lines

    def get_start(self):
        return self.stories[0][0]

    def set_checkpoint(self, x : int):
        self.checkpoint = x

    def select_checkpoint(self):
        self.checkpoint += 1
        choice = input("Your choice:")
        while int(choice) > len(self.stories[self.checkpoint])-1:
            choice = input("Your choice:")
        x = int(choice)
        return self.stories[self.checkpoint][x]
