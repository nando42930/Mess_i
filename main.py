#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize global variables.
MAX_TURNS = 13

# Initialize EV3 Brick.
ev3 = EV3Brick()
ev3.speaker.set_volume(100, which='_all_')
# ev3.speaker.set_speech_options(language='en', voice='f1', speed=None, pitch=99)
# print("Battery(mV): ", ev3.battery.voltage())
if ev3.battery.voltage() < 2250:
    ev3.speaker.say("Battery below 25%. Please, recharge.")
ev3.light.on(Color.WHITE)
ev3.screen.load_image(ImageFile.ANGRY)
ev3.speaker.play_file(SoundFile.GO)
""" big_font = Font(size=24, bold=True)
ev3.screen.set_font(big_font)
str = "Hello!"
ev3.screen.draw_text((178-len(str))/2, 63, str) """

# Initialize motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
medium_motor = Motor(Port.D)

# Initialize drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=184)

# Initialize sensors.
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)

# Main
if not predicted_winner():
    ev3.screen.load_image(ImageFile.HURT)
    ev3.speaker.play_file(SoundFile.UH-OH)
    ev3.speaker.play_file(SoundFile.SORRY)
    ev3.speaker.play_file(SoundFile.CRYING)
    resume()
    reset()
    time = 0
    while time < 5000:
        ev3.screen.load_image(ImageFile.HURT)
        wait(500)
        ev3.screen.load_image(ImageFile.TEAR)
        wait(500)
        time = time()
else:
    ev3.speaker.play_file(SoundFile.FANTASTIC)
    for x in range(MAX_TURNS):
        ev3.speaker.play_file(SoundFile.THREE)
        wait(1000)
        ev3.speaker.play_file(SoundFile.TWO)
        wait(1000)
        ev3.speaker.play_file(SoundFile.ONE)
        wait(1000)
        ev3.speaker.play_file(SoundFile.ZERO)
        speaker.beep()                          # Turn begins.
        if(x % 2 == 0):                         # Enemy's turn.
            """ TODO """
            no_action()
        else:                                   # Robot's turn.
            targets_found = find_target()
            if targets_found == None:
                no_action()
            else:
                target = choose_target(targets_found)
                attack(target)
        speaker.beep()                          # Turn ends.
ev3.light.off()

# Return True when EV3 is the predicted winner. Otherwise, return False.
def predicted_winner():
    """ TODO """
    return True

# Turn without attacks.
def no_action():
    ev3.screen.load_image(ImageFile.ZZZ)
    ev3.speaker.play_file(SoundFile.INSECT_CHIRP)

# EV3 looks for targets in the field.
def find_target():
    ev3.screen.load_image(ImageFile.TARGET)
    ev3.speaker.play_file(SoundFile.SONAR)
    """ TODO """
    return None

# EV3 chooses a target.
def choose_target(targets):
    """ TODO """
    pass

# EV3 attacks a target.
def attack(target):
    """ TODO """
    pass


ev3.speaker.play_file(SoundFile.BACKING_ALERT)  # Robot moving backward.

ev3.screen.load_image(ImageFile.THUMBS_UP)      # Winner case.
ev3.speaker.play_file(SoundFile.FANFARE)
ev3.speaker.play_file(SoundFile.CHEERING)

ev3.screen.load_image(ImageFile.BLACK_EYE)      # EV3 was attacked.
ev3.speaker.play_file(SoundFile.OUCH)

ev3.speaker.play_file(SoundFile.LASER)          # Touch attack.
ev3.speaker.play_file('SUIII.wav')              # Sound attack.
ev3.speaker.play_file(SoundFile.KUNG_FU)        # Crane attack.
ev3.speaker.play_file(SoundFile.SNEEZING)
ev3.speaker.play_file(SoundFile.HORN_2)