from turtle import *
from random import randrange as rnd

def up_press():
    global m
    m += 1 # ускорение
 
def down_press():
    global m
    m -= 1
     
def left_press():
    global a
    a -= 2 # крутизна поворота
 
def right_press():
    global a
    a += 2 
         
def space_press():
    global m,a
    shape('turtle') # форма - черепашка
    reset() # очистить экран и сбросить все настройки
    speed(0) # скорость прорисовки максимальна
    width(3) # толщина линии
    m = 0 # скорость движения
    a = 0 # скорость поворота
    color(1,1,0)        
def move():
    global a
    rt(a) # повернуть на угол
    fd(m) # двигаться вперед
    a /= 1.2 # угол поворота уменьшить
    ontimer(move,30)

def r_press():
    color("red")
def y_press():
    color("yellow")
def g_press():
    color("green")
def p_press():
    color("deep pink")
def b_press():
    color("brown")
def u_press():
    penup()
def d_press():
    pendown()
space_press() # сброс настроек
listen() # слушать нажатие клавиш
onkey(up_press,"Up")
onkey(down_press,"Down")
onkey(left_press,"Left")
onkey(right_press,"Right")
onkey(space_press,"space")
onkey(r_press, "r")
onkey(y_press, "y")
onkey(g_press, "g")
onkey(p_press, "p")
onkey(b_press, "b")
onkey(u_press, "u")
onkey(d_press, "d")
move()
 
done()
