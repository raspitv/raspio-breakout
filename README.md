#raspio-breakout

https://github.com/raspitv/raspi-breakout


RasPiO® Breakout Python scripts

By Alex Eames http://RasPi.TV

These scripts go with the RasPiO® Breakout board
http://rasp.io/breakout

![RasPiO® Breakout board](http://rasp.io/wp-content/uploads/2013/12/RasPiO-Breakout-on-Raspberry-Pi-700.jpg "RasPiO® Breakout")


##Preparation

Connect a wire from each port to an led (long leg, +ve side).
Connect the short leg of the LED to a resistor (~330 Ohms is safe)
Connect the other end of the resistor to GND.

With the RasPiO® Breakout Pro, you don't need a resistor for your LED as there is already one on the underside of the board.

Do this for each port with a GPIO number (17 altogether). Then you are ready to test the ports.
You should have 17 leds connected to GPIO ports and resistors.


##Contents

Run each script by typing 
`sudo python scriptname.py`

With these scripts you should be able to...


* port-test.py       - up and down pattern, increasing speed
* port-test-pwm1.py  - brighten and dim the leds in succession
* port-test-pwm2.py  - brighten and dim alternate sides
* port-test-pwm3.py  - brighten and dim alternate groups of leds

##Enjoy

Have fun connecting things to your Raspberry Pi


