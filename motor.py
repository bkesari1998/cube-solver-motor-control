import RPi.GPIO as GPIO
from time import sleep
from switch import Switch


class Motor:
    '''
    Class to model a stepper motor driven by an A4988 motor driver and controlled by a Raspberry Pi computer.
    '''

    def __init__(self, enable, step, direction):
        '''
        Initializes an instance of Motor and sets up the GPIO pins used to control the motor.
        Parameters: enable, step, and direction are the BCM numbers of the GPIO pins connected to the motor driver.
        Returns: None.
        '''

        self.enable = enable
        self.step = step
        self.direction = direction

        # Set up step and direction pins as outputs
        GPIO.setup(step, GPIO.OUT)
        GPIO.setup(direction, GPIO.OUT)

        # If enable pin is connected, set up enable pin as output
        if (enable >= 0):
            GPIO.setup(enable, GPIO.OUT)

    def direction_CW(self):
        '''
        Sets the direction of the motor to clockwise by setting the direction pin to high.
        Parameters: None.
        Returns: None.
        '''

        # Set direction pin to high
        GPIO.output(self.direction, GPIO.HIGH)

    def direction_CCW(self):
        '''
        Sets the direction of the motor to counterclockwise by setting the direction pin to low.
        Parameters: None.
        Returns: None.
        '''

        # Set direction pin to low
        GPIO.output(self.direction, GPIO.LOW)

    def enable(self):
        '''
        Enables the motor by setting the enable pin to low if enable pin is connected.
        Parameters: None.
        Returns: None.
        '''

        # Set enable pin to low if enable pin is connected
        if (self.enable >= 0):
            GPIO.output(self.enable, GPIO.LOW)

    def disable(self):
        '''
        Disables the motor by setting the enable pin to high if enable pin is connected.
        Parameters: None.
        Returns: None.
        '''

        # Set enable pin to high if enable pin is connected
        if (self.enable >= 0):
            GPIO.output(self.enable, GPIO.HIGH)

    def drive_steps(self, steps, delay):
        '''
        Drives the motor a set amount of steps with a set time delay between each step.
        Parameters: steps is the number of steps the motor will be driven and delay is the time delay between each step.
        Returns: None.
        '''

        # Execute for each step
        for i in range(0, steps):
            GPIO.output(self.step, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.step, GPIO.LOW)
            sleep(delay)

    def drive_steps(self, steps, delay):
        '''
        Drives the motor a set amount of steps with a set time delay between each step.
        Parameters: steps is the number of steps the motor will be driven and delay is the time delay between each step.
        Returns: None.
        '''

        # Execute for each step
        for i in range(0, steps):
            GPIO.output(self.step, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.step, GPIO.LOW)
            sleep(delay)

    def drive_switch(self, switch, delay):
        '''
        Drives the motor unitl a switch is triggered with a set time delay between each step.
        Parameters: switch is a Switch object and delay is the time delay between each step.
        Returns: None.
        '''

        # Execute until switch is triggered
        while (switch.read_input() == 0):
            GPIO.output(self.step, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.step, GPIO.LOW)
            sleep(delay)
