# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:22:13 2022

@author: Asus
"""

def productoria(list):
    '''Ingresada una lista devuelve el producto de todos sus elementos
        Parametros:
            list:lista con los elementos
        Retorno
            Producto de todos sus elementos'''
    despues=list[0]
    for i in range(1,len(list)):
        despues=despues*list[i]
    return despues

def sumatoria(list):
    '''Ingresada una lista devuelve la suma de todos sus elementos
        Parametros:
            list:lista con los elementos
        Retorno
            Suma de todos sus elementos'''
    despues=list[0]
    for i in range(1,len(list)):
        despues=despues+list[i]
    return despues

def interpolacionlagrange(x,X,Y):
    '''Ingresada un valor de x, una lista de valores de X y de Y devuelve la interpolacion de lagrange evaluada en x
        Parametros:
            x:valor de x
            X:valores de x
            Y:valores de y
        Retorno
            Interpolacion de lagrange evaluada en x'''
    
    coeficientes=Y
    polinomios_x=[]
    auxiliar=[]
    for i in range(0,len(X)):
        for j in range(0,len(X)): 
            if i!=j:
                auxiliar.append((x-X[j])/(X[i]-X[j]))
        polinomios_x.append(productoria(auxiliar)*coeficientes[i])
        auxiliar=[]
    return sumatoria(polinomios_x)


def derivada_numerica1(x_values,y_values,loc):
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localizacion de un
        punto en x, retorna la derivada numerica en ese punto.
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
        loc: localizacion en la lista del valor de x que queremos evaluar
    Retorno:
        Derivada evaluada numericamente en el punto deseado
    '''
    y_values[0]
    if loc!=0 and loc!=len(x_values)-1:
        return (y_values[loc+1]-y_values[loc-1])/(2*(x_values[1]-x_values[0]))  
    elif loc==0:
        return (y_values[loc+1]-y_values[loc])/((x_values[1]-x_values[0]))  
    elif loc==len(x_values)-1:
        return (y_values[loc]-y_values[loc-1])/((x_values[1]-x_values[0]))  

def derivada_numerica2(x_values,loc,funcion):
    '''Ingresados los valores de x,y la localizacion de un punto en x,
        retorna la derivada numerica en ese punto con h=10**-6
        Defina la funcion como funcion(x)
    Parametros: 
        x_values: Valores de x
        loc: localizacion en la lista del valor de x que queremos evaluar
        funcion:funcion deseada
    Retorno:
        Derivada evaluada numericamente en el punto deseado
    '''
    h=10e-6
    return (funcion(x_values[loc]+h)-funcion(x_values[loc]-h))/(2*h)

def segunda_derivada_numerica1(x_values,y_values,loc):
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localizacion de un
        punto en x, retorna la segunda derivada numerica en ese punto
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
        loc: localizacion en la lista del valor de x que queremos evaluar
    Retorno:
        Segunda Derivada evaluada nÃºmericamente en el punto deseado. Atencion La funcion evalua en puntos diferentes del inicial y final.
    '''
    return((y_values[loc+1]-2*y_values[loc]+y_values[loc-1])/((x_values[1]-x_values[0])**2))

def segunda_derivada_numerica2(x_values,loc,funcion):
    '''Ingresados los valores de x,y la localizacion en el
        punto en x, retorna la segunda derivada numerica en ese punto con h=10**-6
        Defina la funcion como funcion(x)
    Parametros: 
        x_values: Valores de x
        loc: localizacion en la lista del valor de x que queremos evaluar
        funcion: funcion deseada
    Retorno:
        Segunda Derivada evaluada nÃºmericamente en el punto deseado
    '''
    h=10e-6
    funcion(x_values[loc]-h)
    return((funcion(x_values[loc]+h)-2*funcion(x_values[loc])+funcion(x_values[loc]-h))/((h)**2))

def lista_derivada_numerica1(x_values,y_values):
    '''Ingresados los valores de x y los valores de y, se retorna las derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
    Retorno:
        lista con las derivadas numericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(derivada_numerica1(x_values, y_values,i))
    return list

def lista_derivada_numerica2(x_values,funcion):
    '''Ingresados los valores de x y la funcion deseada, se retorna las derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        funcion: funcion deseada
    Retorno:
        lista con las derivadas numericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(derivada_numerica2(x_values,i,funcion))
    return list

def lista_segunda_derivada_numerica1(x_values,y_values):
    '''Ingresados los valores de x y los valores de y, se retorna las segundas derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
    Retorno:
        lista con las segundas derivadas numericas
    '''
    list=[]
    for i in range(1,len(x_values)-1):
        list.append(segunda_derivada_numerica1(x_values,y_values,i))
    return list

def lista_segunda_derivada_numerica2(x_values,funcion):
    '''Ingresados los valores de x y la función, retorna lista de las segundas derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        funcion: funcion deseada
    Retorno:
        lista con las segundas derivadas numericas
    '''
    list=[]
    for i in range(0,len(x_values)):
        list.append(segunda_derivada_numerica2(x_values,i,funcion))
    return list

def newton_raphson_derivada_conocida(x0,funcion,derivada): 
    '''Ingresados los valores de x0, la funcion y la derivada
        retorna la solucion numerica, porfavor verifique que la funcion no cambie de
        concavidad y la derivada sea diferente de 0 en el intervalo de convergencia, y asegure un intervalo de convergencia; 
        de lo contrario el programa puede no funcionar.
        Defina la funcion como f(x).
    Parametros: 
        x0: valor inicial
        función: función
        derivada: derivada
    Retorno:
        Solucion numerica newton-raphson
        
    '''
    xantes=x0
    xdespues=xantes-(funcion(xantes)/derivada(xantes))
    while (xdespues-xantes)/xantes>10e-6:
        xantes=xdespues
        xdespues=xantes-(funcion(xantes)/derivada(xantes))
    return xdespues

def newton_raphson_derivada_desconocida(x0,funcion): 
    '''Ingresados los valores de x y y
        retorna la solucion numerica(En caso que la derivada sea complicada), porfavor verifique que la funcion no cambie de
        concavidad y la derivada sea diferente de 0 en el intervalo de convergencia, y asegure un intervalo de convergencia; de lo contrario el programa puede no funcionar.
        Defina la funcion como f(x).
    Parametros: 
        x0: valor inicial
        funcion: función conocida.
    Retorno:
        Solucion numerica newton-raphson
    '''
    xantes=x0
    xdespues=x0-(funcion(xantes)/derivada_numerica2([xantes],0,funcion))
    while  (xdespues-xantes)/xantes<10e-6:
        xantes=xdespues
        xdespues=xantes-(funcion(xantes)/derivada_numerica2([xantes],0,funcion))
    return xdespues

def integral_riemann(f,a,b):
    '''Ingresada la funcion, los limites de integracion(1000 particiones) devuelve la integral numerica(riemann) aproximada
        Parametros:
            f:funcion
            a: intervalo inferior
            b: intervalo superior
            n: numero de intervalos
       Retorno
           Devuelve la integral numerica(riemann)'''
    Δx=(b-a)/1000
    I=0
    for i in range(0,1000):
        xi=a+i*Δx
        I+=f(xi)*Δx
    return I

def integral_trapecio(f,a,b):
    '''Ingresada la funcion, los limites de integracion(1000 particiones) devuelve la integral numerica(trapecio) aproximada
        Parametros:
            f:funcion
            a: intervalo inferior
            b: intervalo superior
            n: numero de intervalos
       Retorno
           Devuelve la integral numerica(trapecio)'''
    Δx=(b-a)/1000
    yi=f(a)
    yf=f(b)
    sigmaf=0
    xi=0
    for i in range(1,1000):
        xi=a+i*Δx
        sigmaf+=f(xi)
        
    I=Δx*((yi/2)+sigmaf+(yf/2))
    return I

from scipy.special import roots_legendre

def intregral_gauss_legendre(funcion,a,b):
    '''Ingresada la funcion, los limites de integracion(1000 particiones) devuelve la integral numerica(gauss legendre) aproximada
        Parametros:
            f:funcion
            a: intervalo inferior
            b: intervalo superior
            n: numero de intervalos
       Retorno
           Devuelve la integral numerica(gauss legendre)'''
    
    x,integral=0,0
    raices,pesos=roots_legendre(1000)
    for i in range(0,1000):
        x=(1/2)*(raices[i]*(b-a)+a+b)
        integral+=funcion(x)*pesos[i]
    integral=(1/2)*(b-a)*integral        
    return integral

def matriz_vacia(n,m):
    '''Ingresados los valores deseados de columnas y filas
        retorna una matriz vacía de nxm
    Parametros: 
        n: numero de filas
        m: numero de columnas
    Retorno:
        Matriz vacia de nxm
    '''
    vacia=[]
    for i in range(0,n):
         vacia.append([])
    for j in vacia:
         for k in range(0,m):
             j.append(0)
    return vacia

def print_matriz(matriz):
    '''Imprime la matriz de manera organizada
    '''
    for i in range(0,len(matriz)):
            print(matriz[i])
    return(' ')  
          
def columnaj(matriz,j):
    '''Ingresados la columna deseada
        retorna esta columna
    Parametros: 
        matriz: matriz deseada
        m: columna deseada
    Retorno:
        columna deseada
    '''
    columna=[]
    for i in range(0,len(matriz)):
        columna.append(matriz[i][j])
    return columna

def producto_punto(vector1,vector2):
    '''Ingresados 2 vectores
        retorna su producto punto
    Parametros: 
        vector1: vector 2
        vector2: vector 1
    Retorno:
        producto punto
    '''
    productopunto=0
    for k in range(0,len(vector1)):
          productopunto+=vector1[k]*vector2[k]
    return productopunto

def suma(matriz1,matriz2):
    '''Ingresados 2 Matrices
        retorna su suma
    Parametros: 
        matriz1: Matriz 2
        matrizr2: Matriz 1
    Retorno:
        Retorna su suma
    '''
    suma=matriz_vacia(len(matriz1),len(matriz1[0]))
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz1[0])):
            suma[i][j]=matriz1[i][j]+matriz2[i][j]
    return suma

def resta(matriz1,matriz2):
    '''Ingresados 2 Matrices
        retorna su resta
    Parametros: 
        matriz1: Matriz 1
        matrizr2: Matriz 2
    Retorno:
        Retorna Matriz 1 - Matriz 2
    '''
    resta=matriz_vacia(len(matriz1),len(matriz1[0]))
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz1[0])):
            resta[i][j]=matriz1[i][j]-matriz2[i][j]
    return resta

def producto(matriz1,matriz2):
    '''Ingresados 2 Matrices
        retorna su producto
    Parametros: 
        matriz1: Matriz 1
        matrizr2: Matriz 2
    Retorno:
        Retorna Matriz 1*Matriz 2
    '''
    
    producto=matriz_vacia(len(matriz1),len(matriz2[0]))
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz2[0])):
            producto[i][j]=producto_punto(matriz1[i],columnaj(matriz2,j))
    return producto
    
def productoescalar(matriz,c):
    '''Ingresados 1 Matriz y un escalar
        retorna el producto
    Parametros: 
        matriz1: Matriz 
        c: Escalar
    Retorno:
        Retorna c*Matriz 1
    '''
    new=matriz_vacia(len(matriz),len(matriz[0]))
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
                new[i][j]=matriz[i][j]*c
    return new

def eliminarfilai(matriz,i):
    '''Ingresados 1 Matriz y una fila 
        retorna la matriz sin la fila
    Parametros: 
        matriz1: Matriz 1
        i: Fila deseada
    Retorno:
        Matriz sin la fila i
    '''
    i=i-1
    new=[]
    for k in range(0,len(matriz)):
        if k!=i:
             new.append(matriz[k])
    return new

def eliminarcolumnaj(matriz,j):
    '''Ingresados 1 Matriz y una columna
        retorna la matriz sin la columna
    Parametros: 
        matriz1: Matriz 1
        j: Columna deseada
    Retorno:
        Matriz sin la Columna j
    '''
    j=j-1
    new=[]
    aux=[]
    for i in range(0,len(matriz)):
        for k in range(0,len(matriz[0])):
            if k!=j:
                aux.append(matriz[i][k])
        new.append(aux)
        aux=[]
    return new

def eliminar_filai_columnaj(matriz,i,j):
    '''Ingresados 1 Matriz,una fila y una columna
        retorna la matriz sin la fila y la columna
    Parametros: 
        matriz1: Matriz 1
        i: Fila deseada
        j: Columna deseada
    Retorno:
        Matriz sin la fila i y la columna j
    '''
    new=eliminarfilai(matriz,i)
    new=eliminarcolumnaj(new,j)
    return new

def determinante(matriz):
    return None

print(sumatoria([1,1,1,1,1]))










        




