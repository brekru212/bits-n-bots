### The Mission

Imagine the duties of a dump truck.  They often follow the same path, while also picking up and dropping things off at constant intervals.  This time, we'll be working on getting the bot to follow a predictable path.  Once that is working, your job is to use the claw on the front of your bots to pick up and drop off the cargo.  This way, we'll have a functioning dump/delivery truck.

### Tasks

Your job is to automate the task of picking up and dropping off objects in the designated 'pick up' and 'drop off' zones.  The route for your dump truck makes a square shape.  At each corner of the square, the bot needs to drop off its current object while also picking up the one that is in the 'pick up' zone. 

*1)* Make the robot move in a square using the movement and steering control blocks.  (It will take some trial and error to get a perfect 90 degree turn)
*2)* Once that is working, think about how you can add the 'pick up' and 'drop off' features using the claw.
*3)* Now, what if your boss tells you that you need to travel this route more than once? Well, this is where the 'loop block' comes in handy.  It lets you execute a set of blocks over and over again.

Experiment with the loop block, see if you can make the bot travel in the square shape several times without failure.  Or, try making the loop stop after a certain amount of time.  Or, if you're feeling crazy, make it go on forever!

*4)*  Can you make the bots travel in a shape other than a square? A triangle? Pentagon? Hexagon?  Try coming up with a new delivery route shape for the dump truck.  Or, even harder, in the shape of an infinity symbol?

### Challenges

*5)* What if someone forgot to place an object in the pick up zone?  Well, you can use the infrared sensor from last week to detect whether there is an object that needs to be picked up.  (Look into using the case block)

*6)*  What if there is an obstacle that prevents you from moving in your path?  Can you make the bot stop so that it does not collide with the object.  Or, even better, make it so that the bot goes around an obstacle?


### ORIGINAL CHALLENGES
If the groups finish early, have them try different stopping conditions. Instead of stopping after turning four times, try:
- stopping after 20 seconds of moving in squares
- stopping after 20 seconds, but making sure that the robot always completes a full square (hint: you can put loops inside of other loops)
- doing a loop in one direction and then a loop in another direction.
- Try out the other stopping mechanisms in the loop block- get creative!
- stopping if the infrared sensor sees something within 25 units (unclear what the units are in the block)
- try to get the robot to do the infinity sign over and over
