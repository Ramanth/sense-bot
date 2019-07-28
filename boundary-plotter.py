import numpy as np
import matplotlib.pyplot as plt

#Assuming L, S, R will be 100 when there is no obstacle in that respective direction. ie., max-value 100

X_Plot = []
Y_Plot = []

# current location
X = 0
Y = 0

def obstacle_cord(L, S, R):
    global X, Y
    if(L != 100):
        return (X - L/100, Y)
    if(S != 100):
        return (X, Y + S/100)
    if(R != 100):
        return(X + R/100, Y)

def move_coord(x, y):
    global X,Y
    X = X + x
    Y = Y + y

def plot_coord():
    X_Plot.append(X)
    Y_Plot.append(Y)

    plt.scatter(X_Plot,Y_Plot)
    plt.show()

def plot_coord(x,y):
    X_Plot.append(x)
    Y_Plot.append(y)

    plt.scatter(X_Plot,Y_Plot)
    plt.show()

while(True):
    L = int(input("Enter Left:"))
    S = int(input("Enter Straight:"))
    R = int(input("Enter Right:"))

    (x,y) = obstacle_cord(L,S,R)
    #move_coord(x,y)
    plot_coord(x,y)

    X = int(input("Set X:"))
    Y = int(input("Set Y:"))


