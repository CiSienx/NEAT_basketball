import tensorflow as tf
import numpy as np
import random

class bot:
    def __init__(self):
        self.model = tf.keras.Sequential()
        self.model.add(tf.keras.layers.Dense(2,activation=tf.nn.relu))
        self.model.add(tf.keras.layers.Dense(4,activation=tf.nn.relu))
        self.model.add(tf.keras.layers.Dense(4,activation=tf.nn.relu))
        self.model.add(tf.keras.layers.Dense(1,activation=tf.nn.relu))
        self.model.compile(optimizer='adam',loss='mse',metrics=['accuracy'])

    def train(self,xb,yb):
        inputlayer = np.asarray([xb,yb])
        output = self.model.predict(inputlayer)
        if output[0] <= 0.5:
            output = 0
        else :
            output = 1
        return output

class genepool:
    def __init__(self):
        self.bot1 = bot()
        self.bot2 = bot()
        self.bot3 = bot()
        self.bot4 = bot()
        self.bot5 = bot()
        self.bot6 = bot()
        self.bot7 = bot()
        self.bot8 = bot()
        self.bot9 = bot()
        self.bot10 = bot()
        self.bot_list = [self.bot1,self.bot2,self.bot3,self.bot4,self.bot5,self.bot6,self.bot7,self.bot8,self.bot9,self.bot10]

    def train(self,T,xb,yb):
        out = self.bot_list[T-1].train(xb,yb)
        return out

    def cross(self,score,c1,c2):
        scoreS = sorted(score,reverse=True)
        parent1 = self.bot_list[score.index(scoreS[0])]
        parent2 = self.bot_list[score.index(scoreS[1])]
        pw1 = parent1.model.get_weights()
        pw2 = parent2.model.get_weights()
        pwn1 = pw1
        pwn2 = pw2
        i = random.randint(0,len(pw1)-1)
        j = random.randint(0,len(pw1[i])-1)
        pwn1[i][j] = pw2[i][j]
        pwn2[i][j] = pw1[i][j]
        self.bot_list[c1].model.set_weights(pwn1)
        self.bot_list[c2].model.set_weights(pwn2)
    
    def crossover(self,score):
        print("bot reportcard ")
        scoreS = sorted(score,reverse=True)
        print(scoreS)
        if scoreS[0] > 0:
            self.bot_list[score.index(scoreS[len(scoreS)-1])].model.set_weights(self.bot_list[score.index(scoreS[0])].model.get_weights())
            self.bot_list[score.index(scoreS[len(scoreS)-2])].model.set_weights(self.bot_list[score.index(scoreS[0])].model.get_weights())
            self.cross(score,0,1)
            self.cross(score,2,3)    
            self.cross(score,3,4) 
            self.cross(score,5,6) 
            self.cross(score,7,8)
    
    def mutation(self,score):
        scoreS = sorted(score,reverse=True)
        if scoreS[0] > 0:
            print("bots are mutating 0.15")
            for bot in self.bot_list:
                weights = bot.model.get_weights()
                for i in range(len(weights)):
                    for j in range(len(weights[i])):
                        if random.uniform(0,1) > 0.90:
                            weights[i][j] += random.uniform(-0.5,0.5)
                bot.model.set_weights(weights)
        else:
            print("bots are mutating 0.5")
            for bot in self.bot_list:
                weights = bot.model.get_weights()
                for i in range(len(weights)):
                    for j in range(len(weights[i])):
                        if random.uniform(0,1) > 0.5:
                            weights[i][j] += random.uniform(-0.5,0.5)
                bot.model.set_weights(weights)