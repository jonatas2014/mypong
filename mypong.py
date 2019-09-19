import turtle
import os

# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer()

#desenhar raquete 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

#desenhar raquete 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

#desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 4
ball.dy = 4

score_1 = 0
score_2 = 0

hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P",24,"normal") )

# mover raquete 1
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# mapeando as teclas
screen.listen()
screen.onkeypress(paddle_1_up,"w")
screen.onkeypress(paddle_1_down,"s")
screen.onkeypress(paddle_2_up,"Up")
screen.onkeypress(paddle_2_down,"Down")

while True:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #colisão com parede superior
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1
    
    #colisão com parede inferior
    if ball.ycor() < -290:
        os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

    #colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P",24,"normal") )
        ball.goto(0,0)
        ball.dx *= -1
    
    #colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P",24,"normal") )
        ball.goto(0,0)
        ball.dx *= -1


    # colisão raquetes
    if ball.xcor() < -340 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1     
        os.system("afplay bounce.wav&")   
    
    if ball.xcor() > 340 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")