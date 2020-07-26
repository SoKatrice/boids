from math import cos,sin,pi,floor
import random
import wall

################################
# Classe correspondant aux boids
# Un boid possède :
#    - une position x
#    - une position y
#    - Une vitesse v (qu'on considère comme constante pour l'instant)
#    - Un angle a
#    - nouveau_x et nouveau_y pour gérer les trucs
#    - ...
# Un boid peut :
#    - boidMove() : Se déplacer
#    - boidMeet() : Rencontrer quelqu'un et adapter son comportement en conséquence
#    - boidAvoid() : Changer de trajectoire en approchant un obstacle 
#    - ...
###############################
class boid:

    def __init__(self,x,y,v,a):
        self.x = x
        self.y = y
        self.v = v
        self.v_save = v
        self.a = a
        self.nouveau_x = 0
        self.nouveau_y = 0

        self.chmgt_angle = 0

        self.bordure_safe_2 = 4 * self.v
        self.avoided = False
        self.cpt_avoided = 0


    def boidBehave(self,mur):
        self.boidAvoid(mur)
        self.boidMove()
        self.boidUpdate()

    # Boid se déplace
    def boidMove(self):
        self.nouveau_x = self.x + self.v * cos(self.a)
        self.nouveau_y = self.y + self.v * sin(self.a)

    # Attention gérer les autres dudez
    def boidMeet(self):
        pass

    # Sert à détecter si le point est proche d'un mur ou pas
    def boidWallDetected(self,mur):
        x = floor(self.x)
        y = floor(self.y)
        for i in range(- (self.bordure_safe_2-1), self.bordure_safe_2+1):
            for j in range(- (self.bordure_safe_2-1), self.bordure_safe_2+1):
                if( mur.wallHere(x+i,y+j) == True ):
                    return True
        return False


    def boidAvoid(self,Mur):
        if(self.boidWallDetected(Mur) == True):
            self.avoided = True
            self.a = self.a + pi / 2
            self.cpt_avoided = self.cpt_avoided + 1
            if(self.cpt_avoided >= 10):
                self.v = self.v + 0.1
        else:
            self.avoided = False
            self.cpt_avoided = 0
            self.v = self.v_save
        
    # Mise à jour des x et y, et rajout de hasard dans l'orientation
    def boidUpdate(self):
        self.x = self.nouveau_x
        self.y = self.nouveau_y
        if(self.avoided == False):
            if(self.chmgt_angle == 20):
                nouveau_a = (random.uniform(-pi/4,pi/4))
                self.a = self.a + nouveau_a
                self.chmgt_angle = 0
            else:
                self.chmgt_angle = self.chmgt_angle + 1
                nouveau_a = (random.uniform(-pi/32,pi/32))
                self.a = self.a + nouveau_a
        

    # Pour débug
    def boidPrint(self):
        print("x : " + str(self.x) + " & y : " + str(self.y))
        print(" New x : "+ str(self.nouveau_x) +"    New y :" + str(self.nouveau_y))
        print("------------------")

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_nv_x(self):
        return self.get_nv_x

    def get_nv_y(self):
        return self.get_nv_y