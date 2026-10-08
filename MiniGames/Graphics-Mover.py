import turtle

wn = turtle.Screen()
wn.title("Babbage the Turtle")
wn.bgcolor("#121216")  # Optional dark background

babbage = turtle.Turtle()
babbage.shape("turtle")
babbage.color("#00D2FF")  # Custom turtle color

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


# Key Bindings
wn.onkey(forward, "Up")
wn.onkey(backward, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")

# Essential settings for listening & keeping window open
wn.listen()
wn.mainloop()