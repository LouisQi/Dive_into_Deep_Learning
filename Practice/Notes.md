#### 2.1
```python
import torch

#Baic concept regarding tensor
x = torch.arange(12)
"""
Access the shape of the tensor
1. x.shape --> torch.Size([12])
2. x.numel() --> 12

Reshape the tensor
x.reshape(3,4)

torch.zeros((2,3,4)) 
--> ones
tensor([[[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]],

        [[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]]])
         
torch.randn(3,4) -->standard normal distribution 3 by 4 matrix
"""

#Basic operation regarding tensor
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
x + y, x - y, x * y, x / y, x ** y  # ** power

"""
(tensor([ 3.,  4.,  6., 10.]),
 tensor([-1.,  0.,  2.,  6.]),
 tensor([ 2.,  4.,  8., 16.]),
 tensor([0.5000, 1.0000, 2.0000, 4.0000]),
 tensor([ 1.,  4., 16., 64.]))
"""
#e^x
torch.exp(x)
#tensor([2.7183e+00, 7.3891e+00, 5.4598e+01, 2.9810e+03])

X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)
#dim = 1 has the same effect with dim = -1
"""
(tensor([[ 0.,  1.,  2.,  3.],
         [ 4.,  5.,  6.,  7.],
         [ 8.,  9., 10., 11.],
         [ 2.,  1.,  4.,  3.],
         [ 1.,  2.,  3.,  4.],
         [ 4.,  3.,  2.,  1.]]),
 tensor([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
         [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
         [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]]))
"""

X == Y
X.sum()
"""
tensor([[False,  True, False,  True],
        [False, False, False, False],
        [False, False, False, False]])

tensor(66.)
"""

#Broadcasting mechanism
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
a+b
"""
a duplicates column
--> [0 0
	 1 1
	 2 2]
b duplicates row
--> [0 1
	 0 1
	 0 1]
a+b = [0 1
	   1 2
	   2 3]	 
"""

#Save memory
"""
1. X[:]=X+Y
2. X += Y
Address of X does not change
"""

#Change type
"""
type(X) can access the type of a variable
X.item() can change a tensor to a scalar
"""
```
#### 2.2
```python
```