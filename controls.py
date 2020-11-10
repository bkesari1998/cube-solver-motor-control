import RPi.GPIO as GPIO
import constants
import systems

class Robot:
    '''
    Class used to model the entire cube solving robot.
    '''

    def __init__(self, rotors, belts, table, screw):
        '''
        Initializes an instance of Robot.
        Parameters: rotors is a Rotors object. belts is a Belts object. table is a Table object. screw is a screw object.
        Returns: None.
        '''

        self.rotors = rotors
        self.belts = belts
        self.table = table
        self.screw = screw
        self.state = None
    
    def start_end_sequence():
        '''
        Executes the start/end sequence of the robot.
        Parameters: None.
        Returns: None.
        '''

        self.screw.up()
        self.belts.out()

    def instr_F(instr_sequence):
        '''
        Executes an F rotation of the cube.
        Parameters: instr_sequence is a list of characters containing the previous, current, and next instruction to solve the cube.
        Returns: None.
        '''

        # Previous instruction was F
        if (instr_sequence[0] == 'F'):
            self.table.rotate_cw()

        # Previous instruction was not F
        else:
            # Check belts state
            if (self.belts.state != 'in'):
                
                # Place screw in up position
                self.screw.drive_up()

                # Place belts in in position
                self.belts.drive_in()
            
            # Put screw in intermediate_3 position
            self.screw.drive_intermediate_3()

            # Rotate rotors forward
            self.rotors.rotate_forward()

            # Put screw in intermediate_1 position
            self.screw.drive_intermediate_1()

            # Rotate table
            self.table.rotate_cw()

        # Check if next instruction is not F 
        if (instr_sequence[2] != 'F'):
            
            # Put screw in intermediate_3 positon
            self.screw.drive_intermediate_3()

            # Rotate cube back to original position
            self.rotors.rotate_backward()

    def instr_f(instr_sequence):
        '''
        Executes an f rotation of the cube.
        Parameters: instr_sequence is a list of characters containing the previous, current, and next instruction to solve the cube.
        Returns: None.
        '''

        # Previous instruction was f
        if (instr_sequence[0] == 'f'):
            self.table.rotate_ccw()

        # Previous instruction was not f
        else:
            # Check belts state
            if (self.belts.state != 'in'):
                
                # Place screw in up position
                self.screw.drive_up()

                # Place belts in in position
                self.belts.drive_in()
            
            # Put screw in intermediate_3 position
            self.screw.drive_intermediate_3()

            # Rotate rotors forward
            self.rotors.rotate_forward()

            # Put screw in intermediate_1 position
            self.screw.drive_intermediate_1()

            # Rotate table
            self.table.rotate_ccw()

        # Check if next instruction is not F 
        if (instr_sequence[2] != 'f'):
            
            # Put screw in intermediate_3 positon
            self.screw.drive_intermediate_3()

            # Rotate cube back to original position
            self.rotors.rotate_backward()

    def instr_B(instr_sequence):
        '''
        Executes an B rotation of the cube.
        Parameters: instr_sequence is a list of characters containing the previous, current, and next instruction to solve the cube.
        Returns: None.
        '''

        # Previous instruction was B
        if (instr_sequence[0] == 'B'):
            self.table.rotate_cw()

        # Previous instruction was not B
        else:
            # Check belts state
            if (self.belts.state != 'in'):
                
                # Place screw in up position
                self.screw.drive_up()

                # Place belts in in position
                self.belts.drive_in()
            
            # Put screw in intermediate_3 position
            self.screw.drive_intermediate_3()

            # Rotate rotors backward
            self.rotors.rotate_backward()

            # Put screw in intermediate_1 position
            self.screw.drive_intermediate_1()

            # Rotate table
            self.table.rotate_cw()

        # Check if next instruction is not B 
        if (instr_sequence[2] != 'B'):
            
            # Put screw in intermediate_3 positon
            self.screw.drive_intermediate_3()

            # Rotate cube back to original position
            self.rotors.rotate_forward()

    def instr_b(instr_sequence):
        '''
        Executes an B rotation of the cube.
        Parameters: instr_sequence is a list of characters containing the previous, current, and next instruction to solve the cube.
        Returns: None.
        '''

        # Previous instruction was b
        if (instr_sequence[0] == 'b'):
            self.table.rotate_ccw()

        # Previous instruction was not b
        else:
            # Check belts state
            if (self.belts.state != 'in'):
                
                # Place screw in up position
                self.screw.drive_up()

                # Place belts in in position
                self.belts.drive_in()
            
            # Put screw in intermediate_3 position
            self.screw.drive_intermediate_3()

            # Rotate rotors backward
            self.rotors.rotate_backward()

            # Put screw in intermediate_1 position
            self.screw.drive_intermediate_1()

            # Rotate table
            self.table.rotate_ccw()

        # Check if next instruction is not b
        if (instr_sequence[2] != 'b'):
            
            # Put screw in intermediate_2 positon
            self.screw.drive_intermediate_2()

            # Rotate cube back to original position
            self.rotors.rotate_forward()

    def instr_U(instr_sequence):
        '''
        Executes an U rotation of the cube.
        Parameters: instr_sequence is a list of characters containing the previous, current, and next instruction to solve the cube.
        Returns: None.
        '''

        # Previous instruction was U
        if (instr_sequence[0] == 'U'):
            self.table.rotate_cw()

        # Previous instruction was not U
        else:
            # Check belts state
            if (self.belts.state != 'in'):
                
                # Place screw in up position
                self.screw.drive_up()

                # Place belts in in position
                self.belts.drive_in()
            
            # Put screw in intermediate_3 position
            self.screw.drive_intermediate_3()

            # Rotate rotors forward 2 times
            self.rotors.rotate_forward()
            self.rotors.rotate_forward()

            # Put screw in intermediate_1 position
            self.screw.drive_intermediate_1()

            # Rotate table
            self.table.rotate_cw()

        # Check if next instruction is not U 
        if (instr_sequence[2] != 'U'):
            
            # Put screw in intermediate_3 positon
            self.screw.drive_intermediate_3()

            # Rotate cube back to original position
            self.rotors.rotate_backward()
            self.rotors.rotate_backward()

    def instr_u(instr_sequence):
        '''
        Executes an u rotation of the cube.
        Parameters: instr_sequence is a list of characters containing the previous, current, and next instruction to solve the cube.
        Returns: None.
        '''

        # Previous instruction was u
        if (instr_sequence[0] == 'u'):
            self.table.rotate_ccw()

        # Previous instruction was not u
        else:
            # Check belts state
            if (self.belts.state != 'in'):
                
                # Place screw in up position
                self.screw.drive_up()

                # Place belts in in position
                self.belts.drive_in()
            
            # Put screw in intermediate_3 position
            self.screw.drive_intermediate_3()

            # Rotate rotors forward 2 times
            self.rotors.rotate_forward()
            self.rotors.rotate_forward()

            # Put screw in intermediate_1 position
            self.screw.drive_intermediate_1()

            # Rotate table
            self.table.rotate_ccw()

        # Check if next instruction is not u
        if (instr_sequence[2] != 'u'):
            
            # Put screw in intermediate_3 positon
            self.screw.drive_intermediate_3()

            # Rotate cube back to original position
            self.rotors.rotate_backward()
            self.rotors.rotate_backward()
    
    def instr_D(self):
        '''
        Executes a D rotation of the cube.
        Parameters: None.
        Returns: None.
        '''

        # Check if belts are in
        if (self.belts.state != 'in'):

            # Place screw in up position
            self.screw.drive_up()
            
            # Bring belts in
            self.belts.drive_in()

        # Place screw in intermediate_1 position
        self.screw.drive_intermediate_1()

        # Rotate table
        self.table.rotate_cw()

    def instr_d(self):
        '''
        Executes a d rotation of the cube.
        Parameters: None.
        Returns: None.
        '''

        # Check if belts are in
        if (self.belts.state != 'in'):

            # Place screw in up position
            self.screw.drive_up()
            
            # Bring belts in
            self.belts.drive_in()

        # Place screw in intermediate_1 position
        self.screw.drive_intermediate_1()

        # Rotate table
        self.table.rotate_ccw()
    
    def instr_R(self):
        '''
        Executes a R rotation of the cube.
        Parameters: None.
        Returns: None.
        '''

        # Check if belts are in
        if (self.belts.state != 'in'):

            # Place screw in up position
            self.screw.drive_up()
            
            # Bring belts in
            self.belts.drive_in()

        # Place screw in intermediate_1 position
        self.screw.drive_intermediate_2()

        # Rotate right rotor
        self.rotors.rotate_r_cw()
    
    def instr_r(self):
        '''
        Executes a r rotation of the cube.
        Parameters: None.
        Returns: None.
        '''

        # Check if belts are in
        if (self.belts.state != 'in'):

            # Place screw in up position
            self.screw.drive_up()
            
            # Bring belts in
            self.belts.drive_in()

        # Place screw in intermediate_1 position
        self.screw.drive_intermediate_2()

        # Rotate right rotor
        self.rotors.rotate_r_ccw()

   def instr_L(self):
        '''
        Executes a L rotation of the cube.
        Parameters: None.
        Returns: None.
        '''

        # Check if belts are in
        if (self.belts.state != 'in'):

            # Place screw in up position
            self.screw.drive_up()
            
            # Bring belts in
            self.belts.drive_in()

        # Place screw in intermediate_1 position
        self.screw.drive_intermediate_2()

        # Rotate left rotor
        self.rotors.rotate_l_cw()
    
    def instr_l(self):
        '''
        Executes a l rotation of the cube.
        Parameters: None.
        Returns: None.
        '''

        # Check if belts are in
        if (self.belts.state != 'in'):

            # Place screw in up position
            self.screw.drive_up()
            
            # Bring belts in
            self.belts.drive_in()

        # Place screw in intermediate_1 position
        self.screw.drive_intermediate_2()

        # Rotate right rotor
        self.rotors.rotate_l_ccw()
