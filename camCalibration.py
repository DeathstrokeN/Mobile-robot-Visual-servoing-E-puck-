#Author: andrea cherubini cherubini@lirmm.fr
#Script for calibrating e-puck camera given uv_xyz.dat file pairing the pixel 
#coordinates to their metric position in the calibration cube reference frame
#Input: the uv_xyz.dat file
#Output:  
#Options:

import numpy as np
import math  as m

#load file to a matrix 
dataMat = np.loadtxt("uv_xyz.dat")
u=dataMat[:,0]
v=dataMat[:,1]
x=dataMat[:,2]
y=dataMat[:,3]
z=dataMat[:,4]
nPixels=np.size(z);

#fill A and B matrices for least square estimation and solve Ax= b*
A=np.zeros((2*nPixels, 11))
b=np.zeros((2*nPixels, 1))
for i in range(0, nPixels):
    A[i,:]=[0,0,0,0,0,0,0,0,0,0,0];#TODO
    b[i,:]=1;#TODO
print(A)
print(b)
X=np.linalg.pinv(A)@b;
Xt=np.concatenate((np.transpose(X),np.ones((1,1))), axis=1)
#design C and extract its three lines
C=np.concatenate((Xt[:,0:4], Xt[:,4:8],Xt[:,8:12]), axis=0)
print(C)
c1=C[0,:3]
c2=C[1,:3]
c3=C[2,:3]
#compute scale factor lambda (noted L here)
L=1#TODO
print(L)
#compute intrinsic parameters
uo=1#TODO
vo=1#TODO
print(uo)
print(vo)
alpha_u=1#TODO
alpha_v=1#TODO
print(alpha_u)
print(alpha_v)
#compute extrinsic parameters
r1= [[2, 0, 0]]#TODO
r2= [[0, 2, 0]]#TODO
r1n=(r1/np.linalg.norm(r1)).reshape(1,3)
r2n=(r2/np.linalg.norm(r2)).reshape(1,3)
r3=[[0, 0, 1]]#TODO
R=np.concatenate((r1n,r2n,r3), axis=0)
print(R)
px=.001#TODO
py=.001#TODO
pz=.25#TODO
p=np.array([[px],[py],[pz]])
print(p)

#display camera and cube frames
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

if __name__ == '__main__':
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.set_xlabel('X')
    ax1.set_xlim(-.5, .5)
    ax1.set_ylabel('Y')
    ax1.set_ylim(0, 1)
    ax1.set_zlabel('Z')
    ax1.set_zlim(-.5, .5)

#camera frame in pyplot frame
O_cam = (0, 0, 0)
X_cam = (1, 0, 0)
Y_cam = (0, 0, -1)
Z_cam = (0, 1, 0)
arrow_prop_dict = dict(mutation_scale=20, arrowstyle='->', shrinkA=0, shrinkB=0)
a = Arrow3D([O_cam[0], X_cam[0]], [O_cam[1], X_cam[1]], [O_cam[2], X_cam[2]], **arrow_prop_dict, color='r')
ax1.add_artist(a)
a = Arrow3D([O_cam[0], Y_cam[0]], [O_cam[1], Y_cam[1]], [O_cam[2], Y_cam[2]], **arrow_prop_dict, color='g')
ax1.add_artist(a)
a = Arrow3D([O_cam[0], Z_cam[0]], [O_cam[1], Z_cam[1]], [O_cam[2], Z_cam[2]], **arrow_prop_dict, color='b')
ax1.add_artist(a)
ax1.text(-0.1, 0, 0, r'$C$')

#object (cube) frame (transformed wrt pyplot frame)
R_pypCam = np.array([[1, 0, 0],[0, 0, 1],[0, -1, 0]])
O_wor = R_pypCam @ p;
X_wor = R_pypCam @ (p + R[:,[0]]);
Y_wor = R_pypCam @ (p + R[:,[1]]);
Z_wor = R_pypCam @ (p + R[:,[2]]);
a = Arrow3D([O_wor[0][0], X_wor[0][0]], [O_wor[1][0], X_wor[1][0]], [O_wor[2][0], X_wor[2][0]], **arrow_prop_dict, color='r')
ax1.add_artist(a)
a = Arrow3D([O_wor[0][0], Y_wor[0][0]], [O_wor[1][0], Y_wor[1][0]], [O_wor[2][0], Y_wor[2][0]], **arrow_prop_dict, color='g')
ax1.add_artist(a)
a = Arrow3D([O_wor[0][0], Z_wor[0][0]], [O_wor[1][0], Z_wor[1][0]], [O_wor[2][0], Z_wor[2][0]], **arrow_prop_dict, color='b')
ax1.add_artist(a)
ax1.text(0, 0, 0.1, r'$W$')
plt.show()