#!/usr/bin/env pybricks-micropython
import types
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import player


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Initialize EV3 Brick.
ev3 = EV3Brick()
ev3.speaker.set_volume(100, which='_all_')
# ev3.speaker.set_speech_options(language='en', voice='f1', speed=None, pitch=99)
# print("Battery(mV):", ev3.battery.voltage())
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
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
crane_motor1 = Motor(Port.A)
crane_motor2 = Motor(Port.D)

# Initialize drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=184)

# Initialize sensors.
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S4)

# Initialize global variables.
MAX_TURNS = 13
SLOTS = 6
enemies = [None] * SLOTS
r = player.Robot()


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
    # Checking each slot.
    for current_slot in range(SLOTS):
        while color_sensor.color() == Color.WHITE:
            robot.drive(speed=-100, turn_rate=0)
        robot.stop(stop_type=Stop.HOLD)
        ev3.speaker.play_file(SoundFile.BACKING_ALERT)
        robot.straight(70)
        robot.turn(90)
        while color_sensor.color() == Color.WHITE:
            robot.drive(speed=-100, turn_rate=0)
        robot.stop(stop_type=Stop.HOLD)

        # If found, assigns an enemy to a slot, according to his color.
        enemy_found = None
        if color_sensor.color() == Color.GREEN:
            enemy_found = player.Tank()
        elif color_sensor.color() == Color.RED:
            enemy_found = player.Artillery()
        elif color_sensor.color() == Color.BROWN:
            enemy_found = player.Infantry()
        if enemy_found != None:
            enemies.insert(current_slot, enemy_found)

        # Next slot.
        if current_slot != SLOTS-1:
            ev3.speaker.play_file(SoundFile.BACKING_ALERT)
            robot.straight(70)
            robot.turn(-90)
            robot.straight(-280)

# EV3 picks a target.
""" NEEDS TO BE IMPROVED """
def pick_target():
    for idx in len(enemies)-1:
        if enemies[idx] != None:
            if idx != len(enemies)-1:
                ev3.speaker.play_file(SoundFile.BACKING_ALERT)
                robot.straight(70)
                robot.turn(90)
                robot.straight(-1400 + idx * 280)
                robot.turn(-90)
                robot.straight(-70)
            return idx
    return None

# Executes crane attack.
def crane_attack():
    while ultrasonic_sensor.distance() >= 200:
        robot.drive(speed=-100, turn_rate=0)
    robot.stop(stop_type=Stop.HOLD)
    crane_motor1.run_time(1000, 5000, then=Stop.HOLD, wait=True)
    crane_motor2.run_time(700, 5000, then=Stop.HOLD, wait=True)
    crane_motor1.run_time(1000, 5000, then=Stop.HOLD, wait=True)
    ev3.speaker.play_file(SoundFile.BACKING_ALERT)
    while color_sensor.color() == Color.WHITE or color_sensor.color() == Color.BLACK:
        robot.drive(speed=100, turn_rate=0)
    if color_sensor.color()==Color.GREEN or color_sensor.color()==Color.RED or color_sensor.color()==Color.BROWN:
        robot.straight(70)

# Executes touch attack.
def touch_attack():
    while touch_sensor.pressed() == False:
        robot.drive(speed=-100, turn_rate=0)
    robot.stop(stop_type=Stop.HOLD)
    ev3.speaker.play_file(SoundFile.BACKING_ALERT)
    while color_sensor.color() == Color.WHITE or color_sensor.color() == Color.BLACK:
        robot.drive(speed=100, turn_rate=0)
    if color_sensor.color()==Color.GREEN or color_sensor.color()==Color.RED or color_sensor.color()==Color.BROWN:
        robot.straight(70)

# Executes sound attack.
def sound_attack():
        ev3.speaker.play_file('SUIII.wav')

# EV3 decides the attack to be executed.
def attack_type():
    """ TODO """
    pass

# EV3 attacks a target.
def attack(type):
    if type == 1:
        crane_attack()
    elif type == 2:
        touch_attack()
    elif type == 3:
        sound_attack()
    else:
        print("Unknown attack.")

# EV3 repositions itself when its turn ends.
def reposition(idx):
    ev3.speaker.play_file(SoundFile.BACKING_ALERT)
    robot.straight(70)
    robot.turn(-90)
    robot.straight(-280 * idx)


# Main
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
        """ !!!!!!!!!! TODO !!!!!!!!!! """
        no_action()
    else:                                   # Robot's turn.
        if not predicted_winner():
            ev3.screen.load_image(ImageFile.HURT)
            ev3.speaker.play_file(SoundFile.UH_OH)
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
        # Chooses a target, type of attack, then attacks and repositions itself.
        find_target()
        target_idx = pick_target()
        if target_idx != None:
            # TODO attack_kind = attack_type()
            attack_kind = 3
            r.attack(attack_kind, enemies[target_idx])
            attack(attack_kind)
            reposition(target_idx)
        else:
            no_action()
            reposition(SLOTS-1)
    speaker.beep()                          # Turn ends.
ev3.light.off()



""" """ """ """ """ """ """ Sounds & Images """ """ """ """ """ """ """

# ev3.screen.load_image(ImageFile.THUMBS_UP)      # Winner case.
# ev3.speaker.play_file(SoundFile.FANFARE)
# ev3.speaker.play_file(SoundFile.CHEERING)

# ev3.screen.load_image(ImageFile.BLACK_EYE)      # EV3 was attacked.
# ev3.speaker.play_file(SoundFile.OUCH)

# ev3.speaker.play_file(SoundFile.LASER)          # Touch attack.
# ev3.speaker.play_file(SoundFile.KUNG_FU)        # Crane attack.
# ev3.speaker.play_file(SoundFile.SNEEZING)
# ev3.speaker.play_file(SoundFile.HORN_2)