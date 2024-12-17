# Import time
import time as tick
# Import Turtle library to utilize basic graphics
# Rename to graphics
import turtle as graphics

# Initialize ball direction, bigger numbers increases ball speed
ballDirX = 4
ballDirY = 4

# Initialize player scores
playerScoreX = 0
playerScoreY = 0

# Determine game FPS
animationSpeed = 60
# Calculate game tick
gameTick = 1.0 / float(animationSpeed)

# Store time since program start
startTime = tick.time()

# Initialize game indow
window = graphics.Screen()
# Rename window to "Pong"
window.title("Pong")
# Set window background color
window.bgcolor("#333333")
# Set window width and height
window.setup(width = 800, height = 600)
# Disables Turtle animations
window.tracer(0)

# Initialize title text
title = graphics.Turtle()
# Sets Turtle's initial speed during the drawing of the object, not needed if Turtle animations are disabled
# title.speed(animationSpeed)
# Set title color
title.color("white")
# This removes the line created by the Turtle
title.penup()
# Hides the Turtle that's drawing the graphics
title.hideturtle()
# Moves Turtle to the specified coordinates
title.goto(0, 250)
# Write text with the specified font
title.write("⌊ ---- PONG ---- ⌉", font = ("Inter", 15, "bold"), align = "center")

# Initialize score text
score = graphics.Turtle()
# Sets Turtle's initial speed during the drawing of the object, not needed if Turtle animations are disabled
# score.speed(animationSpeed)
# Set score color
score.color("white")
# This removes the line created by the Turtle
score.penup()
# Hides the Turtle that's drawing the graphics
score.hideturtle()
# Moves Turtle to the specified coordinates
score.goto(0, -250)
# Write text with the specified font
score.write(f"Player X: {playerScoreX} Player Y: {playerScoreY}", font = ("Inter", 15, "normal"), align = "center")

# Initialize left paddle
leftPaddle = graphics.Turtle()
# Sets Turtle's initial speed during the drawing of the object, not needed if Turtle animations are disabled
leftPaddle.speed(animationSpeed)
# Set paddle shape
leftPaddle.shape("square")
# Set paddle color
leftPaddle.color("red")
# Set paddle length and width
leftPaddle.shapesize(stretch_wid = 5, stretch_len = 1)
# This removes the line created by the Turtle
leftPaddle.penup()
# Moves Turtle to the left side of the screen with the specified coordinates
leftPaddle.goto(-350, 0)

# Initialize right paddle
rightPaddle = graphics.Turtle()
# Sets Turtle's initial speed during the drawing of the object, not needed if Turtle animations are disabled
rightPaddle.speed(animationSpeed)
# Set paddle shape
rightPaddle.shape("square")
# Set paddle color
rightPaddle.color("blue")
# Set paddle length and width
rightPaddle.shapesize(stretch_wid = 5, stretch_len = 1)
# This removes the line created by the Turtle
rightPaddle.penup()
# Moves Turtle to the left side of the screen with the specified coordinates
rightPaddle.goto(350, 0)

# Initialize ball
ball = graphics.Turtle()
# Sets Turtle's initial speed during the drawing of the object, not needed if Turtle animations are disabled
ball.speed(animationSpeed)
# Set ball shape
ball.shape("circle")
# Set ball color
ball.color("white")
# Set ball length and width
# ball.shapesize(stretch_wid = 1, stretch_len = 1)
# This removes the line created by the Turtle
ball.penup()
# Moves Turtle to the center of the screen with the specified coordinates, not needed as the object is initialized at 0, 0 by default
# ball.goto(5, 5)

# Left paddle up function
def leftPaddleUp() :
    yAxis = leftPaddle.ycor()
    leftPaddle.sety(yAxis + 50)

# Left paddle down function
def leftPaddleDown() :
    yAxis = leftPaddle.ycor()
    leftPaddle.sety(yAxis - 50)

# Right paddle up function
def rightPaddleUp() :
    yAxis = rightPaddle.ycor()
    rightPaddle.sety(yAxis + 50)

# Right paddle down function
def rightPaddleDown() :
    yAxis = rightPaddle.ycor()
    rightPaddle.sety(yAxis - 50)

# Listen for user inputs
window.listen()
# Requires a function as an argument to execute whenever a key is pressed
window.onkeypress(leftPaddleUp, "w")
# Requires a function as an argument to execute whenever a key is pressed
window.onkeypress(leftPaddleDown, "s")
# Requires a function as an argument to execute whenever a key is pressed
window.onkeypress(rightPaddleUp, "Up")
# Requires a function as an argument to execute whenever a key is pressed
window.onkeypress(rightPaddleDown, "Down")

# Game core function
def gameCore() :
    # Access ball direction as a global variable
    global ballDirX
    global ballDirY

    # Access player scores as a global variable
    global playerScoreX
    global playerScoreY

    # Access game tick as global variable
    global gameTick

    frameCount = 0

    # Main game loop (keeps program running)
    while True :
        # Updates screen
        window.update()

        # Count current frame
        frameCount += 1
        # This makes the overall game speed more consistent
        tick.sleep(gameTick)

        # Clear text
        title.clear()
        # Update FPS display
        title.write(f"⌊ ---- PONG ---- ⌉\n        FPS: {round(frameCount / (tick.time() - startTime))}", font = ("Inter", 15, "bold"), align = "center")

        # This changes the ball's position over time
        ball.setx(ball.xcor() + ballDirX)
        ball.sety(ball.ycor() + ballDirY)

        # Alternatively, we can use .goto() instead which is more accurate
        # ball.goto(ball.xcor() + ballDirX, ball.ycor() + ballDirY)

        # Check for collisions for top to bounce the ball
        if ball.ycor() > 290 :
            # ball.sety(290)
            ballDirY = -ballDirY

        # Check for collisions for bottom to bounce the ball
        if ball.ycor() < -290 :
            # ball.sety(-290)
            ballDirY = -ballDirY
        
        # Check if ball reached Player X's side
        if ball.xcor() > 390 :
            # Reset ball position
            ball.goto(0, 0)
            # Change the direction of the ball
            ballDirX = -ballDirX

            # Add score
            playerScoreX += 1

            # Clear text
            score.clear()
            # Update score display
            score.write(f"Player X: {playerScoreX} Player Y: {playerScoreY}", align = "center", font = ("Inter", 15, "normal"))
        
        # Check if ball reached Player Y's side
        if ball.xcor() < -390 :
            # Reset ball position
            ball.goto(0, 0)
            # Change the direction of the ball
            ballDirX = -ballDirX

            # Add score
            playerScoreY += 1

            # Clear text
            score.clear()
            # Update score display
            score.write(f"Player X: {playerScoreX} Player Y: {playerScoreY}", align = "center", font = ("Inter", 15, "normal"))
        
        # Check for collisions for Player X's paddle to bounce the ball
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40 :
            # ball.setx(340)
            ballDirX = -ballDirX

        # Check for collisions for Player Y's paddle to bounce the ball
        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftPaddle.ycor() - 40 :
            # ball.setx(-340)
            ballDirX = -ballDirX

# Initialize game core
gameCore()