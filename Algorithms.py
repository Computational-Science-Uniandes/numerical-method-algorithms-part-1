# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:22:13 2022

@author: Asus
"""

def derivada_numerica1(x_values,y_values,loc):#Verificada
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localizacion de un
        punto en x, retorna la derivada numerica en ese punto.


    ParÃ¡metros: 
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

def derivada_numerica2(x_values,loc,funcion):#Verifcada
    '''Ingresados los valores de x,y la localizacion de un punto en x,
        retorna la derivada numerica en ese punto con h=10**-6
        Defina la funcion como funcion(x)


    ParÃ¡metros: 
        x_values: Valores de x
        loc: localizacion en la lista del valor de x que queremos evaluar
        funcion:funcion deseada

    Retorno:
        Derivada evaluada numericamente en el punto deseado
    '''
    h=10e-6
    return (funcion(x_values[loc]+h)-funcion(x_values[loc]-h))/(2*h)

def segunda_derivada_numerica1(x_values,y_values,loc):#verificada
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


    ParÃ¡metros: 
        x_values: Valores de x
        loc: localizacion en la lista del valor de x que queremos evaluar
        funcion: funcion deseada

    Retorno:
        Segunda Derivada evaluada nÃºmericamente en el punto deseado
    '''
    h=10e-6
    funcion(x_values[loc]-h)
    return((funcion(x_values[loc]+h)-2*funcion(x_values[loc])+funcion(x_values[loc]-h))/((h)**2))

def lista_derivada_numerica1(x_values,y_values):#verificada
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

def lista_derivada_numerica2(x_values,funcion):#verificada
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

def lista_segunda_derivada_numerica1(x_values,y_values):#verificada
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

def lista_segunda_derivada_numerica2(x_values,funcion):#verificada
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


    ParÃ¡metros: 
        x0: valor inicial
        función: función
        derivada: derivada
        
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
    '''
    xantes=x0
    xdespues=x0-(funcion(xantes)/derivada_numerica2([xantes],0,funcion))
    while  (xdespues-xantes)/xantes<10e-6:
        xantes=xdespues
        xdespues=xantes-(funcion(xantes)/derivada_numerica2([xantes],0,funcion))
    return xdespues


