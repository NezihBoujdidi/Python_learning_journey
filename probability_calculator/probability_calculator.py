** learned how to use the copy module , to copy mutable types without the original one being affected, like x= copy.deepcopy({'c':1,'b':5}), but when using copy.copy on nested objects
    like [1,2,[3,4]] changing 3 or 4 in the copy will affect the original but changing 1 or 2 wont **
** in __init__ , **kwargs will tell that the kwargs will be a dict of key values , but *args will be simple list **

import copy
import random

class Hat:
    __slots__ = ('__contents')

    def __init__(self, **args):
        if len(args) == 0:
            raise TypeError(f"the {__class__.__name__} class takes at least one argument of a color but 0 were given")
        self.__contents = []
        for color , i in args.items():
            for _ in range(i):
                self.__contents.append(color)
        print(self.__contents)


    @property
    def contents(self):
        return self.__contents
    
    @contents.setter
    def contents(self, value):
        self.__contents = value


    def draw(self, number):
        removed_balls = []
        for _ in range(number):
            if len(self.__contents) == 0 :
                break   
            removed_ball = self.__contents.pop(random.randint(0,len(self.__contents)-1))
            removed_balls.append(removed_ball)
        return removed_balls
            


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if not isinstance(hat, Hat):
        raise TypeError(f"{hat} should be an instance of {Hat.__name__}")
    balls = copy.deepcopy(hat.contents)
    m = 0
    for _ in range(num_experiments):
        match = 0
        hat.contents = copy.deepcopy(balls)
        removed_balls = hat.draw(num_balls_drawn)
        for color , value in expected_balls.items():
            if removed_balls.count(color) < value :
                break
            else:
                match += 1
        if match == len(expected_balls) :
            m += 1
    return m/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=20)
print(probability)
