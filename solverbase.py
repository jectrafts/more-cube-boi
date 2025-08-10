from twophase import solver as tw


# white = ['yellow', 'red', 'blue', 'white', 'white', 'red', 'yellow', 'yellow', 'red']
# yellow = ['yellow', 'blue', 'red', 'blue', 'yellow', 'blue', 'red', 'green', 'white']
# red = ['blue', 'orange', 'blue', 'orange', 'red', 'red', 'red', 'yellow', 'blue']
# orange= ['white', 'yellow', 'green', 'orange', 'orange', 'green', 'orange', 'yellow', 'green']
# green = ['orange', 'green', 'orange', 'orange', 'green', 'blue', 'white', 'red', 'green']
# blue = ['white', 'white', 'orange', 'green', 'blue', 'white', 'yellow', 'white', 'green']

white = ['white', 'yellow', 'yellow', 'yellow', 'white', 'red', 'white', 'blue', 'white']
yellow = ['yellow', 'white', 'green', 'white', 'yellow', 'green', 'green', 'yellow', 'red']
red = ['orange', 'orange', 'red', 'white', 'red', 'red', 'green', 'blue', 'orange']
orange= ['blue', 'blue', 'green', 'blue', 'orange', 'white', 'yellow', 'green', 'red']
green = ['red', 'orange', 'blue', 'red', 'green', 'green', 'yellow', 'orange', 'orange']
blue = ['blue', 'green', 'orange', 'yellow', 'blue', 'red', 'white', 'orange', 'blue']





faces = [white, blue, red, yellow, green, orange]

# Create color map based on center stickers
color_map = {
    'white': 'U',   # white center
    'blue': 'R',    # blue center
    'red': 'F',     # red center
    'yellow': 'D',  # yellow center
    'green': 'L',   # green center
    'orange': 'B'   # orange center
}

# Convert to 54-letter cube string
cube_str = ''.join(color_map[color] for face in faces for color in face)

# Solve
solution = tw.solve(cube_str)

# Output
print("Cube string:", cube_str)
print("Solution:", solution)
print(len(solution))



