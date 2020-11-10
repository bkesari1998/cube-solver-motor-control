import RPi.GPIO as GPIO

class Switch:
    '''
    Class to model a SPDT switch with the NO terminal connected to a Raspberry Pi computer.
    '''

    def __init__(self, NO):
        '''
        Initializes an instance of Switch and sets up the GPIO pin connected to the NO terminal.
        Parameters: NO is the BCM number of the GPIO pin connected to the NO terminal of the switch.
        Returns: None.
        '''

        self.NO = NO

        # Set up NO as an input
        GPIO.setup(NO, GPIO.IN)
        
    def read_input(self):
        '''
        Reads the input value of the NO terminal of the switch.
        Parameters: None.
        Returns: Returns 1 if the switch is closed and 0 if the switch is open.
        '''

        return GPIO.input(self.NO)

    
