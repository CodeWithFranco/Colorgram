import colorgram

# Extract 7 colors from image
colors = colorgram.extract('Colorgram.jpeg', 30)

# New list
rgb_colors = []

# Get the color code
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)