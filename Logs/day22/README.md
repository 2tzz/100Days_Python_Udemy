# Day 22 - Build Pong: The Famous Arcade Game
## Pong

![](pong.gif)

## Exercises
### Setup the Main Screen
- Set up a screen with a height of 600px and width of 800px.
- The screen background should be black.
- Make the screen window stay open until it is clicked.


### Write a Paddle Class and Paddle Objects that Respond to Key Presses
- Create a paddle that is 20px in width and 100px in height.
- The position coordinates will be (350, 0) for the first paddle and (-350, 0) for the second paddle (x_pos, y_pos).
- The paddles should move up and down by 20px
- The right paddle should move when pressing the “up” and “down” keys.
- The left paddle should move when pressing the "w" and "s" keys.


### Write a Ball Class and Make it Move
- Create a ball class with the width of 20px and height of 20px.
- Its starting position will be (0, 0).
- Move the ball to the top right edge of the screen for practice.


### Add the Ball Bouncing Logic
- Detect ball collision with the wall on either the top of the screen or the bottom of the screen.
- Create a method that makes the ball move in the oppoite direction of the y-axis when collision with a wall has happened.


### How to Detect Collisions with a Paddle
- Create a method using specific conditions so that when they are met, collision with a paddle has happened.
- Create a separate bounce method on the x-axis that will make the ball change directions once it hits a paddle.


### How to Detect when the Ball goes Out of Bounds
- Create a method that resets the ball once it has gone past the screen's set threshold.
- Once the ball resturns to its starting positon at (0, 0), it must move towards the opposite direction of where it was missed.


### Score Keeping and Changing Ball Speed
- Keep track of the score of each player by creating a scoreboard class.
- Write a method so that when the player misses the ball, a point will be awarded to their opponent.
- Write a method where the ball increases in speed every time it is hit by a paddle
