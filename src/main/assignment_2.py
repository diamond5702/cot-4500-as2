import numpy as np

np.set_printoptions(precision=7, suppress=True, linewidth=100)


#Problem 1:
  #Solving for f(3.7)
x = [3.6,3.8,3.9]

diff = [0.1,-0.1,-0.2]

Q0 = [1.675,1.436,1.318]

Q1 = (1/(x[1]-x[0]))*((diff[0])*(Q0[1]) - (diff[1])*(Q0[0]))


Q2 = (1/(x[2]-x[1]))*((diff[1])*(Q0[2]) - (diff[2])*(Q0[1]))


Q22 = (1/(x[2]-x[0]))*((diff[0])*(Q2) - (diff[2])*(Q1))

print(Q22, "\n\n")

#Problem 2:
    #Find 1st, 2nd, 3rd degree Polynomials.
x=[7.2, 7.4, 7.5, 7.6]

y= [23.5492, 25.3913, 26.8224, 27.4589]

firstdd1= (y[1] - y[0])/ (x[1] - x[0])
firstdd2= (y[2] - y[1])/ (x[2] - x[1])
firstdd3= seconddd1= (y[3] - y[2])/ (x[3] - x[2])

second_dd1= (firstdd2- firstdd1) / (x[2]-x[0])
second_dd2= (firstdd3- firstdd2) / (x[3]-x[1])

third_dd = (second_dd2 - second_dd1) / (x[3] - x[0])
print(firstdd1,"\n", second_dd1,"\n", third_dd,"\n")


#Problem 3:
    #Approximate f(7.3)
w= 7.3

p1= y[0] + (( w - x[0])*(firstdd1))

p2= p1 + ((w - x[0])*(w - x[1])*(second_dd1))

p3= p2 + ((w - x[0])*(w - x[1])*(w - x[2])*(third_dd))

print (p3, "\n")

#Problem 4:

#Problem 5:

