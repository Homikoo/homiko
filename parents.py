import random
class human:
    legs = 2
    head = 1
    hands = 2
    eye = None
    hair = None
class mom(human):
    def __init__(self):
        self.eye = 'blue eyes'
        self.hair = 'blond hair'
print(('mom: '), mom().eye, mom().hair)

class papa(human):
    def __init__(self):
        self.eye = 'green eyes'
        self.hair = 'black hair'
       
print(('papa: '), papa().eye, papa().hair)  
      
class baby(human):
    def __init__(self):
        e = random.randrange(0, 2)
        h = random.randrange(0, 2)
        if e == 1:
            self.eye = mom().eye
        else:
            self.eye = papa().eye
        if h == 1:
            self.hair = mom().hair
        else:
            self.hair = papa().hair
print(("baby: "), baby().eye,  baby().hair)


