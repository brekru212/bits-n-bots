## Working with sensors:

The goal for this project is make our bots aware of their surroundings.  Otherwise, our bot will run into things and collide with objects in future lessons!.  

We will be using the 'infrared sensor' to measure proximity.  Does everyone know what the word 'infrared' means?  If not, be sure to ask!

## Task  

### Alpha
Use the infrared sensor to display the robot's proximity to nearby objects on the screen.  

Hint: You need to use the 'wired' setting for the display block.  Also, you need to drag a wire from the infrared sensor block to the display block

Do you notice anything weird about how your program behaves? You may have noticed that the value doesn't show up!  This is because the program executes too quickly for your eyes to read the value.  Try adding a 'wait block' at the end of your blocks.


### Beta
Now that you successfully displayed the proximity on the display, can you do this a second time?

Use the same block(s) from task Alpha to display the proximity on the screen two separate times.  In between each time you read the sensor, make the bot wait two or three seconds.  

Pick up the bot and point it at various objects, have some fun measuring the bot's proximity to different objects!

### Gamma

Now, let's add some motion in between reading the sensors.

How would you make the robot turn 90 degrees and then display the proximity sensor value on the screen?  Can you do this four times, each time turning ninety degrees?


In what order do you have to place the blocks?  (Remember, EV3 reads from left to right, just like us!)

Before continuining on to the challenges, call over a volunteer.  Show them what you just did and try to explain to them how everything works!


## Challenges
**0)** To make it so that the robot keeps checking the proximity sensor over and over again, we use a 'while loop'.  In EV3, this is called a loop block. This way, it will continuously execute your blocks over and over again.  Try doing this.

**1)** Once you have that working, trying adding movement.  Make the bot move around and explore its surroundings in a pattern of your choice. (Circle, square, zig zag).  

**2)** After moving, use the value from the proximity sensor to control how fast the robot moves.  This allows us to slow down once we get close to something and lets our bot do some decision making! (Use the wire concept you used earlier! Take the value from the sensor and drag it into the motor power value).  

Do you notice something wrong here? You may have to use a math block (red block) to perform the sensor value

**The Last Challenge**

Lets make our bot do some multitasking!

Try using two start blocks.  For the first start block, handle all of the motion of the bot.

For the second start block, control the proximity sensor.  If the value of the sensor is ever less than 10, make the program stop running.

This allows our bot to perform multiple tasks at once, instead of one after the other!




