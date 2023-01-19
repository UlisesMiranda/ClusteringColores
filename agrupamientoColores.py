
import random

import cv2
import kmeans as km
import numpy as np
import matplotlib.pyplot as plt

def agrupamientoPorColoresKmeans(imagen):
    filas, columnas, c = imagen.shape

    imagenNp = np.array(imagen, dtype=np.uint8)

    listR = imagenNp[:,:,2].reshape((-1, 1))  
    listG = imagenNp[:,:,1].reshape((-1, 1)) 
    listB = imagenNp[:,:,0].reshape((-1, 1)) 

    X = np.concatenate((listR,listG,listB), axis=1)

    kClusters = 5

    centroides, asignaciones = km.k_means(X, kClusters)

    m = listR.shape
    for i in range(m[0]):
        listR[i] = int(centroides[asignaciones[i]][2]) 
        listG[i] = int(centroides[asignaciones[i]][1]) 
        listB[i] = int(centroides[asignaciones[i]][0]) 
        
    listR.shape = (filas, columnas) 
    listG.shape = (filas, columnas) 
    listB.shape = (filas, columnas) 

    listR = listR[:, :, np.newaxis]  
    listG = listG[:, :, np.newaxis]
    listB = listB[:, :, np.newaxis]

    imagenAgrupadaColores = np.concatenate((listR,listG,listB), axis=2)

    cv2.imshow("Imagen Original", imagen)
    cv2.imshow("Imagen por kmeans", imagenAgrupadaColores)
    cv2.waitKey()



random.seed(0)

imagen = cv2.imread("crayones.jpg")

agrupamientoPorColoresKmeans(imagen)