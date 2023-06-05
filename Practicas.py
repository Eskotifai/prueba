def operacion1():
    from math import sqrt
    try:
        x = float(input("introduzca x: "))
        y = float(input("introduzca y: "))
        numerador = 3*x**2*y*sqrt(2*x+y)
        denominador = sqrt(4*x**2+4*x*y+y**2)   
        if x!=0 or y!=0:
            operacion = numerador/denominador
            print(f"El resultado es {operacion}")
        else:
            print("no se puede dividir entre cero")
    except Exception:
        print("Introduce solo numeros")
 
def kilometraje():
    try: 
        km= float(input("introduzca los kilometros: "))    
        if 0<km<300:
            print("El cliente debe cancelar 25000bs")
        elif 300<km<=1000:
            razon1= 8500/km
            print(f"El cliente debe cancelar {25000+razon1}bs")
        elif km>1000:
            razon2= 6500/km
            print(f"El cliente debe cancelar {25000+razon2}bs")
        else:
            print("Introduzca un kilometraje valido")
    except Exception:
        print("introduce solo numeros")

def pago_empleados():
    print("\nLos tipos de empleados son los siguientes:\nIntroduzca un numero del 1 al 4 para seleccionar el tipo de empleado:\n")
    print("1 Para gerente\n2 Para Trabajador por Hora\n3 Para Trabajador por comision\n4 Para trabajador a destajo\n\nPara cerrar el programa use 5")
    while True:
        
            try:
                
                nombre_empleado=(input("\nIntroduzca el nombre del empleado: "))               
                empleado= int(input("\nIntroduzca el tipo de empleado: "))
                
                if empleado == 1:
                    while True:
                        try:
                            print(f"\nEl empleado {nombre_empleado} es un Gerente\n")
                            sueldo = int(input("Introduzca el salario semanal del Gerente: "))       
                            if sueldo>0:
                                print(f"\nEl gerente {nombre_empleado} tiene un salario semanal fijo de {sueldo} bolivares chinos")
                                break
                            else:
                                print("\n**Introduzca un salario valido**\n")
                        except Exception:
                            print("\n**Introduce solo numeros**")
                        
                elif empleado == 2:
                    while True:
                        try:
                            print(f"\nEl empleado {nombre_empleado} es un Trabajador por hora\n")
                            sueldo = int(input("Introduzca el sueldo del trabajador por hora: "))
                            horas = int(input("\nIntroduzca las horas de trabajo: "))
                            if horas == 40:
                                print(f"\nEl salario del trabajador por hora {nombre_empleado} es: {sueldo}")
                                break
                            elif 0<horas<40:
                                ratio= sueldo/40
                                reducido = 40 - horas
                                sueldoreducido= sueldo-(ratio*reducido)
                                print(f"\nEl salario del trabajador por horas {nombre_empleado} es: {sueldoreducido} por flojo")
                                break       
                            elif horas>40:
                                ratio= sueldo/40
                                extra = horas-40
                                sueldoextra= sueldo+(ratio*extra*1.5)
                                print(f"\nEl salario del trabajador por horas {nombre_empleado} es: {sueldoextra} por trabajador")
                                break
                            else:
                                print("\n**Introduzca un salario valido**")
                        except Exception:
                            print("\n**introduce solo numeros**")
                            
                elif empleado == 3:
                    while True:
                        try:
                            print(f"\nEl empleado {nombre_empleado} es un Trabajador por comision\n")
                            sueldo= 25000
                            bruto = int (input("Introduzca las ventas brutas semanales: "))
                            if bruto>0:
                                sueldo= sueldo+0.057*bruto
                                print(f"El salario del trabajador por comision {nombre_empleado} es {sueldo}")
                                break
                            else:
                                print("\n**Introduzca una venta valida**")
                        except Exception:
                            print("\n**Introduce solo numeros**")
                    
                elif empleado == 4:
                    while True:
                        try:
                            print(f"\nEl empleado {nombre_empleado} es un Trabajador a destajo\n")
                            articulo= int(input("Introduzca el precio del articulo: "))
                            cantidad= int(input("\nIntroduzca el numero de articulos: "))
                            if articulo>0 and cantidad>0:
                                print(f"El salario del trabajador a destajo {nombre_empleado} es {articulo*cantidad}")
                                break
                            else:
                                print("\n**Introduzca un articulo valido**")
                        except Exception:
                            print("\n**Introduce solo numeros**")
                
                elif empleado == 5:
                    print('\n**Salir**\n')
                    break
                                
                else:
                    print("\n**Introduzca solo numeros del 1 al 5**")
                    
            except Exception:
                print("\n**Introduce solo numeros**")
 
