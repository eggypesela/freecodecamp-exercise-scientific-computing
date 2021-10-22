#! /usr/bin/env/python3
#created by Regina Citra Pesela (reginapasela@gmail.com)

import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        #create dictionary variable
        self.balls = dict()
        for key, value in kwargs.items():
            if value > 0:
                self.balls[key] = value

        #create list from variables
        # self.ballList = list()
        self.contents = list()

        #append each balls to ballList
        for i in self.balls:
            for j in range(self.balls[i]):
                self.contents.append(i)
        
        self.contentsCopy = copy.copy(self.contents)
            
    def draw(self, numberDraw):
        self.ballDrawList = list()
        self.countBallList = len(self.contents) - 1

        #If the number of balls to draw exceeds the available quantity, return all the balls
        if numberDraw >= len(self.contentsCopy):
            return self.contentsCopy
            
        #draw object in ballList to ballDrawList by index
        for i in range(numberDraw):
            try:
                #generate random number from 0 to ballList
                self.indexNum = random.randint(0, self.countBallList)
                
                #pop ballList by index and then put those pop value into ballDrawList
                self.ballDrawList.append(self.contents[self.indexNum])
                
                #commented for experiment
                self.contents.pop(self.indexNum)
                
                #make sure ballcount minus 1 each loop because we grab 1 item from ballList
                self.countBallList -= 1

            except:
                self.contents = copy.copy(self.contentsCopy)
            
            
        #print("contentsReal = ", self.contents)
        #print("contentsCopy = ", self.contentsCopy)

        return self.ballDrawList

def experiment(hat, expected_balls, num_balls_drawn = 1, num_experiments = 1):
    ballDrawDict = dict()
    countSuccess = 0
    countBall = 1
    ballDraw = list()

    #loop by number of experiments
    for i in range(num_experiments):
        if len(hat.contents) == (num_balls_drawn - 1):
            #reset self.contentsCopy
            hat.contents = copy.copy(hat.contentsCopy)
        
        #draw balls from object
        ballDraw = hat.draw(num_balls_drawn)
        
        #convert ballDrawList into dict
        for j in ballDraw:
            ballDrawDict[j] = ballDrawDict.get(j, 0) + 1

        # compare ballDrawList to expected_balls, if same countSuccess +1
        if set(expected_balls.keys()).issubset(ballDrawDict.keys()):
            counterCompare = 0
            for i in expected_balls.keys():
                if ballDrawDict.get(i) >= expected_balls.get(i):
                    counterCompare += 1
        
                if counterCompare == len(expected_balls):
                    countSuccess += 1

        #reset the dictionary
        ballDrawDict = dict()
            
    return countSuccess / num_experiments