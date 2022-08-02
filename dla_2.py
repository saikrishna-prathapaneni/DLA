import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from PIL import Image
import logging

class DLA:
    
    def __init__(self,stickiness=0.01,size=251):
       
        self.stickiness =stickiness
        self.size=size
        self.matrix=np.ones([self.size,self.size],dtype=int)
        self.matrix[int(self.size/2),int(self.size/2)]=0
        self.edges = {'left':[0,random.randint(0,self.size-1)],'right':[self.size-1,random.randint(0,self.size-1)]
                       ,'up':[random.randint(0,self.size-1),self.size-1],'down':[random.randint(0,self.size-1),0]}
        self.present_loc=[]
        
        
    def print_matrix(self):
        print(self.matrix)
        
    def get_ones(self):
        print("ones count =>", np.where(self.matrix==1)[0].shape[0])

    
    def show_matrix(self):
        plt.figure(figsize=(30, 25))
        name='images/test_test'+str(time.time())+'.jpg' #str(time.time())
        plt.imsave(name, self.matrix.astype('uint8'), 
                               cmap=matplotlib.cm.gray,vmin=0, vmax=1)
        plt.close()
        
        
        
    def get_states(self,x,y):
        locs=[(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
        status = False
        if x<self.size-1 and y<self.size-1:
            for lo in locs:
                try:
                    if self.matrix[lo[0],lo[1]] == 0:
                            status= True
                            break
                except Exception:
                    pass
            if status:
                r = np.random.choice([1,0],p=[1-self.stickiness,self.stickiness])
                print(r)
                if r==0:
                    status = False
            

        return status
        

    
    def select_random_move(self,x,y):
        
        self.present_loc = [x,y]
        self.matrix[x,y]=0
        
        while True:  
            try: 
                if self.get_states(self.present_loc[0],self.present_loc[1]):
                    print("end")
                    
                    break
                x_loc=self.present_loc[0]
                y_loc=self.present_loc[1]
                
         
                locs=[(x_loc-1,y_loc-1),(x_loc+1,y_loc-1),
                         (x_loc+1,y_loc+1),(x_loc-1,y_loc)
                         ,(x_loc+1,y_loc),(x_loc,y_loc+1),
                         (x_loc-1,y_loc+1),(x_loc,y_loc-1)]
               
                random_direction = random.choice(locs)
                
                self.introduce_element(0,random_direction[0],random_direction[1])
                self.matrix[self.present_loc[0],self.present_loc[1]] = 1
                # if random_direction[0] <0:
                #     self.present_loc[0] = self.size-1
                #     self.present_loc[1] = random_direction[1]
                # elif random_direction[0] >self.size-1:
                #     self.present_loc[0] = 0
                #     self.present_loc[1] = random_direction[1]
                # elif random_direction[1] >self.size-1:
                #     self.present_loc[1] = 0
                #     self.present_loc[0] = random_direction[0]
                # elif random_direction[1]<0:
                #     self.present_loc[1] =self.size-1
                #     self.present_loc[0] = random_direction[0]
                # else:
                    
                self.present_loc=[random_direction[0],random_direction[1]]
               # print(self.present_loc)
               
            except Exception:
                
                pass

        
    def get_random_Edge(self):
        
        
        return random.choice(list(self.edges.values()))
    
    def introduce_element(self,element,x,y):
        
        self.matrix[x,y]=element
        
    def move(self,points=100):
        i=0
        try:
            for _ in range(points):
          
                self.select_random_move(self.get_random_Edge()[0],self.get_random_Edge()[1]) 
                i=i+1
                print(i)
                #self.show_matrix() 
        except Exception:
            pass
        self.show_matrix() 
             
            

 