import numpy as np
import pygame as pg
import random 

class evni:
    def __init__(self,surface,size):
        self.k_h = [[50,size[1]/2],[50,size[1]/6],[50,size[1]/4],[size[0]-50,size[1]/2],[size[0]-50,size[1]/6],[size[0]-50,size[1]/4]]
        self.surface = surface
        self.size = size
        self.pos_b = [size[0]/2,size[1]]
        self.Vx_b = 0
        self.Vy_b = 0
        self.pos_k = [50,size[1]/2]
        self.direction = -1
        self.ball_img = pg.image.load("ball.png").convert_alpha()
        self.basket_img = pg.image.load("basket.png").convert_alpha()

    def ball(self,trigger,time):
        self.Vy_b += 20*time
        if trigger:
            self.Vy_b = -80
            self.Vx_b = 15*self.direction
        if self.Vx_b != 0 or self.Vy_b != 0:
            self.pos_b[0] += self.Vx_b*time
            self.pos_b[1] += self.Vy_b*time
        if self.pos_b[1] > self.size[1]-20:
            self.Vy_b = -np.absolute(self.Vy_b/1.5)
            self.Vx_b = self.Vx_b/1.5
            self.pos_b[0] += self.Vx_b*time
            self.pos_b[1] = self.size[1]-20
        if self.pos_b[1] < -200:
            self.pos_b[1] = -200
        if self.pos_b[0] > self.size[0]:
            self.pos_b[0] = 0
        if self.pos_b[0] < 0:
            self.pos_b[0] = self.size[0]
        self.surface.blit(self.ball_img,(self.pos_b[0]-25,self.pos_b[1]-25))

    def baskets(self,goal):
        if goal:
            self.pos_k = random.choice(self.k_h)
            if self.pos_k[0] == 50:
                self.direction = -1
            else:
                self.direction = 1
        self.surface.blit(self.basket_img,(self.pos_k[0]-40,self.pos_k[1]-5,40,5))

