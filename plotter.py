import numpy as np
import matplotlib.pyplot as plt

X_Plot = []
Y_Plot = []

X = 0
Y = 0

def next_step(L,S,R):
    straight = False
    right = False
    left = False

    if(S == 100):
        straight = True
    if(R == 100):
        right = True
    if(L == 100):
        left = True
    dir = [left, straight, right]

    if(dir == [True,True,True]):
        return (0,1)
    if(dir == [True, True, False]):
        return (-1,1)
    if(dir == [True, False, True]):
        return (-1,0)
        #return (1,0) #one more possibility move
    if(dir == [False, True, True]):
        return [1,1]
    if(dir == [True, False, False]):
        return [-1,0]
    if(dir == [False, False, True]):
        return [1,0]
    if(dir == [False, True, False]):
        return [0,1]

def move_coord(x, y):
    global X, Y
    X = X + x
    Y = Y + y

def plot_coord():
    X_Plot.append(X)
    Y_Plot.append(Y)

    plt.scatter(X_Plot,Y_Plot)
    plt.show()

while(True):
    L = int(input("Enter Left:"))
    S = int(input("Enter Straight:"))
    R = int(input("Enter Right:"))

    (x,y) = next_step(L,S,R)
    move_coord(x,y)
    plot_coord()






