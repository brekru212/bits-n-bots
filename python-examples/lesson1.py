"""My first attempt at converting the lessons Brett wrote into python.  Also a good way to get familiar with the ev3 python package"""

from ev3dev.ed3dev import LEDSide, LED

if __name__ == '__main__':
    #makes the left/right LEDs blink orange
    left_led = LEDSide("left")
    right_led = LEDSide("right")
    right_led.blink(LED.Color.ORANGE)
    left_led.blink(LED.Color.ORANGE)

