# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

import turtle
import os

# Velocidade inicial
INITIAL_SPEED = 0.1
# A cada rebatida a bola aumenta em 7,5% a velocidade
SPEED_INCREASE = 0.0075

# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

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
ball.dx = INITIAL_SPEED
ball.dy = INITIAL_SPEED

# pontuação
score_1 = 0
score_2 = 0

# head-up display da pontuação
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
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
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
    if ball.ycor() < -280:
        os.system("afplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    #colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P",24,"normal") )
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0,0)
        # Reiniciando a velocidade
        ball.dx = INITIAL_SPEED
        ball.dy = INITIAL_SPEED
        ball.dx *= -1
    
    #colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P",24,"normal") )
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0,0)
        # Reiniciando a velocidade
        ball.dx = INITIAL_SPEED
        ball.dy = INITIAL_SPEED      
        ball.dx *= -1


    # colisão com raquete 1
    if ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        if (ball.dx < 0):
            ball.dx -= SPEED_INCREASE
            if (ball.dy < 0):
                ball.dy -= SPEED_INCREASE
            else:
                ball.dy += SPEED_INCREASE
        else:
            ball.dx += SPEED_INCREASE
            if (ball.dy >= 0):
                ball.dy += SPEED_INCREASE
            else:
                ball.dy -= SPEED_INCREASE    
        os.system("afplay bounce.wav&")   
    
    # colisão com raquete 2
    if ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        if (ball.dx < 0):
            ball.dx -= SPEED_INCREASE
            if (ball.dy < 0):
                ball.dy -= SPEED_INCREASE
            else:
                ball.dy += SPEED_INCREASE
        else:
            ball.dx += SPEED_INCREASE
            if (ball.dy >= 0):
                ball.dy += SPEED_INCREASE
            else:
                ball.dy -= SPEED_INCREASE
        os.system("afplay bounce.wav&")