def bucle_whiletrue():
    while True:
        try:
            x= int(input("\nintroduzca un numero del 0 al 10: "))            
            if x>=0 and x<=10:
                print(f"\nEl numero es {x}\n")    
                while True:
                    x= x + 1
                    print(f"{x}\n")                
                    if x == 20:
                        break
            else:
                print("\nIntroduzca solo numeros del 1 al 10")
        except Exception:
            print("\nIntroduce solo numeros")

def menu_simple():
    while True:
        
        try:
            
            print('Opcion 1\nOpcion 2\nOpcion 3\nOpcion 4\n')
            opcion= int(input('Seleccione la opcion: '))
            
            if opcion == 1:
                while True:    
                    try:                    
                        print('\nla opcion es 1')
                        numero= int(input('\nintroduce un numero entero positivo: '))
                        if numero>0:
                            print(f'\nel numero es: {numero}\n') 
                            break
                        else:
                            print('introduce solo enteros positivos')                                
                    except Exception:
                        print('introduce solo numeros')
                
            elif opcion == 2:
                while True:
                    try:
                        print('\nla opcion es 2')
                        numero= int(input('\nintroduce un numero entero positivo: '))
                        if numero>0:
                                print(f'\nel numero es: {numero}\n')
                                break
                        else:
                            print('\nintroduce solo enteros positivos')
                    except Exception:
                        print('\nintroduce solo numeros')
                            
            elif opcion == 3:
                while True:
                    try:
                        print('\nla opcion es 3')
                        numero= int(input('\nIntroduce un numero entero positivo: '))
                        if numero>0:
                            print(f'\nEl numero es {numero}\n')
                            break
                        else:
                            print('\nIntroduce solo enteros positivos')
                    except Exception:
                        print('\nIntroduce solo numeros')
                        
            elif opcion == 4:
                while True:
                    try:
                        print('\nla opcion es 4')
                        numero= int(input('\nIntroduce un numero entero positivo: '))
                        if numero>0:
                            print(f'\nel numero es {numero}\n')
                            break
                        else:
                            print('\nintroduce solo enteros positivos')
                    except Exception:
                        print('\nintroduce solo numeros')
                        
            else:
                print('\nIntroduce solo numeros del 1 al 4\n')
                            
        except Exception:
            print('\nintroduce solo numeros\n')       
   
def prueba_string():
    nombre = (input('introduce tu nombre: '))
    print (f'\n{nombre} eres un webon XD')

def multiplos_5():
    while True:
        try:
            n=int(input('Introduce a n: '))
            if n%5==0:
                for i in range(1,n):
                    if i%5==0:
                        print(i)
                break
            else:
                print(f'{n} No es multiplo de 5')
        except ValueError:
            print('\nIntroduce solo numeros\n')
    
def grados():
    
    print('**Menu**\nOpcion 1 Centigrados a Fahrenheit\nOpcion 2 Fahrenheit a Centigrados\nOpcion 3 Salir\n')
    CONST_1=1.8
    CONST_2=32
    while True:
        
        try:
            
            opcion=int(input('Introduce la opcion: '))
            if opcion == 3:
                print('**Salir**\n')
                break
            grados=float(input('Introduce los grados: '))
            
            if opcion == 1:                                    
                print(f'{grados}C equivalen a {(grados*CONST_1)+CONST_2}F')
                
            elif opcion == 2:
                print(f'{grados}F equivalen a {(grados-CONST_2)/CONST_1}C')
            
            else:
                print('Introduce una opcion valida')
                
        except Exception:
            print('**Introduce solo numeros**')

