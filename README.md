# cube-solver-motor-control
Python programs to control stepper motors for Rubik's cube solving robot

## Usage
### Python Version
This project uses Python 3.
### External Libraries
- RPi.GPIO
### Programs
constants.py: Contains constants used in other python files in the projects
<br/>
motor.py: Contains a class used to model and control a Nema 17 stepper motor driven by a A4988 stepper motor driver connected to a Raspberry Pi
<br/>
switch.py: Contains a class used to model a SPDT switch connected to a Raspberry Pi
<br/>
systems.py: Contains classes used to model and control the unique systems of the Rubik's cube solving robot.
<br/>
controls.py: Contains the functions used to control the entire robot to solve a Rubik's cube.
