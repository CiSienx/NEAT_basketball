import pygame as pg 
from objects import evni
import time
from AI import bot, genepool
import numpy as np

family_bot = genepool()
size = (500,600)
screen = pg.display.set_mode((size))
room = evni(screen,(500,500))
trigger = False

def control():
    global trigger
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        if event.type == pg.MOUSEBUTTONDOWN:
            #trigger = True
            pass

def main():
    pg.init()
    time = 0.5
    global trigger
    score = 0
    combo = 6
    Train_no = 1
    gen_no = 0
    bot_score_list = []
    while True:
        goal = False
        trigger = False
        control()
        if int(combo) == 0:
            print(score)
            bot_score_list.append(score)
            score = 0
            gameoverT = pg.font.SysFont("monospace",32).render("GameOver",1,(250,10,10))
            screen.blit(gameoverT,(size[0]/3,size[1]/3))
            playagainT = pg.font.SysFont("monospace",32).render("PlayAgain?",1,(250,10,10))
            screen.blit(playagainT,(size[0]/3,size[1]/2))
            room.pos_b = [size[0]/2,size[1]]
            Train_no += 1
            combo = 6
            if Train_no > 10:
                family_bot.crossover(bot_score_list)
                family_bot.mutation(bot_score_list)
                bot_score_list = []
                Train_no = 1
                gen_no += 1

        else:
            X = (room.pos_b[0]-room.pos_k[0])/100
            Y = (room.pos_b[1]-room.pos_k[1])/100
            out = family_bot.train(Train_no,X,Y)
            if out == 1:
                trigger = True
            combo -= time/10
            screen.fill((200,200,200))
            pg.draw.line(screen,(0,0,0),(0,size[1]-200),(size[0],size[1]-200),width=5)
            pg.draw.rect(screen,(150,150,150),(0,size[1]-200,size[0],size[1]))
            room.ball(trigger,time)
            if room.pos_k[1] > room.pos_b[1] - 10 and room.pos_k[1] < room.pos_b[1] + 10 and room.pos_k[0] > room.pos_b[0] - 40 and room.pos_k[0] < room.pos_b[0] + 50:
                goal = True
                score += 10
                combo = 6
            room.baskets(goal)
            scoretext = pg.font.SysFont("monospace",32).render("Score :"+str(score),1,(250,10,10))
            screen.blit(scoretext,(0,0))
            bot_on = pg.font.SysFont("monospace",20).render("Bot number :"+str(Train_no),1,(0,100,0))
            screen.blit(bot_on,(size[0]-330,0))
            gen_on = pg.font.SysFont("monospace",20).render("Generation number :"+str(gen_no),1,(0,100,0))
            screen.blit(gen_on,(size[0]-330,30))
            comboT = pg.font.SysFont("monospace",20).render("Count :"+str(int(combo)),1,(250,10,10))
            screen.blit(comboT,(size[0]-150,0))
        pg.display.flip()

if __name__ == "__main__":
    main()