def prueba_excepciones():
    while True:
        try:
            numero=float(input('Introduce un numero: \n'))
            print(numero)
            break
        except ValueError:
            print('introduce solo numeros')
                                    
def vuelto(): #Completar mostrando la menor cantidad de billetes posibles
    while True:
        try:
            cobra= float(input('Cuanto cobra: '))
            paga= float(input('Cuanto paga: '))
            vuelto = paga-cobra
            
            if cobra > 0 and paga >0:
                
                if paga>cobra:
                    print(f'Te deben {vuelto}$')
                    
                elif vuelto == 0:
                    print('No te deben dinero')
            else:
                print('Introduzca un monto valido')
        except ValueError:
            print('Introduce solo numeros')
        
def coprimos():
    while True:
        try:
            num1=int(input('Introduzca el numero 1: '))
            num2=int(input('Introduzca el numero 2: '))
            
            if not num1%num2==0:
                print(f'{num1} y {num2} son coprimos')
                
            else:
                print("Los numeros no son coprimos")
                
        except ValueError:
            print('Introduce solo numeros')
    
def es_multiplo(): #Arreglar mostrando TRUE o FALSE
    while True:
        try:
            n=int(input('Introduzca n: '))
            m=int(input('Introduzca m: '))
            if n%m==0:
                print(f'{n} es multiplo de {m}')
            else:
                print(f'{n} y {m} no son multiplos')
        except ValueError:
            print('Introduce solo numeros')

def suma_cuadrados():
    while True:
        try:
            n=int(input('Introduce a n: '))
            j=0
            if not (n == 0 and n<0):
                
                for i in range(1,n):
                    
                    j+=i**2
                    print(j)
                break
            else:
                print('No introduzcas 0')
        except ValueError:
            print('Introduce solo numeros')

def suma_cuadrados_impares():
    while True:
        try:
            n=int(input('Introduce a n: '))
            j=0
            if not (n == 0 and n<0):
                
                for i in range(1,n):
                    
                    if i%2!=0:
                        j+=i**2
                        print(j)
                break
            
            else:
                print('No introduzcas 0')
                
        except ValueError:
            print('Introduce solo numeros')
    
def listas():
    
    objetos=['a','b','c','d','e']
    lista_vacia=[]
    
    for i in enumerate(objetos): #Recorre la lista, imprime el indice (desde 0 hasta n) y el elemento entre parentesis
        print(i)
    print('')
    
    for j in range(len(objetos)): #Recorre los elementos de una lista
        print(objetos[j])
    print('')
    
    for k in objetos: #Recorre los elementos de una lista
        print(k)
    print('')    
    
    for j,k in enumerate(objetos): #Imprime el indice y el elemento de la lista sin parentesis usando una tupla (j,k)
        print(j,k)
    print('')
    
    print(len(objetos)) #Imprime la cantidad total de elementos de una lista
    print('')
    
    for l in range(5): #Agrega elementos a una lista hasta un rango n
        nuevo_elemento=(input('Inserta un elemento en la lista: ')) #Agrega un objeto a una lista en la ultima posicion
        lista_vacia.append(nuevo_elemento)
    print(f'La lista es {lista_vacia}')
    
    for m in range(4): #Elimina los elementos de una lista hasta un rango n
        lista_vacia.pop() #Elimina el ultimo elemento de un a lista si no se especifica un indice
    print(f'La lista es {lista_vacia}')
    
    for n in range(len(objetos)): #Elimina todos los elementos de una lista con un ciclo
        lista_vacia.pop() #Elimina el ultimo elemento de una lista si no se especifica un indice
    print(f'La lista esta vacia: {lista_vacia}')
    # IndexError (fuera del rango de la lista) (usar pop/remove en una lista vacia)
    
    objetos.clear() #Elimina todos los elementos de una lista
    print('Se elimino la lista')
     
