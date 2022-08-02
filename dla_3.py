#!/usr/bin/python
from random import randint, choice
import random
import numpy as np
import matplotlib.pyplot as plt

class dlaSimulator:
	
	def __init__(self,imageSize,nparticles,stickiness):
		self.imageSize = imageSize
		self.nparticles = nparticles
		self.stickiness = stickiness
		self.imageMat = np.zeros((imageSize,imageSize))
		self.imageMat[int(imageSize/2)][int(imageSize/2)]=1
		return None


	def simulate(self): # returns the image matrix generated after doing dla simulation for given parameters
		k = 0.1 * self.nparticles
		for i in range(self.nparticles):
			currx, curry = self.entryPoint()
			while(self.stickNeighbour(currx,curry)==False):
				if(self.hasBlankSurrounding(currx,curry)):
					currx, curry = self.randomWalk(currx,curry)
				else :
					self.imageMat[currx,curry] = 1
					break
			if(i%k==0):
				print(i)
		return self.imageMat
  

              

	def entryPoint(self): #generates random position on edge for incoming particle to start from
		imgx = self.imageSize
		imgy = self.imageSize
		side = random.randint(0,3)
		if(side == 0):
			xst = 0
			yst = random.randint(0,imgy-1)
		elif(side == 1):
			xst = random.randint(0,imgx-1)
			yst = 0
		elif(side == 2):
			xst = random.randint(0,imgx-1)
			yst = imgy-1
		elif(side == 3):
			xst = imgx-1
			yst = random.randint(0,imgy-1)
		return([xst,yst])

	def hasBlankSurrounding(self,currx,curry): # checks if it has black pixels as a neighbour
		sx = [-1, -1, 0, 1, 1, 1, 0, -1]
		sy = [0, 1, 1, 1, 0, -1, -1, -1]

		for x,y in zip(sx,sy):
			xx = currx + x
			yy = curry + y
			if(0<=xx<self.imageSize and 0<=yy<self.imageSize):
				if(self.imageMat[xx][yy]==0):
					return True
		return False

	def randomWalk(self,currx,curry): # does one step of 2-D random walk 
		sx = [-1, -1, 0, 1, 1, 1, 0, -1]
		sy = [0, 1, 1, 1, 0, -1, -1, -1]
		flag = True
		while(flag):
			p = random.randint(0,7)
			xx = currx + sx[p]
			yy = curry + sy[p]
			if(0<=xx<self.imageSize and 0<=yy<self.imageSize):
				if(self.imageMat[xx][yy]==0):
					flag = False
					currx = xx
					curry = yy
		return([currx,curry])

	def stickNeighbour(self,currx,curry): #checks if it has a white neighbour and if yes then it will stick there with probability = stickiness
		stick = False
		sx = [-1, -1, 0, 1, 1, 1, 0, -1]
		sy = [0, 1, 1, 1, 0, -1, -1, -1]
		for x,y in zip(sx,sy):
			xx = currx + x
			yy = curry + y
			if(0<=xx<self.imageSize and 0<=yy<self.imageSize):
				if(self.imageMat[xx][yy]==1):
					stick = True
					break
		if(stick):
			r = np.random.choice([0,1],p=[1-self.stickiness,self.stickiness])
			if(r==0):
				stick = False
			else :
				self.imageMat[currx][curry]=1

		return stick

        
       
        