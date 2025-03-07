# Day 18 - Turtle & The Graphical User Interface (GUI)
## Hirst Painting

![](hirst_painting.gif)


## Python Turtle Exercises
- Draw a Square
- Draw a Dashed Line
- Drawing Different Shapes
- Generate a Random Walk
- Draw a Spirograph

**Using Colorgram to Extract Colors of a JPG:**
-

**Code**
<details><summary>Solution</summary>
<p>

```Python
import colorgram

# Extract 25 colors from jpg image.
colors = colorgram.extract("image.jpg", 25)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
```

</p>
</details>

#