def suma_y_promedio_de_una_lista():
    lista_a=[]
            
    cantidad_a=int(input('Introduce la cantidad de numeros en la Lista A: '))
    suma_lista_a=0
       
    for i in range(cantidad_a):
        
        a=float(input('\nIntroduce un numero para la Lista A: '))
        lista_a.append(a)
    print(f'\nLista A: {lista_a}')
    suma_lista_a=sum(lista_a)
    print(f'\nLa suma de la lista es {suma_lista_a}') 
    promedio=suma_lista_a/cantidad_a  
    print(f'\nEl promedio de la lista es {promedio}') 
                        
def minimo_maximo_lista():
    
    lista=[]
    longitud=int(input('Determina la longitud de la lista: '))
    for i in range(longitud):
        numeros=int(input('Agrega un numero a la lista: '))
        lista.append(numeros)           
    print(f'\nLa lista es: {lista}')
    print(f'El minimo es {min(lista)}') #MIN determina el minimo de una lista
    print(f'El maximo es {max(lista)}') #MAX determina el maximo de una lista                                       

def negativos_lista(): #Comprension de Listas
    lista=[]
    longitud=int(input('Determina la longitud de la lista: '))
    
    for i in range(longitud):
        numero=float(input('Agrega numeros a la lista: '))
        lista.append(numero)
    print(f'La lista es: {lista}')
    
    eliminar_negativos=[numeros for numeros in lista if numeros>0] #eliminar negativos usando 'Comprension de Listas'
    print(f'Se eliminaron los negativos: {eliminar_negativos}')
    
def invertir_lista():
    lista=[]
    longitud=int(input('Determina la longitud de la lista: '))
    
    for i in range(longitud):
        objetos=input('Agrega elementos a la lista: ')
        lista.append(objetos)
    print(f'La lista es: {lista}')

def tupla():
    lista_A=[]
    lista_B=[]
    a=int(input('Determina la longitud de la lista A: '))
    b=int(input('Determina la longitud de la lista B: '))   
    
    for i in range(a):
        
        objetos_a=input('Agrega elementos a la lista A: ')
        lista_A.append(objetos_a)
    print(f'Lista A: {lista_A}')
    
    for j in range(b):
        
        objetos_b=input('Agrega elementos a la lista B: ')
        lista_B.append(objetos_b)
    print(f'Lista B: {lista_B}')
    
    for i,j in range(lista_A, lista_B):
        print(i,j)
        
def crear_matriz():
    lista_A=[]  
    lista_B=[]
    
    # longitud_A=int(input('Determina la longitud de la lista A: '))
    # for i in range(longitud_A):
        
    #     objetos_A=input('Agrega elementos a la lista: ')
    #     lista_A.append(objetos_A)
    # print(f'Lista A: {lista_A}')
    
    # longitud_B=int(input('Determina la longitd de la lista B:'            #No es el metodo para crear una matriz MxN
    # for j in range(longitud_B):
        
    #     objetos_B=input('Agrega elementos a la lista: ')
    #     lista_B.append(objetos_B)
    # print(f'Lista B: {lista_B}') 
    
    x=int(input('Introduce filas: '))
    y=int(input('Introduce columnas: '))
    #solo es necesario una lista vacia para crear una matriz MxN
    #agrego filas(x) y columnas(y), segun las filas agrega elementos hasta llenarlas
    #al llenarse se repite el ciclo hasta que x llegue a un rango n
    for i in range(x):
        
        lista_A.append([])
        
        for j in range(y):
            
            objetos_A=input('Agrega elementos: ')
            lista_A[i].append(objetos_A) # ! sin [i] imprime la lista vacia y luego agrega los objetos
            
    print(f'Matriz: \n{lista_A}')
    
