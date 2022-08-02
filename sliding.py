import numpy as np 
import matplotlib.pyplot as plt
import matplotlib

class slidingWindow:
    def __init__(self,matrix,window_size=[3,3],stride=10):
        
        self.window_size = window_size
        self.matrix= matrix
        self.sliding_matrix=None
        self.sliding_length = stride
        self.output_ones_zeros=[]
        self.ones=[]
    
    def show_matrix(self):
        plt.figure(figsize=(30, 25))
        name='test_test'+'.jpg' #str(time.time())
        plt.imsave(name, self.ones, 
                               cmap=matplotlib.cm.gray,vmin=0, vmax=1)
        plt.close()    
    
    def output_matrix(self):
        output=[]
        ones=[]
        for i in range(self.matrix.shape[0]-self.sliding_length+1):
            for k in range(self.matrix.shape[1]-self.sliding_length+1):
                value = self.matrix[i:i+self.sliding_length,k:k+self.sliding_length]
                output.append([(np.where(value==1)[0].shape[0],np.where(value==0)[0].shape[0])])
                
                ones.append(output)
                
                ones.append(np.where(value==1)[0].shape[0])
        self.output_ones_zeros=output
        self.ones=ones
        
  
        return ones,output