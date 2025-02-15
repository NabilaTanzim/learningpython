import turtle

# Create a screen for drawing
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color

# Create a turtle for drawing
t = turtle.Turtle()
t.shape("turtle")  # Optional: makes the cursor look like a turtle

# Set the turtle speed (0 is fastest)
t.speed(2)

# Draw a square
for _ in range(400):  # Loop for four sides
    t.forward(1)  # Move the turtle forward by 100 units
    t.left(0.5)      # Turn the turtle left by 90 degrees
for _ in range(350):  # Loop for four sides
    t.back(2)  # Move the turtle forward by 100 units
    t.right(0.5)      # Turn the turtle left by 90 degrees
# Hide the turtle after drawing
t.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
