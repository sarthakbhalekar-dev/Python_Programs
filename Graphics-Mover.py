
import turtle
wn=turtle.Screen()
babbage=turtle.Turtle()
babbage.shape("turtle")

move_speed = 100
turn_angle = 90

def forward():
 babbage.forward(move_speed)


def backward():
  babbage.backward(move_speed)

def left():
 babbage.left(turn_angle)

def right():
  babbage.right(turn_angle)

wn.onkey(forward,"Up")
wn.onkey(backward,"Down")
wn.onkey(left,"Left")
wn.onkey(right,"Right")

