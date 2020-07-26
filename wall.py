import numpy as np
import matplotlib.pyplot as plt

class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

class Wall:

    def __init__(self,wallXSize,wallYSize):
        self.case_mur = np.empty([wallXSize,wallYSize])

    def wallAdd(self,p):
        self.case_mur[p.get_x(),p.get_y()] = 1

    def wallHere(self,x,y):
        if(self.case_mur[x,y] == 1):
            return True
        else:
            return False
        

    
    

    