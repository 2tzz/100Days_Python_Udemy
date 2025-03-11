# Day 20 - Build the Snake Game Part 1: Animation & Coordinates
## Snake Game Part 1

![](snake_game1.gif)


## Exercises
### Create the Snake's Body 
**Instructions:**
- Create 3 squares/turtles from the Turtle() class and line them up next to each other to represent a snake that consists of 3 segments.

**Code**
<details><summary>Solution</summary>
<p>

```Python
x_coord = [0, -20, -40]

for position in range(0, 3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x_coord[position],y=0)
```

</p>
</details>

#

### Animate and Make the Snake Move
**Instructions:**
- Move the snake automatically across the screen without having to do or press anything.
- Modifyed the code so that when the snake's 1st segment changes direction, the rest of the segments follow it and don't continue forward.

**Code**
<details><summary>Solution</summary>
<p>

```Python
segments = []

for position in range(0, 3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=x_coord[position],y=0)
    segments.append(snake)

game_running = True
while game_running:
	for seg in segments:
		seg.forward(20)
```

</p>
</details>

**Code**
<details><summary>Solution</summary>
<p>

```Python
game_running = True
while game_running:
	screen.update()
	time.sleep(1)

	for seg_num in range(len(segments) - 1, 0, -1):
		new_x = segments[seg_num - 1].xcor()
		new_y = segments[seg_num - 1].ycor()
		segments[seg_num].goto(new_x, new_y)
	segments[0].forward(20)
```

</p>
</details>

#

### Control the Snake's Movement Direction
**Instructions:**
- Define functions that will bind to the corresponding key press to change the direction of the snake's path.

**Code**
<details><summary>main.py file</summary>
<p>

```Python
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

</p>
</details>

**Code**
<details><summary>snake.py file</summary>
<p>

```Python

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
```

</p>
</details>
