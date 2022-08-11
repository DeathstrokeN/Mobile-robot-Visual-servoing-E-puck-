#Author: andrea cherubini cherubini@lirmm.fr
#Script for selecting 12 or 127 pixels by clicking on an image of a calibration cube
#Input: an image of the cube with 3 sides appearing and 36 black and white squares on each side
#Output: uv_xyz.dat file pairing the pixel coordinates to their metric position in the cube reference frame 
#Options:replace manual selection with predefined list associated to imageTestCube.jpg and use 127 instead of 12 points

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#flag for replacing manual selection by a predefined list of pixels associated to imageTestCube.jpg
def click():
    return True
#flag for working with 127 instead of 12 pixels
def manyPoints():
    return False
#load and display the image
plt.imshow(mpimg.imread('imageTestCube.jpg'))
matplotlib.use('TkAgg')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
if click(): 
    if manyPoints():
        npts_cal=127;
    else:
        npts_cal=12;
    #click on pixels and store their coordinates
    uv = np.asarray(plt.ginput(npts_cal, timeout=-1))
    print(uv)
else:      
    if manyPoints():
        #load default pixel coordinates
        u = np.array([[
            109, 126, 144, 162, 181, 202, 222, 100, 115, 133, 152, 170, 190, 
            211, 87, 103, 123, 139, 160, 181, 201, 77, 93, 111, 130, 148, 169, 
            189, 64, 80, 99, 115, 138, 160, 180, 53, 68, 86, 105, 124, 145, 
            166, 41, 56, 74, 94, 113,133,156,51,65,81,99,118,140,161,58,73,89,
            108,127,147,167,67,82,98,115,136,155,177,75,89,108,126,144,163,183,
            84,98,114,132,150,171,188,92,105,122,138,157,175,197,177,188,199,
            210, 219, 230, 183, 193, 207, 215, 224, 232, 189, 199, 209, 220, 
            228, 239, 194, 207, 217, 225, 235, 242, 201, 211, 220, 229, 238, 
            246, 207, 214, 222, 232, 241, 250]])
        v = np.array([[
            4, 7, 10, 12, 13, 16, 20, 18, 20, 22, 24, 27, 31, 34, 31, 34, 37, 
            40, 44, 45, 48, 46, 48, 51, 54, 58, 62, 66, 63, 64, 66, 70, 75, 
            78, 83, 78, 79, 83, 87, 92, 96, 101, 95, 100, 100, 106, 111, 117,
            121, 115, 115, 119, 124, 129, 133, 135, 128, 131, 134, 139, 144, 
            149, 152, 143, 146, 150, 156, 160, 166, 169, 157, 161, 165, 169,
            175, 179, 185, 170, 175, 178, 182, 189, 194, 199, 182, 186, 189, 
            195, 201, 205, 212, 118, 100, 83, 66, 50, 35, 135, 118, 98, 84, 
            68, 53, 150, 133, 117, 101, 83, 70, 166, 147, 132, 116, 101, 85, 
            179, 163, 147, 131, 115, 101, 192, 175, 159, 143, 127, 113]]);
    else:
        u = np.array([[64, 139, 171, 99, 177, 222, 240, 202, 145, 69, 116, 192]]);
        v = np.array([[118, 135, 195, 175, 120, 52, 114, 183, 96, 82, 23, 33]]);
    uv = np.concatenate((np.transpose(u), np.transpose(v)), axis=1)
#set metric positions of the pixels in the cube reference frame
if manyPoints():
    xyz=np.array([
          [6,0,6],[6,0,5],[6,0,4],[6,0,3],[6,0,2],[6,0,1],[6,0,0],[5,0,6],
          [5,0,5],[5,0,4],[5,0,3],[5,0,2],[5,0,1],[5,0,0],[4,0,6],[4,0,5],
          [4,0,4],[4,0,3],[4,0,2],[4,0,1],[4,0,0],[3,0,6],[3,0,5],[3,0,4],
          [3,0,3],[3,0,2],[3,0,1],[3,0,0],[2,0,6],[2,0,5],[2,0,4],[2,0,3],
          [2,0,2],[2,0,1],[2,0,0],[1,0,6],[1,0,5],[1,0,4],[1,0,3],[1,0,2],
          [1,0,1],[1,0,0],[0,0,6],[0,0,5],[0,0,4],[0,0,3],[0,0,2],[0,0,1],
          [0,0,0],[0,1,6],[0,1,5],[0,1,4],[0,1,3],[0,1,2],[0,1,1],[0,1,0],
          [0,2,6],[0,2,5],[0,2,4],[0,2,3],[0,2,2],[0,2,1],[0,2,0],[0,3,6],
          [0,3,5],[0,3,4],[0,3,3],[0,3,2],[0,3,1],[0,3,0],[0,4,6],[0,4,5],
          [0,4,4],[0,4,3],[0,4,2],[0,4,1],[0,4,0],[0,5,6],[0,5,5],[0,5,4],
          [0,5,3],[0,5,2],[0,5,1],[0,5,0],[0,6,6],[0,6,5],[0,6,4],[0,6,3],
          [0,6,2],[0,6,1],[0,6,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],
          [6,1,0],[1,2,0],[2,2,0],[3,2,0],[4,2,0],[5,2,0],[6,2,0],[1,3,0],
          [2,3,0],[3,3,0],[4,3,0],[5,3,0],[6,3,0],[1,4,0],[2,4,0],[3,4,0],
          [4,4,0],[5,4,0],[6,4,0],[1,5,0],[2,5,0],[3,5,0],[4,5,0],[5,5,0],
          [6,5,0],[1,6,0],[2,6,0],[3,6,0],[4,6,0],[5,6,0],[6,6,0]])*1e-2;
else:
    xyz=np.array([[0,1,5],[0,1,1],[0,5,1],[0,5,5],[1,1,0],[5,1,0],[5,5,0],[1,5,0],
         [1,0,1],[1,0,5],[5,0,5],[5,0,1]])*1e-2;
#write values (pixel coordinates followed by metric coordinates) in a file
uv_xyz=np.concatenate((uv, xyz), axis=1)
mat = np.matrix(uv_xyz)
with open('uv_xyz.dat','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')
