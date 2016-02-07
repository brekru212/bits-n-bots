The mission
===
Now we want to let the dump truck 'think for itself' a little bit. The goal is to get the robot to get through a simple maze without running into anything. To do this, we'll use 'case structures', which let the robot make a decision and act on it.
Case structures are very common in programming, they are what allow the robots to think for themselves.

Task
---
You need to come up with a case structure that will let the robot navigate the maze

 - If the robot is too close to a wall: turn and keep moving
 - Otherwise, keep moving forward

1. Start by coming up with some code that will make the robot move forward, unless it is too close to a wall; if it is too close, your code should do nothing. You'll need to use the infrared sensor to measure the distance and a comparison to decide if it is too close. Try using the "display distance" block we've given you to get a feel for how the infrared sensor works. 

1. Now make the robot move forward until it gets too close to a wall. When it does, just make it stop. To do this, you'll use what you did in the previous step; just make that happen repeatedly by putting it in a loop. Set the condition on the loop to 'forever' (the infinity sign) so that your robot will do this until it hits the 'stop' block in your case structure.

1. Once you've got the above working, you're almost there! Now change your code above so that the robot turns when it gets too close instead of stopping. A good idea to start is to make the robot just turn left by 90 degrees every time it would run ito a wall. 

Challenges
---

Whew! Just getting your robot through the maze is a great task; however if you're craving more:

1. We want to get the robot through the maze even faster; Can you make the robot move faster if there's no wall nearby? 

1. Can you be smarter about how the robot nagivates? For instance; instead of simply turning left at any obstruction, can you make the robot turn left and then periodically check to see if it can turn right again and keep moving forwrad? You would need to make the robot stop after moving so far and turn to the right; check the distance; and move forward again like normal if there's no wall, but turn left again and keep trying if not. 

Good luck!
