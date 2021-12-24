from tkinter import *
from tkinter import messagebox
import random

ingreso = Tk()
ingreso.geometry("300x100")
colorFondo = "#006"
colorLetra= "#FFF"
ingreso.configure(background=colorFondo)
ingreso.title("Ingreso al juego")
ingreso.resizable(0,0)


usuario = StringVar()
usuario.get


def Jugar():
    ingreso.destroy()
    juego = Tk()
    juego.geometry("500x400")
    juego.configure(background=colorFondo)
    juego.title("Ingreso al juego")
    juego.resizable(0,0)

    opcion = IntVar()
    P1 = StringVar()
    P2 = StringVar()
    P3 = StringVar()
    P4 = StringVar()
    P5 = StringVar()
    P6 = StringVar()
    P7 = StringVar()
    P8 = StringVar()
    P9 = StringVar()
    P10 = StringVar()
    P11 = StringVar()
    P12 = StringVar()
    P13 = StringVar()
    P14 = StringVar()
    P15 = StringVar()
    P16 = StringVar()
    P17 = StringVar()
    P18 = StringVar()
    P19 = StringVar()
    P20 = StringVar()
    P21 = StringVar()
    P22 = StringVar()
    P23 = StringVar()
    P24 = StringVar()
    P25 = StringVar()

    P1.set("Resuelva la siguiente operación: \n\n 2 + ( - 10 ) = \n\n A = 8 \n B = -8 \n C = 12 \n D = -12")
    P2.set("Resuelva la siguiente operación: \n\n - 7 + ( -7 ) = \n\n A = 14 \n B = -14 \n C = 0 \n D = -13")
    P3.set("Resuelva la siguiente operación: \n\n -2 + 2 ( -2 ) = \n\n A = -6 \n B = 6 \n C = 4 \n D = 8")
    P4.set("Resuelva la siguiente operación: \n\n ( -8 ) + 10 = \n\n A = -18 \n B = -2 \n C = 2 \n D = 18")
    P5.set("Resuelva la siguiente operación: \n\n  ( -15 ) +20 + ( -9 ) = \n\n A = 43 \n B = 14 \n C = 20 \n D = Ninguna de las anteriores")
    listaN1 = [P1,P2,P3,P4,P5]
    N1=random.choice(listaN1)
    
    P6.set("Resuelva la siguiente operación: \n\n 15 – 7 ( 2 – 11 ) =  \n\n A = -26 \n B = 78 \n C = 76 \n D = 91")
    P7.set("Resuelva la siguiente operación: \n\n 6 X 2 / 4 = = \n\n A = 3 \n B = 6 \n C = 12 \n D = 24")
    P8.set("Resuelva la siguiente operación: \n\n 24 ( -3 ) / 9 = \n\n A = 18 \n B = 8 \n C = -8 \n D = 72")
    P9.set("Resuelva la siguiente operación: \n\n ( 27 – 3 ) / 8 + 4 ( 5 – 7 )  = \n\n A = 18 \n B = -5 \n C = 36 \n D = 11")
    P10.set("Resuelva la siguiente operación: \n\n 72 / ( - 8 ) - 4 / ( 6 – 4 ) = \n\n A = 11 \n B = -8 \n C = 12 \n D = -74")
    listaN2 = [P6,P7,P8,P9,P10]
    N2=random.choice(listaN2)

    P11.set("Lla suma de cuatro veces X y siete veses Y es: \n\n A = X+X+X+X+Y+Y+Y+Y+Y+Y \n B = 4X + 7Y \n C = 4(-X ) + 7 (Y ) \n D = 4X-7 ")
    P12.set("Z mas tres veces la suma de X y Y es: \n\n A = Z + 3XY \n B = Z + 3X + 3Y \n C = Z + 3(X + Y) \n D = Z + X + Y ")
    P13.set("Cuatro veces Z menos 3 veces la suma de X y Y es: \n\n A = 4Z – 3X +3Y \n B = 4Z – 3 ( X + Y )  \n C = 4Z + 3XY \n D = 4Z - 3X + Y")
    P14.set("Z mas el producto de X y Y es: \n\n A = Z + XY \n B = Z - (X + Y)  \n C = Z (X Y) \n D = Z+ (X) + (Y) ")
    P15.set("El perímetro P de un rectangulo es igual al doble de la suma de su longitud L y su anchura W: \n\n A = P = 2 ( L + W ) \n B =  P = 2L + W  \n C = P= 2L + 2W \n D = P= 4L + W")
    listaN3 = [P11,P12,P13,P14,P15]
    N3=random.choice(listaN3)

    P16.set("¿Cual es el valor de X para la siguiente operación?: \n\n 6X = - 6 \n\n A = 6 \n B = 1 \n C = -1 \n D = 0")
    P17.set("¿Cual es el valor de X para la siguiente operación?: \n\n 64X = 16 \n\n A = 4 \n B = -1/4 \n C = 80 \n D = 48")
    P18.set("¿Cual es el valor de X para la siguiente operación?: \n\n X / 4 = 8 \n\n A = 32 \n B = 2 \n C = 12 \n D = 16")
    P19.set("¿Cual es el valor de X para la siguiente operación?: \n\n 5X + 3 = 4X + 9 \n\n A = 14 \n B = 24 \n C = 6 \n D = 12")
    P20.set("¿Cual es el valor de X para la siguiente operación?: \n\n 5X – 7 = 13X + 1  \n\n A = 1 \n B = -1 \n C = 2 \n D = -2")
    listaN4 = [P1,P2,P3,P4,P5]
    N4=random.choice(listaN4)

    P21.set("Calcula el valor de X y Y cuando X = 3Y: \n\n 4X + 5Y = 170 \n\n A =  X=30 Y=10\n B =  X=3 Y=1 \n C =  X=-30 Y=10 \n D =  X=40 Y=7")
    P22.set("Calcula el valor de X y Y cuando X = 3 : \n\n 5X + Y – 3 = 0  \n\n A =  X=3 Y=12\n B =  X=3 Y=13\n C =  X=-3 Y=10 \n D =  X=0 Y=7")
    P23.set("Calcula el valor de X y Y cuando Y = 3 : \n\n 3X + Y = 15 \n\n A =  X=6 Y=3\n B =  X=3 Y=3 \n C =  X=-3 Y=10 \n D =  X=4 Y=7")
    P24.set("Calcula el valor de X y Y cuando Y = -1: \n\n 2 + ( - 10 ) = \n\n A =  X=-3 Y=-1\n B =  X=3 Y=1 \n C =  X=-30 Y=10 \n D =  X=0 Y=-1")
    P25.set("Calcula el valor de X y Y cuando X = 0: \n\n 4X + 10Y = 170 \n\n A =  X30 Y=17\n B =  X=0 Y=14 \n C =  X=0 Y=18 \n D =  X=0 Y=7")
    listaN5 = [P21,P22,P23,P24,P25]
    N5=random.choice(listaN5)



    def muestraPregunta(N):
        cajaPreguntas =Label(juego,bg="black",fg="White",textvariable=N,state=DISABLED)
        cajaPreguntas.place(x=50,y=50,width=400, height=150)
    
    N=N1
    def respuesta():

        def correcto():
            puntaje =0
            L=1
            puntaje= puntaje + 1
            L= L+1
            messagebox.showinfo("¡Felicidades!", message="{}, su respuesta es correcta. Puntaje: {}".format("Usuario",puntaje))
            A.deselect()
            B.deselect()
            C.deselect()
            D.deselect()
            
            
        
        def incorrecto():
            messagebox.showinfo("Lo sentimos :(", message="{}, su respuesta es incorrecta.\n\n Su puntaje es: 0".format("Usuario"))
            Jugar().destroy()

        def nivel5():
            N=N5
            if N5==P21:
                if opcion.get()==1:
                    correcto()
                else:
                    incorrecto()
            elif N5==P22:
                if opcion.get()==2:
                    correcto()
                else:
                    incorrecto()
            elif N5==P23:
                if opcion.get()==1:
                    correcto()
                else:
                    incorrecto()
            elif N5==P24:
                if opcion.get()==1:
                    correcto()
                else:
                    incorrecto()
            else:
                if opcion.get()==1:
                    correcto()
                else:
                    incorrecto()

        def nivel4():
            N=N4
            if N4==P16:
                if opcion.get()==3:
                    correcto()
                    muestraPregunta(N5)
                    nivel3(N5)
                else:
                    incorrecto()
            elif N4==P17:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N5)
                    nivel3(N5)
                else:
                    incorrecto()
            elif N4==P18:
                if opcion.get()==1:
                    correcto()
                    muestraPregunta(N5)
                    nivel3(N5)
                else:
                    incorrecto()        
            elif N4==P19:
                if opcion.get()==4:
                    correcto()
                    muestraPregunta(N5)
                    nivel3(N5)
                else:
                    incorrecto()
            else:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N5)
                    nivel3(N5)
                else:
                    incorrecto()
        
        def nivel3():
            N=N3
            if N3==P11:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N4)
                    nivel3(N4)
                else:
                    incorrecto()
            elif N3==P12:
                if opcion.get()==3:
                    correcto()
                    muestraPregunta(N4)
                    nivel3(N4)
                else:
                    incorrecto()
            elif N3==P13:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N4)
                    nivel3(N4)
                else:
                    incorrecto()
            elif N3==P14:
                if opcion.get()==1:
                    correcto()
                    muestraPregunta(N4)
                    nivel3(N4)
                else:
                    incorrecto()
            else:
                if opcion.get()==1:
                    correcto()
                    muestraPregunta(N4)
                    nivel3(N4)
                else:
                    incorrecto()

        def nivel2():
            N=N2
            if N2==P6:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N3)
                    nivel3(N3)
                else:
                    incorrecto()
            elif N2==P7:
                if opcion.get()==1:
                    correcto()
                    muestraPregunta(N3)
                    nivel3(N3)
                else:
                    incorrecto()
            elif N2==P8:
                if opcion.get()==3:
                    correcto()
                    muestraPregunta(N3)
                    nivel3(N3)
                else:
                    incorrecto()
            elif N2==P9:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N3)
                    nivel3(N3)
                else:
                    incorrecto()
            else:
                if opcion.get()==1:
                    correcto()
                    muestraPregunta(N3)
                    nivel3(N3)
                else:
                    incorrecto()
        def nivel1():
            nivel = 1
            if N1==P1:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N2)
                    nivel2()
                else:
                    incorrecto()
            elif N1==P2:
                if opcion.get()==2:
                    correcto()
                    muestraPregunta(N2)
                    nivel2()
                else:
                    incorrecto()
            elif N1==P3:
                if opcion.get()==1:
                    correcto()
                    muestraPregunta(N2)
                    nivel2()
                else:
                    incorrecto()        
            elif N1==P4:
                if opcion.get()==3:
                    correcto()
                    muestraPregunta(N2)
                    nivel2()
                else:
                    incorrecto()
            else:
                if opcion.get()==4:
                    correcto()
                    muestraPregunta(N2)
                    nivel2()
                else:
                    incorrecto()
            N = N2
        if N==N1:
            nivel1()
        elif N==N2:
            nivel2()
        elif N==N3:
            nivel3()
        elif N==N4:
            nivel4()
        else:
            nivel5()
     
    muestraPregunta(N1)


    
    etiquetaPreguntas=Label(juego,bd=6,text="Pregunta categoria: ", bg=colorFondo, fg=colorLetra)
    etiquetaPreguntas.place(x=50,y=20)

    cajaCategoria= Label(juego,bd=3,bg="white",fg="red", text ="1" , state=DISABLED)
    cajaCategoria.place(x=170,y=20,width=50)

    etiquetaOpcion = Label(juego, text="Opciones de respuesta: ", bg=colorFondo, fg=colorLetra)
    etiquetaOpcion.place(x=50, y=220) 

    A = Radiobutton(juego,text="A. ",value=1, bg="gray",variable=opcion,bd=5)
    A.place(x=75,y=250)
    B = Radiobutton(juego,text="B. ",value=2, bg="gray", variable=opcion,bd=5)
    B.place(x=175,y=250)
    C = Radiobutton(juego,text="C. ",value=3, bg="gray",variable=opcion,bd=5)
    C.place(x=275,y=250)
    D = Radiobutton(juego,text="D. ",value=4, bg="gray",variable=opcion,bd=5)
    D.place(x=375,y=250)

    botonRendirse = Button(juego, text="Rendirse", bg="green",fg="white")
    botonRendirse.place(x=120, y=320,width=70) 

    botonContinuar = Button(juego, text="Continuar", bg="green",fg="white",command=respuesta)
    botonContinuar.place(x=300, y=320,width=70) 

    juego.mainloop()


etiquetaUsuario = Label(ingreso, text="USUARIO: ", bg=colorFondo, fg=colorLetra)
etiquetaUsuario.place(x=50, y=20) 
entradaUsuario = Entry(ingreso, textvariable=usuario)
entradaUsuario.place(x=120, y=20, width=130) 

botonJugar = Button(ingreso, text="Jugar", bg="green",fg="white",command=Jugar)
botonJugar.place(x=120, y=50,width=70) 


ingreso.mainloop()