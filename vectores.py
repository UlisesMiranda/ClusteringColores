import math
import matplotlib.pyplot as plt
import numpy as np

def graficarVectores(vecs, cols, alpha = 1):

    plt.figure()
    plt.legend(cols)
    plt.axvline(x=0, color='grey', zorder=0)
    plt.axhline(y=0, color='grey', zorder=0)
    
    plt.xlim(-5,5)
    plt.ylim(-5,5)

    for i in range(len(vecs)):
        x = np.concatenate([[0, 0], vecs[i]])
        plt.quiver([x[0]],
                [x[1]],
                [x[2]],
                [x[3]],
                angles='xy', scale_units='xy', scale=1, color=cols[i], alpha=alpha)

    plt.show()
    
def graph_cross_point(v):
    x1 = range(-5,5)
    y1 = [values(v[0],i) for i in x1]

    x2 = range(-5,5)
    y2 = [values(v[1],i) for i in x2]
    
    cross = v[2]

    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.scatter(cross[0],cross[1], c = 'r', marker = 'o')
    
    plt.show() 
    
    
def values(v,x):
    eval = (v[0]*x + v[2])/-v[1]
    return eval

def ingresarVector():
    variables = ['a', 'b', 'c']
    l = []
    for var in variables:
        l.append(int(input(f"Ingrese {var}: ")))
    
    if l[2] != 0:
        return np.array(l, dtype=float) / l[2]
    else:
        return np.array(l, dtype=float) 

def ingresarM():
    variables = ['x', 'y']
    l = []
    for var in variables:
        l.append(int(input(f"{var}: ")))
    l.append(1)
            
    return np.array(l, dtype=float)

def obtenerDistancia(m1, m2):
    
    distancia = math.sqrt((m1[0] - m2[0])**2 + (m1[1] - m2[1])**2)

    return distancia



opc = 's'

while opc == 's':
    l1 = np.zeros(3)
    l2 = np.zeros(3)
    l3 = np.zeros(3)
    m1 = np.zeros(3)
    m2 = np.zeros(3)
    
    print("--------Bienvenido-------")
    print("Operaciones:\n")
    print("1. l1 * l2= escalar")
    print("2. l1 x l2 = m")
    print("3. l1 x l3 = m1 && l2 x l3 = m2 -> distancia(m1 a m2)")
    print("4. m1 x m2")
    print("5. Distancia de m1 a m2")
    
    tipoOperacion = int(input("Ingrese la operacion que desea: "))
        
    result = None 
    resultEscalar = 0
    if tipoOperacion == 1:
        print("\nIngresa l1: ")
        l1 = ingresarVector()
        print("\nIngresa l2: ")
        l2 = ingresarVector()
        
        resultEscalar = l1 @ m1
        
        v = np.array([l1, l2, [0,0,0]])
        graph_cross_point(v)
        
    
    if (tipoOperacion == 2):
        print("\nIngresa l1: ")
        l1 = ingresarVector()
        print("\nIngresa l2: ")
        l2 = ingresarVector()
        
        result = np.cross(l1, l2)
        
        if result[2] != 0:
            result = result / result[2]
        
        v = np.array([l1, l2, result])
        graph_cross_point(v)
        
        
    if tipoOperacion == 3:
        print("\nIngresa l1: ")
        l1 = ingresarVector()
        print("\nIngresa l2: ")
        l2 = ingresarVector()
        print("\nIngresa l3: ")
        l3 = ingresarVector()
        
        m1 = np.cross(l1, l3)
        if (m1[2] != 0):
            m1 = m1 / m1[2]
        v = np.array([l1, l3, m1])
        graph_cross_point(v)
        
        
        m2 = np.cross(l2, l3)
        if (m2[2] != 0):
            m2 = m2 / m2[2]
        v = np.array([l2, l3, m2])
        graph_cross_point(v)
        
        resultEscalar = obtenerDistancia(m1, m2)
    
    if tipoOperacion == 4:
        print("\nIngresa m1: ")
        m1 = ingresarM()
        print("\nIngresa m2: ")
        m2 = ingresarM()
        
        result = np.cross(m1, m2)
        
        if result[2] != 0:
            result = result / result[2]
        v = np.array([m1, m2, result])
        graph_cross_point(v)
        
    if tipoOperacion == 5:
        print("\nIngresa m1: ")
        m1 = ingresarM()
        print("\nIngresa m2: ")
        m2 = ingresarM()
        
        result = obtenerDistancia(m1, m2)
        
        if result[2] != 0:
            result = result / result[2]
        v = np.array([m1, m2, result])
        graph_cross_point(v)
    
    
        
    print("Colores: \n")
    print("l1: red")
    print("l2: blue")
    print("l3: orange")
    print("m1: green")
    print("m2: pink")
    print("result: black")
    
    if tipoOperacion != 1 and tipoOperacion != 3 and tipoOperacion != 5:
        print("Resultado: ", result)
        graficarVectores([l1, l2, l3, m1, m2, result], ['red', 'blue', 'orange', 'green', 'pink', 'black'] )
    else:
        print("Resultado: ", resultEscalar)
        graficarVectores([l1, l2, l3, m1, m2], ['red', 'blue', 'orange', 'green', 'pink'])
    
    opc = input("Desea otra operacion? s/n: ")