'''
Author: liboyu
Date: 2021-11-24 10:58:57
LastEditTime: 2021-11-24 13:15:17
LastEditors: newsun-HP-Pavilion-Gaming-Laptop-15-dk0xxx
Description: In User Settings Edit
FilePath: /2022task6/simu.py
'''
height = 1080
width= 720

import numpy as np
import cv2
import random as rd
class Ball:
    def __init__(self):
        self.v = np.array([0,0],dtype=np.int64) #定义球的速度
        self.v_now = np.array([0,0],dtype=np.int64) #定义球的速度
        self.alpha = 5#速度系数
        self.p = np.array([width/2,height/2])
        l = []
        for i in range(50):#定义惯性系数
            l.append([rd.random(),rd.random()])
        self.past_vs = np.array(l,dtype=np.int64)
        
    def update_v(self):
        self.v_now[0] = (rd.random()-0.5) * 10
        self.v_now[1] = (rd.random()-0.5) * 10
        self.past_vs = np.roll(self.past_vs,1,axis = 0)
        
        self.past_vs[0] = self.v_now
        self.v = np.mean(self.past_vs,axis=0)

    def move(self):
        self.update_v()
        self.p = self.p + self.alpha * self.v
        
    

ball = Ball()



while True:
    background = np.zeros((width, height, 3), dtype = "uint8")
    cv2.circle(background,(round(ball.p[0])%height,round(ball.p[1])%width),20,(0,0,255),-1)
    # print(ball.p[0])
    # print(ball.p[1])
    cv2.imshow("a",background)
    ball.move()
    cv2.waitKey(10) 