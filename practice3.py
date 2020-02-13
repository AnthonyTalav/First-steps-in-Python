import turtle

def main():
    window=turtle.Screen()
    ninja=turtle.Turtle()
    make_square(ninja)
    window.mainloop()

def make_square(ninja):
    length=int(input('Escriba el tamaño del cuadrado: '))
    make_line_and_turn(ninja,length)

def make_line_and_turn(ninja, length):
    

    for i in range(4):
        ninja.forward(length)
        ninja.left(90)


if __name__=="__main__":
    main()