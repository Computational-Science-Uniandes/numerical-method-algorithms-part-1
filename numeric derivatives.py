# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 06:35:37 2022

@author: Asus
"""
def derivada_numerica1(x_values,y_values,loc):#Verificada
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localización de un
        punto en x, retorna la derivada númerica en ese punto.


    Parámetros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
        loc: localización en la lista del valor de x que queremos evaluar

    Retorno:
        Derivada evaluada númericamente en el punto deseado
    '''
    y_values[0]
    if loc!=0 and loc!=len(x_values)-1:
        return (y_values[loc+1]-y_values[loc-1])/(2*(x_values[1]-x_values[0]))  
    elif loc==0:
        return (y_values[loc+1]-y_values[loc])/((x_values[1]-x_values[0]))  
    elif loc==len(x_values)-1:
        return (y_values[loc]-y_values[loc-1])/((x_values[1]-x_values[0]))  

        

def derivada_numerica2(x_values,loc,funcion):#Verifcada
    '''Ingresados los valores de x,y la localización de un punto en x,
        retorna la derivada númerica en ese punto con h=10**-6
        Defina la función como funcion(x)


    Parámetros: 
        x_values: Valores de x
        loc: localización en la lista del valor de x que queremos evaluar
        funcion:función deseada

    Retorno:
        Derivada evaluada númericamente en el punto deseado
    '''
    h=10e-6
    return (funcion(x_values[loc]+h)-funcion(x_values[loc]-h))/(2*h)

    

def segunda_derivada_numerica1(x_values,y_values,loc):#verificada
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localización de un
        punto en x, retorna la segunda derivada númerica en ese punto


    Parámetros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
        loc: localización en la lista del valor de x que queremos evaluar

    Retorno:
        Segunda Derivada evaluada númericamente en el punto deseado. Atención La función evalua en puntos diferentes del inicial y final.
    '''
    return((y_values[loc+1]-2*y_values[loc]+y_values[loc-1])/((x_values[1]-x_values[0])**2))

def segunda_derivada_numerica2(x_values,loc,funcion):#verificada
    '''Ingresados los valores de x,y la localización en el
        punto en x, retorna la segunda derivada númerica en ese punto con h=10**-6
        Defina la función como funcion(x)


    Parámetros: 
        x_values: Valores de x
        loc: localización en la lista del valor de x que queremos evaluar
        funcion: función deseada

    Retorno:
        Segunda Derivada evaluada númericamente en el punto deseado
    '''
    h=10e-6
    funcion(x_values[loc]-h)
    return((funcion(x_values[loc]+h)-2*funcion(x_values[loc])+funcion(x_values[loc]-h))/((h)**2))


def lista_derivada_numerica1(x_values,y_values):#verificada
    '''Ingresados los valores de x y los valores de y, se retorna las derivadas númericas

    Parámetros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y

    Retorno:
        lista con las derivadas númericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(derivada_numerica1(x_values, y_values,i))
    return list
    
    
def lista_derivada_numerica2(x_values,funcion):#verificada
    '''Ingresados los valores de x y la función deseada, se retorna las derivadas númericas

    Parámetros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        función: función deseada
    Retorno:
        lista con las derivadas númericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(derivada_numerica2(x_values,i,funcion))
    return list

def lista_segunda_derivada_numerica1(x_values,y_values):#verificada
    '''Ingresados los valores de x y los valores de y, se retorna las segundas derivadas númericas

    Parámetros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y

    Retorno:
        lista con las segundas derivadas númericas
    '''
    list=[]
    for i in range(1,len(x_values)-1):
        list.append(segunda_derivada_numerica1(x_values,y_values,i))
    return list

    

    
def lista_segunda_derivada_numerica2(x_values,funcion):#verificada
    '''Ingresados los valores de x y la función deseada, se retorna las derivadas númericas

    Parámetros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        función: función deseada
    Retorno:
        lista con las segundas derivadas númericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(segunda_derivada_numerica2(x_values,i,funcion))
    return list

#def newton_raphson_derivada_conocida(x0,funcion,derivada): En proceso
    '''Ingresados los valores de x y y
        retorna la solución númerica, Porfavor verifique con la función cambio_concavidad y
        derivada_0, y asegure un intervalo de convergencia; de lo contrario el programa puede no funcionar
        defina la función como f(x)


    Parámetros: 
        x_values: Valores de x
        y_values: Valores de y
        
    '''
    #xantes=x0
    #xdespues=xantes-(funcion(xantes)/derivada(xantes))
    #while xdespues-xantes>10e-6:
        #xantes=xdespues
       # xdespues=xantes-(funcion(xantes)/derivada(xantes))
    #return xdespues

#def newton_raphson_derivada_desconocida(funcion,h): En proceso
    '''Ingresados los valores de x y y
        retorna la solución númerica(En caso que la derivada sea complicada), Porfavor verifique con la función cambio_concavidad_númerica
        derivada_no_cero_numerica, y asegure un intervalo de convergencia; de lo contrario el programa puede no funcionar


    Parámetros: 
        funcion: Función conocida
        h: 
    '''
    #xantes=x_values[loc]
    #xdespues=xantes-(funcion(xantes)/derivada_central_numerica2(x_values,y_values,loc))
    #while xdespues-xantes>10**-6:
        #xantes=xdespues
        #xdespues=xantes-(funcion(xantes)/derivada(xantes))
    #return xdespues







        
    