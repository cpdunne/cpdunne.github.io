import turtle


def draw_polygon(n_sides):
    side_length = 50
    screen = turtle.Screen()
    screen.bgcolor("pink")
    bingus = turtle.Turtle()
    anglesum = (n_sides - 2) * 180
    for i in range(n_sides):              
        bingus.forward(side_length)    
        bingus.left(180 - anglesum / n_sides)
    screen.exitonclick()
    # ADD Code to draw a regular polygon with the specified number of sides

def get_n_sides():
    validation = True
    while validation:
        n_sides = int(input("Enter the number of sides of a regular polygon: "))
        if n_sides >= 3 and n_sides <= 25:
            validation = False
        else:
            print("Invalid input! Number of sides must be between 3 and 25.")
    return n_sides
    # Add code to get the number of polygon sides (3-24) with input validation,
    # and return it
    

def main():
    n_sides = get_n_sides()
    draw_polygon(n_sides)
    # Add code to call get_n_sides(), save the value it returns,
    # Then call draw_polygon() to draw the polygon 

main()