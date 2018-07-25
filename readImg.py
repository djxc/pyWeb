# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import pandas as pd

def readImg(data):    
    img = cv.imread(data)
    cv.namedWindow("img")
    cv.imshow("img", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def mergeImg(dataPath, outPath):    
    for j in range(5):
        list = []
        for i in range(4):
            name = 'demo%d%d.jpg'  %(j, i)
            img = cv.imread(dataPath + name)
            list.append(img)
        #====使用numpy的数组矩阵合并concatenate======
        #纵向连接
        image = np.vstack((list))
    	#横向连接image = np.concatenate([gray1, gray2], axis=1)
        #image = np.concatenate([img1, img2], axis=1)
        #====使用pandas数据集处理的连接concat========
        
    #    df1 = pd.DataFrame(img1)
    #    
    #    df2 = pd.DataFrame(img2) # ndarray to dataframe
    ##    df = pd.concat([df1, df2])  
    #    #纵向连接,横向连接=pd.concat([df1, df2], axis=1)
    #    df =pd.concat([df1, df2], axis=1)
    #    image = np.array(df) # dataframe to ndarray
    #    
        #=============
        
        #cv.imshow('image', image)
        outname = 'part%d.jpg' % j
        cv.imwrite(outPath + outname, image)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        print(outname + '保存成功')

def mergeImg1(dataPath, outPath):    
    list = []  
    for j in range(2):
        name = 'part%d.jpg' %j
        img = cv.imread(dataPath + name)
        list.append(img)
 
    image = np.concatenate(list, axis=1)
      
        
    #    df1 = pd.DataFrame(img1)
    #    
    #    df2 = pd.DataFrame(img2) # ndarray to dataframe
    ##    df = pd.concat([df1, df2])  
    #    #纵向连接,横向连接=pd.concat([df1, df2], axis=1)
    #    df =pd.concat([df1, df2], axis=1)
    #    image = np.array(df) # dataframe to ndarray
    #    

    outname = 'part%d.jpg' % j
    cv.imwrite(outPath + outname, image)
    print(outname + '保存成功')


if __name__ == "__main__":
    mergeImg1('/home/dj/2018/python/part1/', 'RS/')
#    readImg()
    
