import turtle
import time
import random as rd

# declaring the variables
delay = 0.1
score = 0
high_score = 0
cols = ['red','pink','magenta','mistyrose','paleturquoise3','purple1','plum3','black','brown','grey','yellow','dodgerblue2','goldenrod2']
col = rd.choice(cols)
# firstly lemme create a window for the game

window = turtle.Screen()
window.title("Formal Snake Game")
window.bgcolor("lawngreen")
window.setup(width=600, height=600)
window.tracer(0) # i've used this function to speed upp the programme

# done with the window, now i can start creating the snake, say lemme start with the head
snake_head = turtle.Turtle()
snake_head.shape('circle')
snake_head.color('Orangered')
snake_head.speed(0)
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# snake's food
snake_food = turtle.Turtle()
snake_food.shape('circle')
snake_food.color(col)
snake_food.speed(0)
snake_food.penup()
snake_food.goto(0,200)

snake_body=[] # this list is created to add segemnts to the snake when snake eats the food

# to display the score i will create a score tab and a highscore tab
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Scored : 0 \t\t Highscore : 0", align="center", font=("Verdana", 18, "normal"))

# function declaration part
def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = "top"


def go_down():
    if snake_head.direction != 'up':
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != 'right':
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != 'left':
        snake_head.direction = "right"


def move():
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x+20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x-20)
    if snake_head.direction == "top":
        y = snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y-20)


# keyboard bindings
window.listen()
window.onkey(go_up, 'w')
window.onkey(go_down, 's')
window.onkey(go_left, 'a')
window.onkey(go_right, 'd')

# the main game's loop goes this way
while True:
    window.update()

    # check if the food is contacted to snake
    if snake_head.distance(snake_food) < 20 :
        # this will move the food to a random spot
        x = rd.randint(-290, 290)
        y = rd.randint(-290, 290)
        snake_food.goto(x, y)
        new_col = rd.choice(cols)
        snake_food.color(new_col)
        # this will  add body to snake
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape('square')
        new_body.color(new_col)
        new_body.penup()
        snake_body.append(new_body)

        # shorten the delay to adjust the speed
        delay -= 0.001

        # this will increase the score
        score += 1
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Scored : {} \t\t Highscore : {}".format(score, high_score), align="center", font=("Verdana", 18, "normal"))

    # moving the end segments in the reverse order
    for i in range(len(snake_body)-1,0,-1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x, y)

    # move the segment 0 where the head is
    if len(snake_body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x, y)

    # to stop if the snake hits the wall
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"

        # moving away the snake's body
        for seg in snake_body:
            seg.goto(1000, 1000)
        # clear the snake body
        snake_body.clear()

        # reset the delay
        delay = 0.1

        #clear the score
        score = 0
        pen.clear()
        pen.write("Scored : {} \t\t Highscore : {}".format(score, high_score), align="center",
                  font=("Verdana", 18, "normal"))


    move()

    # to check the collision with the body of the snake
    for seg in snake_body:
        if seg.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = 'stop'

            # moving away the snake's body
            for segment in snake_body:
                segment.goto(1000, 1000)
            # clear the snake body
            snake_body.clear()

            # reset the delay
            delay = 0.1

            # clear the score
            score = 0
            pen.clear()
            pen.write("Scored : {} \t\t Highscore : {}".format(score, high_score), align="center",
                      font=("Verdana", 18, "normal"))

    time.sleep(delay)
window.mainloop()

