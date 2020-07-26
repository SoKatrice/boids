from math import cos,sin,pi
import random

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

    def __init__(self,x,y,speed,angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.radian = angle*pi/180

        self.wall_bas = 0
        # self.wall_haut = 760
        self.wall_haut = 100
        self.wall_gauche = 0
        # self.wall_droite = 1130
        self.wall_droite = 100


    def boidBehave(self):
        self.boidMove()

    # Boid se déplace
    def boidMove(self):
        if(self.nextToXWalls()):
            self.angle = 180-self.angle if self.angle<180 else 540-self.angle
            self.radian = self.angle*pi/180
        if(self.nextToYWalls()):
            self.angle = 360-self.angle
            self.radian = self.angle*pi/180
        self.x = round(self.x + self.speed * cos(self.radian),3)
        self.y = round(self.y + self.speed * sin(self.radian),3)
        

    def nextToXWalls(self):
        if(self.x - 5 < self.wall_gauche):
            return True
        if(self.x + 5 > self.wall_droite):
            return True
        return False

    def nextToYWalls(self):
        if(self.y - 5 < self.wall_bas):
            return True
        if(self.y + 5 > self.wall_haut):
            return True
        return False


    # Attention gérer les autres dudez
    def boidMeet(self):
        pass

    # Gestion des frontières : changer d'angle ?
    def boidAvoid(self):
        if(self.x <= (self.wall_bas+self.bordure_safe) or self.x >= (self.wall_haut-self.bordure_safe) or self.y <= (self.wall_gauche+self.bordure_safe) or self.y >= (self.wall_droite-self.bordure_safe)):
            self.avoided = True
            #correction_random = random.uniform(pi/2 - pi/8 ,pi/2 + pi/8 )
            #self.a = self.a + correction_random
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