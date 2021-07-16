from tkinter import *

if __name__ == '__main__':

    expresion = ''

    def click_boton(texto_boton):
        global expresion
        expresion+=texto_boton
        pantallita.delete(0,END)
        pantallita.insert(0,expresion)

    def limpiar_pantalla():
        global expresion
        expresion = ''
        pantallita.delete(0,END)

    def calcular():
        global expresion
        print(expresion)
        try:
            resultado = eval(pantallita.get())
            expresion = str(resultado)
        except:
            resultado = "Error de sintaxis"
            expresion = ''  
        pantallita.delete(0,END)
        pantallita.insert(0,resultado)

    ventana = Tk()
    ventana.title("Python Calc")

    pantallita = Entry(ventana, justify=RIGHT, bg='lightyellow', fg='red')
    pantallita.grid(row=0, column=0, columnspan=5,  sticky="nsew")

    siete = Button(ventana, text=" 7 ", command=lambda: click_boton('7')).grid(row=1, column=0,  sticky="nsew")
    ocho = Button(ventana, text=" 8 ", command=lambda: click_boton('8')).grid(row=1, column=1,  sticky="nsew")
    nueve = Button(ventana, text=" 9 ", command=lambda: click_boton('9')).grid(row=1, column=2,  sticky="nsew")
    division = Button(ventana, text=" / ", command=lambda: click_boton('/')).grid(row=1, column=3,  sticky="nsew")
    p_izquierdo = Button(ventana, text=" ( ", command=lambda: click_boton('(')).grid(row=1,column=4, sticky="nsew")

    cuatro = Button(ventana, text=" 4 ", command=lambda: click_boton('4')).grid(row=2, column=0,  sticky="nsew")
    cinco = Button(ventana, text=" 5 ", command=lambda: click_boton('5')).grid(row=2, column=1,  sticky="nsew")
    seis = Button(ventana, text=" 6 ", command=lambda: click_boton('6')).grid(row=2, column=2,  sticky="nsew")
    multiplicacion = Button(ventana, text=" x ", command=lambda: click_boton('*')).grid(row=2, column=3,  sticky="nsew")
    p_derecho = Button(ventana, text=" ) ", command=lambda: click_boton(')')).grid(row=2,column=4, sticky="nsew")

    uno = Button(ventana, text=" 1 ", command=lambda: click_boton('1')).grid(row=3, column=0,  sticky="nsew")
    dos = Button(ventana, text=" 2 ", command=lambda: click_boton('2')).grid(row=3, column=1,  sticky="nsew")
    tres = Button(ventana, text=" 3 ", command=lambda: click_boton('3')).grid(row=3, column=2,  sticky="nsew")
    resta = Button(ventana, text=" - ", command=lambda: click_boton('-')).grid(row=3, column=3,  sticky="nsew")
    potencia = Button(ventana, text=" ^ ", command=lambda: click_boton('**')).grid(row=3,column=4, sticky="nsew")

    cero = Button(ventana, text=" 0 ", command=lambda: click_boton('0')).grid(row=4, column=0,  sticky="nsew")
    punto = Button(ventana, text=" . ", command=lambda: click_boton('.')).grid(row=4, column=1,  sticky="nsew")
    igual = Button(ventana, text=" = ", command=calcular).grid(row=4, column=2,  sticky="nsew")
    suma = Button(ventana, text=" + ", command=lambda: click_boton('+')).grid(row=4, column=3,  sticky="nsew")
    clear = Button(ventana, text="CLS", command=limpiar_pantalla).grid(row=4,column=4, sticky="nsew")

    ventana.mainloop()

    # ( ) exp CLS