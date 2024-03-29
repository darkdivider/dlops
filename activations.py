import numpy as np
import matplotlib.pyplot as plt

class activation():
    def __init__(self, x: np.array, activation: str, out: str='print'):
        self.x=x
        y=eval('self.'+activation+'()')
        if out=='print':
            print(y)
        if out=='plt':
            plt.plot(self.x,y)
            plt.axhline(0, color='black')
            plt.axvline(0, color='black')
            if activation in ['tanh', 'sigmoid']:
                plt.axhline(1, color='red')
            if activation=='tanh':
                plt.axhline(-1,color='red')
            plt.title(activation)
            plt.show()
    def sigmoid(self):
        return 1/(1+np.exp(-self.x))
    def relu(self):
        return (self.x+np.abs(self.x))/2
    def leakyrelu(self):
        return self.x*(self.x>0)+self.x*0.01*(self.x<0)
    def tanh(self):
        return np.tanh(self.x)

x=np.linspace(-10,10,100)
activation(x,'leakyrelu','print')