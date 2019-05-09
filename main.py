import turtle

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgreen')
        self.__startLine = -width/2 +20 #linea de salida
        self.__finishLine = width/2 -20 #línea de llegada
    
        self.__createRunners()
    
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
        
if __name__=='__main__':#usamos esta función para probar el programa aquí en main y que al importarlo en otro programa no se ejecute esta parte
    circuito = Circuito(640,480)
    