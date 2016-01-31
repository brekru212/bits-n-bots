## Working with sensors:

The goal for this project is to get used to using the various sensors that come with ev3 to control the actions of the bot.  We currently have an infrared sensor, which can be used for measuring the robot's proximity to an object.

### Task:  

Use the infrared sensor to display the robot's proximity to it's ojbect on the screen.  (You'll need to add a wait block at the end to make sure that the program doesn't end right after it displays the value, otherwise you won't see anything before it disappears!)

Make the robot respond to its surroundings.  If something gets too close to it, the display screen should display "Too Close!", or emit a sound of your choice.  

Do you notice anything weird about how your program behaves? Try to figure it out.

### Challenges
**0)** To make it so that the robot keeps checking the proximity sensor over and over again, we use a 'while loop'. This way, it will continuously execute your blocks over and over again.

**1)** Once you have that working, trying adding movement.  Make the bot move around and explore its surroundings in a pattern of your choice. (Circle, square, zig zag).  

**2)** At the end of the motion, check to see whether or not the bot is too close to its surroundings. 

Optionally, you can do so by making the robot spin in a circle (this is more challenging!!) and checking the sensor throughout the rotation, or by making the bot just check in the direction that the bot is facing.

**The Last Challenge** What if the robot isn't that far away from an object, but it also isn't that close to one?  Well, you can change the robot's movement speed depending on its proximity to something  (Use the wire you used earlier!).  (Hint, use a case block and read the help information).