def SRP_arreglo():
    A=[]
    B=[]
    suma=[]
    diferencia=[]
    producto=[]
    longitud_a=int(input('Determina la longitud de la lista A: '))
    longitud_b=int(input('Determina la longitud de la lista B: ')) 
    if longitud_a == longitud_b:
        for i in range(longitud_a):
            m=int(input('Agrega elementos (A): '))
            A.append(m)
        print(f'Lista A: {A}')
        for j in range(longitud_b):
            m=int(input('Agrega elementos (B): '))
            B.append(m)
        print(f'Lista B: {B}')
        for k in range(longitud_a):
            suma.append(A[k]+B[k]) #Lo mismo aplica para resta y multiplicacion
        print(suma)

def ordenamiento_seleccion():
    arreglo=[]
    longitud=int(input('Determina la longitud del arreglo: '))
    
    for i in range(longitud):
        objetos=(input('Agrega objetos: '))
        arreglo.append(objetos)
    print(f'Arreglo: {arreglo}')
    
    for j in range(len(arreglo)):
        posicion_menor=j
        
        for k in range(j, len(arreglo)):
            
            if(arreglo[k] < arreglo[posicion_menor]):
                posicion_menor=k
                
        if posicion_menor != j:
            posicion_nueva=arreglo[j]
            arreglo[j]=arreglo[posicion_menor]
            arreglo[posicion_menor]=posicion_nueva
            
    print(f'Arreglo ordenado: {arreglo}')
        
def ordenamiento_insercion():
    arreglo=[]
    longitud=int(input('Determina la longitud del arreglo: '))
    for i in range(longitud):
        objetos=input('Agrega elementos: ')
        arreglo.append(objetos)
    print(f'Arreglo: {arreglo}')   
    for j in range(longitud):
        for k in range(j, 0 , -1):
            if arreglo[k-1] > arreglo[k]:
                cambio=arreglo[k]
                arreglo[k]=arreglo[k-1]
                arreglo[k-1]=cambio
    print(f'Arreglo ordenado: {arreglo}')

def ord_ins_sort():
    lista=[]
    longitud=int(input('Determina la longitud de la lista: '))
    for i in range(longitud):
        objetos=input('Agrega elementos: ')
        lista.append(objetos)
    print(f'Lista: {lista}')
    lista.sort()
    print(f'Lista ordenada: {lista}')                        
 
def ord_sel_sort():
    lista=[]
    longitud=int(input('Determina la longitud de la lista: '))
    for i in range(longitud): 
        objetos=input('Agrega elementos: ')
        lista.append(objetos)
    print(f'Lista: {lista}')
    lista.sort(reverse=True)
    print(f'Lista ordenada: {lista}') 
 
def busq_binaria():
    arreglo=[]
    longitud=int(input('Determina la longitud del arreglo: '))
    
    for i in range(longitud):
        objetos=int(input('Agrega numeros: '))
        arreglo.append(objetos)
    print(f'Arreglo: {arreglo}')
    arreglo.sort()
    print(f'Arreglo ordenado: {arreglo}')
    
    izq = 0
    med = 0
    der = len(arreglo) - 1
       
    buscar_numero=int(input('Busca un numero en el arreglo ordenado: '))
    
    while izq <= der:
        
        med = (izq+der)//2
    
        if buscar_numero > arreglo[med]:
            izq = med + 1
            
        elif buscar_numero < arreglo[med]:
            der = med - 1
        else:
            break
        # print(izq, med, der)
    
    existe=False        
    for i in arreglo:
        if buscar_numero == i:
            existe=True
            break
    if existe:
        print(f'{buscar_numero} esta en el arreglo')
    else:
        print(f'{buscar_numero} no esta en el arreglo')
            
            
    
    
        
if __name__ == '__main__':
    busq_binaria()