import turtle


def get_coordinates(x, y):
    print(f"Clicked coordinates: ({x}, {y})")


# Create a screen object
screen = turtle.Screen()


# Register the click event and call the get_coordinates function
screen.onclick(get_coordinates)

# Run the turtle main loop
turtle.mainloop()
