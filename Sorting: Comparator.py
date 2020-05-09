from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score 
        
    def __repr__(self):
        return "{} {}".format(self.name, self.score)


    def comparator(a, b):
        if a.name is b.name and a.score is b.score:
            return 0
        elif a.score is b.score:
            return 1 if a.name > b.name else -1
        return 1 if a.score < b.score else -1


