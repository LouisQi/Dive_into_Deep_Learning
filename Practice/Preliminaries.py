import torch
import os
import numpy as np

# file_path = 'C:/Users/DELL/OneDrive/桌面/Sung Robotics Lab/Dive_into_Deep_Learning/Practice'
# file_dir = 'Self_made_data'

# os.mkdir(os.path.join(file_path,file_dir),exist_ok =True)
# data_file = os.path.join(file_path,file_dir,'house.csv')
# with open(data_file, 'w') as f:
#     f.write('NumRooms,Alley,Price\n')  
#     f.write('NA,Pave,127500\n')  
#     f.write('2,NA,106000\n')
#     f.write('4,NA,178100\n')
#     f.write('NA,NA,140000\n')
    
# #x = torch.arange(12,dtype=torch.float32).reshape(3,4)
# #x = x.reshape(3,4)

# X = torch.arange(12, dtype=torch.float32).reshape((3,4))
# Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

# a = torch.arange(3).reshape((3, 1))
# b = torch.arange(2).reshape((1, 2))

# Z = torch.zeros_like(Y)
# print(Z)
# print('id(Z):', id(Z))
# Z[:] = X + Y
# print(Z)
# print('id(Z):', id(Z))

# print(X[0:3])
