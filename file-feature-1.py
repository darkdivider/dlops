import activations as acts
import numpy as np

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

for activ in ['sigmoid','relu','leakyrelu','tanh'] :
    print(f'Activation = {activ}')
    acts.activation(np.array(random_values),activ,'print') 