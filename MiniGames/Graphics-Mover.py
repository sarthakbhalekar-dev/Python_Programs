
import turtle

# ---------- WINDOW ----------

screen = turtle.Screen()
screen.title("Babbage the Turtle")
screen.setup(width=950, height=700)
screen.bgcolor("#121216")

# ---------- BABBAGE ----------

babbage = turtle.Turtle()
babbage.shape("turtle")
babbage.color("#00D2FF")
babbage.pensize(3)
babbage.speed(6)

move_distance = 30
turn_angle = 30
drawing = True

# ---------- COLORS ----------

colors = {
    "1": "#00D2FF",
    "2": "#FF6B6B",
    "3": "#51CF66",
    "4": "#FFD43B",
    "5": "#CC5DE8",
    "6": "#FFFFFF"
}

# ---------- INFORMATION PANEL ----------

info = turtle.Turtle()
info.hideturtle()
info.penup()
info.color("white")


def update_info():
    info.clear()

    status = "ON" if drawing else "OFF"

    info.goto(-450, 295)
    info.write(
        "BABBAGE THE TURTLE  |  "
        f"Pen: {status}  |  "
        f"Move: {move_distance}  |  "
        f"Size: {babbage.pensize()}",
        font=("Arial", 13, "bold")
    )

    info.goto(-450, -295)
    info.write(
        "Arrows: Move/Turn | Space: Pen | "
        "1-6: Colors | +/-: Move | [ ]: Pen Size",
        font=("Arial", 11, "normal")
    )

    info.goto(-450, -320)
    info.write(
        "C: Circle | S: Square | T: Star | "
        "R: Reset | X: Clear | Q: Quit",
        font=("Arial", 11, "normal")
    )


# ---------- MOVEMENT ----------

def forward():
    babbage.forward(move_distance)


def backward():
    babbage.backward(move_distance)


def left():
    babbage.left(turn_angle)


def right():
    babbage.right(turn_angle)


# ---------- PEN CONTROLS ----------

def toggle_pen():
    global drawing

    drawing = not drawing

    if drawing:
        babbage.pendown()
    else:
        babbage.penup()

    update_info()


def change_color(key):
    babbage.pencolor(colors[key])


def increase_size():
    babbage.pensize(
        min(babbage.pensize() + 1, 15)
    )
    update_info()


def decrease_size():
    babbage.pensize(
        max(babbage.pensize() - 1, 1)
    )
    update_info()


# ---------- MOVEMENT DISTANCE ----------

def increase_move():
    global move_distance

    move_distance = min(move_distance + 10, 100)
    update_info()


def decrease_move():
    global move_distance

    move_distance = max(move_distance - 10, 10)
    update_info()


# ---------- DRAW SHAPES ----------

def draw_square():
    for _ in range(4):
        babbage.forward(100)
        babbage.right(90)


def draw_circle():
    babbage.circle(50)


def draw_star():
    for _ in range(5):
        babbage.forward(120)
        babbage.right(144)


# ---------- RESET AND CLEAR ----------

def reset_turtle():
    global drawing

    babbage.penup()
    babbage.home()
    babbage.setheading(0)

    drawing = True
    babbage.pendown()

    update_info()


def clear_drawing():
    babbage.clear()
    update_info()


# ---------- KEYBOARD CONTROLS ----------

screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.onkey(toggle_pen, "space")

# Color shortcuts
for key in colors:
    screen.onkey(
        lambda k=key: change_color(k),
        key
    )

# Movement controls
screen.onkey(increase_move, "plus")
screen.onkey(increase_move, "equal")
screen.onkey(decrease_move, "minus")

# Pen thickness
screen.onkey(increase_size, "bracketright")
screen.onkey(decrease_size, "bracketleft")

# Shapes
screen.onkey(draw_circle, "c")
screen.onkey(draw_square, "s")
screen.onkey(draw_star, "t")

# Reset and clear
screen.onkey(reset_turtle, "r")
screen.onkey(clear_drawing, "x")

# Quit
screen.onkey(screen.bye, "q")

# ---------- START ----------

update_info()
screen.listen()
screen.mainloop()
