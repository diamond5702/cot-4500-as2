 import numpy as np

#Problem 1:
  #Solving for f(3.7)
  
x = [3.6,3.8,3.9]

diff = [0.1,-0.1,-0.2]

Q0 = [1.675,1.436,1.318]

Q1 = (1/(x[1]-x[0]))*((diff[0])*(Q0[1]) - (diff[1])*(Q0[0]))


Q2 = (1/(x[2]-x[1]))*((diff[1])*(Q0[2]) - (diff[2])*(Q0[1]))


Q22 = (1/(x[2]-x[0]))*((diff[0])*(Q2) - (diff[2])*(Q1))

print(Q22)
