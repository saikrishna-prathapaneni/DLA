import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image

class DLA:
    
    def __init__(self,stickiness=0.1,size=251):
       
        self.stickiness =stickiness
        self.size=size
        self.matrix=np.zeros([self.size,self.size],dtype=int)
        self.matrix[int(self.size/2),int(self.size/2)]=1
        #self.edges = {'left':self.matrix[:,0],'right':self.matrix[:,size-1],'up':self.matrix[0,:],'down':self.matrix[size-1,:]}
        self.edges = {'left':[0,0],'right':[0,self.size-1],'up':[self.size-1,0],'down':[self.size-1,self.size-1]}
        self.present_loc=[]
        
        
    def print_matrix(self):
        print(self.matrix)
        
    def get_ones(self):
        print("ones count =>", np.where(self.matrix==1)[0].shape[0])

    
    def show_matrix(self):
        fig = plt.figure()
        plt.figure(figsize=(30, 25))
        plt.imsave('test.jpg', self.matrix.astype('uint8'), 
                               cmap=matplotlib.cm.gray,vmin=0, vmax=1)
        plt.close(fig)
        
        
        
    def get_states(self,x,y):
        locs=[(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
        
        status = False
        for lo in locs:
            try:
                if self.matrix[lo[0],lo[1]] == 1:
                    status= True
                    break
            except Exception:
                pass
        
        return status
    
    def select_random_move(self,x,y):
        
   
        
        self.present_loc = [x,y]
        self.matrix[x,y]=1
        
        while True:  
            try: 
                if self.get_states(self.present_loc[0],self.present_loc[1]):
                    print(self.get_states(self.present_loc[0],self.present_loc[1]))
                    print("end")
                    break
                if x==0 and y==0:
                    locs=[(x+1,y+1),(x,y+1),(x+1,y)]
                elif x==0 and y !=0:
                    locs = [(x+1,y+1),(x+1,y-1),(x,y-1),(x,y+1),(x+1,y)]
                elif x != 0 and y==0:
                    locs = [(x+1,y+1),(x-1,y+1),(x,y+1),(x+1,y),(x-1,y)]
                else:
                    locs=[(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
                # if self.present_loc[0]==0:
                #     random_direction = random.choice(locs)
                # else:
                random_direction = random.choice(locs)
                self.introduce_element(1,random_direction[0],random_direction[1])
                self.matrix[self.present_loc[0],self.present_loc[1]] = 0
                self.present_loc=[random_direction[0],random_direction[1]]
                print(self.present_loc)
               
            except Exception:
                print("passed")
        print("\n================================")
           
       
       
        # if self.get_states(x,y):
        #     pass
        # else:
        #     self.introduce_element(1,random_direction[0],random_direction[1])
        #     self.present_loc=[random_direction[0],random_direction[1]]
        #     self.matrix[x,y]= 0
            
        
    def get_random_Edge(self):
        return random.choice(list(self.edges.values()))
    
    def introduce_element(self,element,x,y):
        
        self.matrix[x,y]=element
        
    def move(self,points=100):
        for _ in range(points):
             self.select_random_move(self.get_random_Edge()[0],self.get_random_Edge()[1]) 


if __name__ == '__main__':
    obj=DLA(size=6)
    
    #obj.get_ones()
    #print(obj.get_states(125,126))
    
    obj.move(6)
    obj.show_matrix()
    # image = Image.open('test.jpg')
    # image.show()
    