from scipy import optimize as opt
from scipy.spatial import ConvexHull as hull
import numpy as np
import matplotlib.pyplot as plt


def D_pot(f1, f2, t1, t2):
    dx = abs(np.sin(t1)*np.cos(f1) - np.sin(t2)*np.cos(f2))
    dy = abs(np.sin(t1)*np.sin(f1) - np.sin(t2)*np.sin(f2))
    dz = abs(np.cos(t1) - np.cos(t2))
    return 1 / (dx ** 2 + dy ** 2 + dz ** 2) ** (0.5)

def multipot(l, N):
    E = 0
    for i in range(N):
        for j in range(i+1, N):
                       E += D_pot(l[i], l[j], l[i+N], l[j+N])
    return E

def to_cart(l, N):
    a = np.zeros((N, 3))
    for i in range(N):
        a[i][0] = np.cos(l[i]) * np.sin(l[N+i])
        a[i][1] = np.sin(l[i]) * np.sin(l[N+i])
        a[i][2] =np.cos(l[N+i])
    return a