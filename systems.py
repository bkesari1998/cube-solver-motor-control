import RPi.GPIO as GPIO
from time import sleep
from motor import Motor
from switch import Switch
import constants


class Rotors:
    '''
    Class to model the rotor motors system of the cube solving robot.
    '''

    def __init__(self, rotor_r, rotor_l):
        '''
        Initializes an instance of Rotors.
        Parameters: rotor_r and rotor_l are Motor objects. inner_r, outer_r, inner_r, outer_r are Switch objects.
        Returns: None.
        '''

        self.rotor_r = rotor_r
        self.rotor_l = rotor_l

    def rotate_forward(self):
        '''
        Rotates both motors forward 50 steps.
        Parameters: None.
        Returns None.
        '''

        # Set direction of both motors
        self.rotor_r.direction_CW()
        self.rotor_l.direction_CCW()

        # Execute 50 iterations of loop
        for i in range(0, constants.STEPS):
            GPIO.output(self.rotor_r.step, GPIO.HIGH)
            GPIO.output(self.rotor_l.step, GPIO.HIGH)
            sleep(constants.DELAY)
            GPIO.output(self.rotor_r.step, GPIO.LOW)
            GPIO.output(self.rotor_l.step, GPIO.LOW)
            sleep(constants.DELAY)

    def rotate_backward(self):
        '''
        Rotates both motors backward 50 steps.
        Parameters: None.
        Returns None.
        '''

        # Set direction of both motors
        self.rotor_r.direction_CCW()
        self.rotor_l.direction_CW()

        # Execute 50 iterations of loop
        for i in range(0, constants.STEPS):
            GPIO.output(self.rotor_r.step, GPIO.HIGH)
            GPIO.output(self.rotor_l.step, GPIO.HIGH)
            sleep(constants.DELAY)
            GPIO.output(self.rotor_r.step, GPIO.LOW)
            GPIO.output(self.rotor_l.step, GPIO.LOW)
            sleep(0.002)

    def rotate_r_cw(self):
        '''
        Rotates the right rotor motor 50 steps in the clockwise direction.
        Parameters: None.
        Returns: None.
        '''

        # Set direction and drive
        self.rotor_r.direction_CW()
        self.rotor_r.drive_steps(constants.STEPS, constants.DELAY)
    
    def rotate_r_ccw(self):
        '''
        Rotates the right rotor motor 50 steps in the counterclockwise direction.
        Parameters: None.
        Returns: None.
        '''

        # Set direction and drive
        self.rotor_r.direction_CCW()
        self.rotor_r.drive_steps(constants.STEPS), constants.DELAY)

    def rotate_l_cw(self):
        '''
        Rotates the left rotor motor 50 steps in the clockwise direction.
        Parameters: None.
        Returns: None.
        '''

        # Set direction and drive
        self.rotor_l.direction_CW()
        self.rotor_l.drive_steps(constants.STEPS, constants.DELAY)
    
    def rotate_l_ccw(self):
        '''
        Rotates the left rotor motor 50 steps in the counterclockwise direction.
        Parameters: None.
        Returns: None.
        '''

        # Set direction and drive
        self.rotor_l.direction_CCW()
        self.rotor_l.drive_steps(constants.STEPS, constants.DELAY)

