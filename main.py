from turtle import *
import turtle
from sys import exit as abort
from os.path import isfile
from random import randint

# Student details
student_number = 11888288  
student_name = "Your Name"

# Check student details
if not isinstance(student_number, int) or not isinstance(student_name, str):
    print('\nUnable to run: Invalid student details, aborting!\n')
    abort()

# Check for configuration and data modules
config_file = 'config.py'
data_file = 'data.py'

if isfile(config_file) and isfile(data_file):
    print('\nConfiguration and Data generation modules found ...\n')
    from config import create_drawing_canvas, release_drawing_canvas, cell_size, grid_width, grid_height
    from data import test_cases, raw_data 
else:
    print('\nRequired module files missing, aborting!\n')
    abort()

# Mapping months to x-coordinates
month_to_x = {
    'January': -4.5 * cell_size, 'February': -3.5 * cell_size, 'March': -2.5 * cell_size,
    'April': -1.5 * cell_size, 'May': -0.5 * cell_size, 'June': 0.5 * cell_size,
    'July': 1.5 * cell_size, 'August': 2.5 * cell_size, 'September': 3.5 * cell_size,
    'October': 4.5 * cell_size, 'November': 5.5 * cell_size, 'December': 6.5 * cell_size
}

# Define a function to draw the investment symbol
def draw_rounded_rectangle(center_x, center_y, width, height, color):

    # Set up the turtle to start drawing
    fillcolor(color)
    pencolor('black')
    pensize(2)
    penup()

    # Calculate the corner radius
    corner_radius = min(width, height) / 5

    # Move to the starting position (bottom left corner)
    goto(center_x - width / 2 + corner_radius, center_y - height / 2)
    pendown()

    # Start filling the shape
    begin_fill()

    # Bottom side
    forward(width - 2 * corner_radius)
    circle(corner_radius, 90)

    # Right side
    forward(height - 2 * corner_radius)
    circle(corner_radius, 90)

    # Top side
    forward(width - 2 * corner_radius)
    circle(corner_radius, 90)

    # Left side
    forward(height - 2 * corner_radius)
    circle(corner_radius, 90)

    # Finish filling
    end_fill()
    penup()

def draw_eyes(x, y):
    turtle.pensize(1)
    for i in range(-1, 2, 2): 
        turtle.goto(x + i * 5, y + 10)
        turtle.pendown()
        turtle.dot()
        turtle.penup()

def draw_ears(x, y):
    ear_width = 4
    ear_height = 8
    turtle.penup()
    # Left ear
    turtle.goto(x - 10, y + 20)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(ear_width, 90)
        turtle.circle(ear_height, 90)
    turtle.end_fill()
    turtle.penup()
    # Right ear
    turtle.goto(x + 10, y + 20)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(ear_width, 90)
        turtle.circle(ear_height, 90)
    turtle.end_fill()
    turtle.penup()


def draw_sheep(x, y, orientation, color):
    # Draw the sheep's body as a rounded rectangle
    turtle.fillcolor(color)
    body_width = 60
    body_height = 40
    draw_rounded_rectangle(x, y, body_width, body_height, color)

    # Calculate positions of other components based on orientation
    head_offset_y = body_height / 4 if orientation != 'down' else -body_height / 1 

    # sheep's head as a circle
    head_radius = 15
    turtle.penup()
    goto(x, y + head_offset_y)
    turtle.pendown()
    turtle.begin_fill()
    circle(head_radius)
    turtle.fillcolor('white')
    end_fill()

    # sheep's ears as small circles or ovals
    draw_ears(x, y + head_offset_y)

    # sheep's eyes as dots
    draw_eyes(x, y + head_offset_y)

    # Reset turtle state
    pensize(1)
    turtle.color('black')
    penup()
    setheading(0)

# Visualize data function with drawing symbols
def visualise_data(data_points):
    # Define the drawing canvas limits based on the grid size
    max_y = (grid_height // 2) * cell_size
    min_y = -(grid_height // 2) * cell_size
    safety_margin = 5  

    # Turn off animation for faster drawing
    tracer(False)

    for month, value in data_points:
        x = month_to_x[month]
        orientation = 'up' if value > 0 else 'down' if value < 0 else 'flat'
        if value == 0:
            # Draw a single blue sheep at level 0
            draw_sheep(x, 0, 'right', 'deepskyblue')
        else:
            # Determine the color based on the value
            color = 'darkseagreen' if value > 0 else 'coral'

            # Determine the orientation based on the value
            orientation = 'up' if value > 0 else 'down'

            # Modify the range to include the actual value by adding 1 or -1 accordingly
            range_end = value + (1 if value > 0 else -1)

            # Draw a sheep for each level from 0 to the value (inclusive)
            for i in range(0, range_end, (1 if value > 0 else -1)):
                # Calculate the Y coordinate for the sheep
                y = i * cell_size

                # Ensure the sheep is drawn within the grid limits
                y = max(min_y + safety_margin, min(y, max_y - safety_margin))

                draw_sheep(x, y, orientation, color)

    # Update the screen with all the drawings
    update()



# Define a function to calculate the total profit
def calculate_total_profit(data_points):
    total_profit = sum(value for _, value in data_points)
    return total_profit

def display_text(text, x, y, font_size=14, color='black'):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align='right', font=('Arial', font_size, 'normal'))
    turtle.hideturtle()




def main():
    create_drawing_canvas('Financial Report Visualisation by ' + student_name)
    test_case_index = 0
    data = raw_data(test_cases[test_case_index][2])
    visualise_data(data)
    # Calculate the total profit
    total_profit = calculate_total_profit(data)
    # Display total profit on the screen in the bottom left corner
    display_text(f"Total profit ($bn): {total_profit}", -(grid_width // 2) * cell_size + 20, -((grid_height // 2) * cell_size) - 20, font_size=16, color='black')
    release_drawing_canvas(student_name)

if __name__ == "__main__":
    main()

