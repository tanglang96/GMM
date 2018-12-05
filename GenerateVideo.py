import cv2 as cv
import numpy as np
import glob as glob

left_list=glob.glob(r'./WavingTrees/b*.bmp')
right_list=glob.glob(r'./output/*.bmp')
file_index=0
VW=cv.VideoWriter('test.avi',cv.VideoWriter_fourcc(*'MJPG'),25,(320,120))
for i in range(len(left_list)):
    print(left_list[i])
    print(right_list[i])
    result=np.concatenate((cv.imread(left_list[i]),cv.imread(right_list[i])),axis=1)
    cv.imwrite(r'./video/'+'%05d'%file_index+'.bmp',result)
    VW.write(result)
    file_index+=1