class Belts:
    '''
    Class to model the belt system of the cube solving robot
    '''

    def __init__(self, belt_r, belt_l, inner_r, outer_r, inner_l, outer_l):
        '''
        Initializes an instance of Belts.
        Parameters: belt_r and belt_l are Motor objects. inner_r, outer_r, inner_l, and outer_l are Switch objects.
        Returns: None.
        '''

        self.belt_r = belt_r
        self.belt_l = belt_l
        self.inner_r = inner_r
        self.outer_r = outer_r
        self.inner_l = inner_l
        self.outer_l = outer_l
        self.state = None

    def drive_in(self):
        '''
        Drives both belt motors until both inner switches are triggered.
        Parameters: None.
        Returns: None.
        '''

        # Set direction of both motors
        self.belt_r.direction_CCW()
        self.belt_l.direction_CW()

        # Execute until at least 1 switch is triggerd
        while ((self.inner_r.read_input() == 0)  or (self.inner_l.read_input() == 0)):
            GPIO.output(self.belt_r.step, GPIO.HIGH)
            GPIO.output(self.belt_l.step, GPIO.HIGH)
            sleep(constants.DELAY)
            GPIO.output(self.belt_r.step, GPIO.LOW)
            GPIO.output(self.belt_l.step, GPIO.LOW)
            sleep(constants.DELAY)

        # Execute if right inner switch is not triggered
        if (self.inner_r.read_input() == 0):
            self.belt_r.drive_switch(self.inner_r, constants.DELAY)
        
        # Execute if left inner switch is not triggered
        elif (self.inner_l.read_input() == 0):
            self.belt_l.drive_switch(self.inner_l, constants.DELAY)

        # Set state
        self.state = 'in'

    def drive_out(self):
        '''
        Drives both belt motors until both outer switches are triggered.
        Parameters: None.
        Returns: None.
        '''

        # Set direction of both motors
        self.belt_r.direction_CW()
        self.belt_l.direction_CCW()

        # Execute until at least 1 switch is triggerd
        while ((self.outer_r.read_input() == 0)  or (self.outer_l.read_input() == 0)):
            GPIO.output(self.belt_r.step, GPIO.HIGH)
            GPIO.output(self.belt_l.step, GPIO.HIGH)
            sleep(constants.DELAY)
            GPIO.output(self.belt_r.step, GPIO.LOW)
            GPIO.output(self.belt_l.step, GPIO.LOW)
            sleep(constants.DELAY)

        # Execute if right outer switch is not triggered
        if (self.outer_r.read_input() == 0):
            self.belt_r.drive_switch(self.inner_r, constants.DELAY)
        
        # Execute if left outer switch is not triggered
        elif (self.outer_l.read_input() == 0):
            self.belt_l.drive_switch(self.inner_l, constants.DELAY)

        # Set state
        self.state = 'out'

class Table:
    '''
    Class to model the table system of the cube solving robot.
    '''

    def __init__(self, table):
        '''
        Initializes an instance of table.
        Parameters: table is a Motor object.
        Returns: None.
        '''

        self.table = table

    def rotate_cw(self):
        '''
        Rotates the table 50 steps in the clockwise direction.
        Parameters: None.
        Returns: None.
        '''

        # Set direction to clockwise
        self.table.direction_CW()

        # Drive motor
        self.table.drive_steps(constants.STEPS, constants.DELAY)

    def rotate_ccw(self):
        '''
        Rotates the table 50 steps in the counterclockwise direction.
        Parameters: None.
        Returns: None.
        '''

        # Set direction to clockwise
        self.table.direction_CCW()

        # Drive motor
        self.table.drive_steps(constants.STEPS, constants.DELAY)

class Screw:
    '''
    Class to model the lead screw system of the cube solving robot.
    '''

    def __init__(self, screw, upper, lower):
        '''
        Initializes an instance of Screw.
        Parameters: screw is a Motor object. upper and lower are Switch objects.
        Returns: None.
        '''

        self.screw = screw
        self.upper = upper
        self.lower = lower
        self.state = None
    
    def drive_up(self):
        '''
        Rotates lead screw until upper switch is triggered.
        Parameters: None.
        Returns: None.
        '''

        # Set direction of motor
        self.screw.direction_CW()

        # Drive motor until upper switch is triggered
        self.screw.drive_switch(self.upper, constants.DELAY)

        # Set state
        self.state = 'up'

    def drive_down(self):
        '''
        Rotates lead screw until lower switch is triggered.
        Parameters: None.
        Returns: None.
        '''

        # Set direction of motor
        self.screw.direction_CCW()

        # Drive motor until lower switch is triggered
        self.screw.drive_switch(self.lower, constants.DELAY)

        self.state = 'down'
    
    def drive_intermediate_1(self):
        '''
        Rotates lead screw 200 steps down from the upper position.
        Parameters: None.
        Returns: None.
        '''

        # Rotate lead screw to the upper position
        self.up()

        # Set direction of motor
        self.screw.direction_CCW()

        # Drive motor 200 steps
        self.screw.drive_steps(4 * constants.STEPS, constants.DELAY)

        # Set state
        self.state = 'intermediate_1'

    def drive_intermediate_2(self):
        '''
        Rotates lead screw 400 steps down from the upper position.
        Parameters: None.
        Returns: None.
        '''

        # Rotate lead screw to the upper position
        self.up()

        # Set direction of motor
        self.screw.direction_CCW()

        # Drive motor 400 steps
        self.screw.drive_steps(8 * constants.STEPS, constants.DELAY)

        # Set state
        self.state = 'intermediate_2'

    def drive_intermediate_3(self):
        '''
        Rotates lead screw 600 steps down from the upper position.
        Parameters: None.
        Returns: None.
        '''

        # Rotate lead screw to the upper position
        self.up()

        # Set direction of motor
        self.screw.direction_CCW()

        # Drive motor 600 steps
        self.screw.drive_steps(12 * constants.STEPS, constants.DELAY)

        # Set state
        self.state = 'intermediate_3'