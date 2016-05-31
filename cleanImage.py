#!/usr/bin/python
# -*- coding:utf-8 -*-

from skimage import io, data
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import copy
import datetime
import time
import os
import threading
import random
from os.path import isfile, join 


dataPath = '/home/wh//script/dataset/'
width = 2

class pixel(object):
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, count):
        self.count += 1

    def __eq__(self, obj):
        if self.r == obj.r and self.g == obj.g and self.b == obj.b:
            return True
        else:
            return False





def filterImg(target_path, plain_path):

    # 抽取降水区域
    plain = io.imread(plain_path)
    target = io.imread(target_path)
    target = target[0:480, 0:480, :]
    for i in xrange(target.shape[0]):
        for j in xrange(target.shape[1]):
            flag = True
            for k in xrange(target.shape[2]):
                if target[i,j,k] != plain[i,j,k]:
                   flag = False
                   break
            if flag:
                target[i,j,0] = target[i,j,1] = target[i,j,2] = 255

    # 填充空白处
    for i in xrange(width, target.shape[0]-width):
        for j in xrange(width, target.shape[1]-width):
            if np.equal(target[i, j], [255, 255, 255]).all():
                tmp = []
                for m in xrange(i-width, i+width+1):
                    for n in xrange(j-width, j+width+1):
                        t=copy.deepcopy(target[m,n])
                        tmp.append(pixel(target[m,n,0], target[m,n,1], target[m,n,2]))
                        # tmp.append(t)
                c=max(tmp, key=tmp.count)
                target[i,j,0] = c.r
                target[i,j,1] = c.g
                target[i,j,2] = c.b

    io.imsave('/home/wh/script/filter/'+ str(random.randint(100000, 999999)) + '.gif', target)

# io.imsave('/home/wh/code/python/data/extract.gif', plain)
    # plt.imshow(target)
    # plt.show()



if __name__ == '__main__':

    start = time.clock()

    # 提取目录列表
    lists = os.listdir(dataPath)
    dirs = []
    for d in lists:
        if not isfile(join(dataPath, d)):
            dirs.append(d)
    # print(dirs)

    # 提取图像文件
    for d in dirs:
        dirPath = dataPath + str(d)
        lists = os.listdir(dirPath)
        imgs = []
        for i in lists:
            imgs.append(i)

        # 为每张图像创建一个线程
        threads = []
        for img in imgs[:100]:
            imgPath = dataPath + str(d) + '/' + str(img)
            tarPath = dataPath + 'hefei.gif'
            # print(imgPath, tarPath)

            # print(imgPath)
            t = threading.Thread(target=filterImg, args=(imgPath, tarPath))
            threads.append(t)
        
        # print(len(threads))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        print("all done")
    
    finish = time.clock()
    print(finish - start)
    




# img = io.imread('/home/wh/code/python/data/extract.gif')
# io.imsave('/home/wh/code/python/data/extract.jpg', img)

# -----------------------------------------------------------
# cut original images and extract rainfall area 
# -----------------------------------------------------------
# img = io.imread('/home/wh/code/python/data/RADA_CHN_DOR_L3_ST_NOC-OHP-Z9200-20160419025000.GIF')
# cut = img[0:480, 0:480 :]
# io.imsave('/home/wh/code/python/data/1.gif', cut)

# img = io.imread('/home/wh/code/python/data/RADA_CHN_DOR_L3_ST_NOC-OHP-Z9200-20160506075500.gif')
# cut = img[0:480, 0:480 :]
# io.imsave('/home/wh/code/python/data/2.gif', cut)

# img1 = io.imread('/home/wh/code/python/data/1.gif')
# img2 = io.imread('/home/wh/code/python/data/2.gif')

# # print(img1.shape)
# # print(img2.shape)

# for i in xrange(img1.shape[0]):
#     for j in xrange(img1.shape[1]):
#         flag = True
#         for k in xrange(img1.shape[2]):
#             if img1[i,j,k] != img2[i,j,k]:
#                flag = False
#                break
#         if flag:
#             img2[i,j,0] = img2[i,j,1] = img2[i,j,2] = 255

# io.imsave('/home/wh/code/python/data/extract.gif', img2)

# plt.imshow(img1)
# plt.imshow(img2)
# plt.show()
# cv2.imshow("1",img)
# cv2.imshow("2",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# -----------------------------------------------------------
# inpaint image
# -----------------------------------------------------------
# img1 = io.imread('/home/wh/code/python/data/1.gif')
# img2 = io.imread('/home/wh/code/python/data/2.gif')
# img3 = io.imread('/home/wh/code/python/data/extract.gif')

# class pixel(object):
    
#     def __init__(self, r, g, b):
#         self.r = r
#         self.g = g
#         self.b = b

#     def __add__(self, count):
#         self.count += 1

#     def __eq__(self, obj):
#         if self.r == obj.r and self.g == obj.g and self.b == obj.b:
#             return True
#         else:
#             return False


# width =2

# # tmp=[]
# # tmp.append(img3[0,0])
# # print type(tmp[0])
# # print type(img3[0,0])

# for i in xrange(width, img3.shape[0]-width):
#     for j in xrange(width, img3.shape[1]-width):
#         if np.equal(img3[i, j], [255, 255, 255]).all():
#             tmp = []
#             for m in xrange(i-width, i+width+1):
#                 for n in xrange(j-width, j+width+1):
#                     t=copy.deepcopy(img3[m,n])
#                     tmp.append(pixel(img3[m,n,0], img3[m,n,1], img3[m,n,2]))
#                     # tmp.append(t)
#             c=max(tmp, key=tmp.count)
#             img3[i,j,0] = c.r
#             img3[i,j,1] = c.g
#             img3[i,j,2] = c.b

# io.imsave('/home/wh/code/python/data/3.gif', img3)
# plt.imshow(img3)
# plt.show()

# -----------------------------------------------------------
# -----------------------------------------------------------

# img1 = io.imread('/home/wh/code/python/data/extract.gif')
# img2 = io.imread('/home/wh/code/python/data/2.gif')
# io.imsave('/home/wh/code/python/data/extract.jpg',img1)
# io.imsave('/home/wh/code/python/data/2.jpg',img2)

# -----------------------------------------------------------
# -----------------------------------------------------------

# im = cv2.imread('/home/wh/code/python/data/extract.jpg')
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
# im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# mask = np.zeros(im.shape)
# mask = mask.astype('uint8')

# cv2.drawContours(mask, contours, -1, (255,255,255), 1)

# grey_mask = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)
# dst = cv2.inpaint(im, grey_mask, 1, cv2.INPAINT_TELEA)

# # plt.figure(num='astronaut',figsize=(8,8))  

# # plt.subplot(2,2,1)     
# # plt.imshow(im)      
# # plt.subplot(2,2,2)     
# # plt.imshow(imgray)      
# # plt.subplot(2,2,3)     
# # plt.imshow(dst)      
# # plt.subplot(2,2,4)     
# # plt.imshow(grey_mask)      
# # plt.show()

# # cv2.imshow("1", im)
# # cv2.imshow("2", imgray)
# cv2.imshow("3", dst)
# # cv2.imshow("4", grey_mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
