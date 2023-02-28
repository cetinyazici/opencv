# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 19:28:52 2023

@author: Lenovo
"""

import cv2 
from matplotlib import pyplot as plt

resim = cv2.imread("c.jpg")

cv2.imshow("resim penceresi", resim)


plt.imshow(resim,cmap="gray")
plt.show()


k = cv2.waitKey(0)

cv2.destroyWindow("resim penceresi")

if k == 27:
    print("ESC tusuna basılarak kapatıldı...")
    
elif k == ord("q"):
    print("q tuşuna basılarak kapatıldı..ve Resim kayıt edildi!!")
    cv2.imwrite("cgri.jpg",resim)