#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import player
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Initialize motors, drive base and sensors.
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
crane_motor1 = Motor(Port.A)
crane_motor2 = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=176)
color_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S4)


# Initialize global variables.
ev3 = EV3Brick()
watch = StopWatch()
ev3_log = DataLog()
r = player.Robot()
MAX_TURNS = 13
SLOTS = 6
enemies = [None] * SLOTS



# EV3 moves forward for a specific distance(mm).
def forward(distance):
    robot.straight(-distance)

# EV3 moves backward for a specific distance(mm).
def backward(distance):
    robot.straight(distance)

# EV3 turns left for a specific angle in degrees.
def turn_left(angle):
    robot.turn(angle)

# EV3 turns right for a specific angle in degrees.
def turn_right(angle):
    robot.turn(-angle)

# Return True when EV3 is the predicted winner. Otherwise, return False.
def predicted_winner():
    """ TODO """
    return True

# Turn without attacks.
def no_action():
    # ev3.screen.load_image(ImageFile.ZZZ)
    ev3.speaker.play_file(SoundFile.INSECT_CHIRP)

# EV3 looks for targets in the field.
""" TO BE TESTED """
def find_targets():
    ev3.screen.load_image(ImageFile.TARGET)
    ev3.speaker.play_file(SoundFile.SONAR)
    # Checking each slot.
    for current_slot in range(SLOTS):
        while color_sensor.color() == Color.WHITE:
            robot.drive(speed=-100, turn_rate=0)
        if enemies[current_slot] == None or current_slot == SLOTS-1:
            robot.stop()
            ev3.speaker.play_file(SoundFile.BACKING_ALERT)
            backward(70)
            turn_left(90)
            while color_sensor.color() == Color.WHITE:
                robot.drive(speed=-100, turn_rate=0)
            robot.stop()
            if enemies[current_slot] == None:
                # If found, assigns an enemy to a slot, according to his color.
                enemy_found = None
                if  color_sensor.color() == Color.GREEN:
                    ev3.speaker.say("GREEN GREEN GREEN")
                    enemy_found = player.Tank()
                elif color_sensor.color() == Color.RED:
                    ev3.speaker.say("RED RED RED")
                    enemy_found = player.Artillery()
                elif color_sensor.color() == Color.BROWN:
                    ev3.speaker.say("BROWN BROWN BROWN")
                    enemy_found = player.Infantry()
                if enemy_found != None:
                    enemies.insert(current_slot, enemy_found)

                # Next slot.
                if current_slot != SLOTS-1:
                    ev3.speaker.play_file(SoundFile.BACKING_ALERT)
                    backward(70)
                    turn_right(90)
                    forward(280)
        """ # Next slot right away.
        else:
            robot.stop()
            forward(70) """

# EV3 picks a target.
""" NEEDS TO BE IMPROVED """
def fight_targets():
    last_idx = SLOTS-1
    fought = False
    for idx in reversed(range(SLOTS)):
        if enemies[idx] != None:
            if idx != SLOTS-1:
                ev3.speaker.play_file(SoundFile.BACKING_ALERT)
                backward(70)
                turn_left(90)
                forward((last_idx-idx) * 280)
                turn_right(90)
                forward(70)
            attack_kind = attack_type()
            r.attack(attack_kind, enemies[idx])
            attack(attack_kind)
            last_idx = idx
            fought = True
        elif idx == 0 and not fought:
            no_action()
    return last_idx

# Executes crane attack.
def crane_attack():
    while ultrasonic_sensor.distance() >= 200:
        robot.drive(speed=-100, turn_rate=0)
    # robot.stop(stop_type=Stop.HOLD)
    robot.stop()
    crane_motor1.run_time(1000, 5000, then=Stop.HOLD, wait=True)
    crane_motor2.run_time(700, 5000, then=Stop.HOLD, wait=True)
    crane_motor1.run_time(1000, 5000, then=Stop.HOLD, wait=True)
    ev3.speaker.play_file(SoundFile.BACKING_ALERT)
    while color_sensor.color() == Color.WHITE or color_sensor.color() == Color.BLACK:
        robot.drive(speed=100, turn_rate=0)
    if color_sensor.color()==Color.GREEN or color_sensor.color()==Color.RED or color_sensor.color()==Color.BROWN:
        backward(70)

# Executes touch attack.
def touch_attack():
    while not touch_sensor.pressed():
        robot.drive(speed=-100, turn_rate=0)
    # robot.stop(stop_type=Stop.HOLD)
    robot.stop()
    ev3.speaker.play_file(SoundFile.BACKING_ALERT)
    while color_sensor.color() == Color.WHITE or color_sensor.color() == Color.BLACK:
        robot.drive(speed=100, turn_rate=0)
    if color_sensor.color()==Color.GREEN or color_sensor.color()==Color.RED or color_sensor.color()==Color.BROWN:
        backward(70)

# Executes sound attack.
def sound_attack():
        ev3.speaker.play_file('SUIII.wav')

# EV3 decides the attack to be executed.
""" NEEDS TO BE IMPROVED """
def attack_type():
    return random.randint(1, 3)

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
    backward(70)
    turn_right(90)
    """ IF STATEMENT TO BE TESTED """
    """ if idx == 0:
        backward(280) """
    backward(280 * idx)

def move(pos1, pos2):
    """ TODO """
    pass

def no_targets():
    for i in range(SLOTS):
        if enemies[i] != None:
            return False
    return True

def under_attack():
    last_idx = 0
    for idx in range(SLOTS):
        if enemies[idx] != None:
            forward((idx-last_idx) * 280)
            while color_sensor.color() == Color.WHITE:
                robot.drive(speed=-100, turn_rate=0)
            robot.stop()
            ev3.speaker.play_file(SoundFile.BACKING_ALERT)
            backward(70)
            turn_left(90)
            while color_sensor.color() == Color.WHITE:
                robot.drive(speed=-100, turn_rate=0)
            robot.stop()
            # ev3.screen.load_image(ImageFile.BLACK_EYE)
            ev3.speaker.play_file(SoundFile.OUCH)
            last_idx = idx
""" TODO """



# Initialize EV3 Brick.
def init():
    ev3.speaker.set_volume(100, which='_all_')
    # ev3.speaker.set_speech_options(language='en', voice='f1', speed=None, pitch=99)
    mV = ev3.battery.voltage()
    print("Battery(mV):", mV)
    if mV != None and mV < 2250:
        ev3.speaker.say("Battery below 25%. Please, recharge.")
    ev3.light.on(Color.WHITE)
    ev3.screen.load_image(ImageFile.ANGRY)
    ev3.speaker.play_file(SoundFile.GO)
    """ big_font = Font(size=24, bold=True)
    ev3.screen.set_font(big_font)
    str = "Hello!"
    ev3.screen.draw_text((178-len(str))/2, 63, str) """



# Game's lifetime.
def main():
    init()
    watch.resume()
    for x in range(MAX_TURNS):
        print("Turn number {} has started.".format(x+1))
        # ev3.speaker.play_file(SoundFile.THREE)
        # ev3.speaker.play_file(SoundFile.TWO)
        # ev3.speaker.play_file(SoundFile.ONE)
        # ev3.speaker.play_file(SoundFile.ZERO)
        # Turn begins.
        ev3.speaker.beep()
        # Enemy's turn.
        if(x % 2 == 0):
            if x == 0 or no_targets():
                no_action()
            else:
                idx = under_attack()
                reposition(idx)
        # Robot's turn.
        else:
            if not predicted_winner():
                ev3.screen.load_image(ImageFile.HURT)
                ev3.speaker.play_file(SoundFile.UH_OH)
                ev3.speaker.play_file(SoundFile.SORRY)
                ev3.speaker.play_file(SoundFile.CRYING)
                time = 0
                watch.reset()
                while time != None and time < 5000:
                    ev3.screen.load_image(ImageFile.HURT)
                    wait(500)
                    ev3.screen.load_image(ImageFile.TEAR)
                    wait(500)
                    time = watch.time()
            else:
                ev3.speaker.play_file(SoundFile.FANTASTIC)
            # Searches for targets and fights them, if possible.
            find_targets()
            idx = fight_targets()
            # Selects an attack, attacks and repositions itself.
            reposition(idx)
        ev3.speaker.beep()                      # Turn ends.
    ev3.light.off()

if __name__ == '__main__':
    main()



""" """ """ """ """ """ """ Sounds & Images """ """ """ """ """ """ """

# ev3.screen.load_image(ImageFile.THUMBS_UP)      # Winner case.
# ev3.speaker.play_file(SoundFile.FANFARE)
# ev3.speaker.play_file(SoundFile.CHEERING)

# ev3.speaker.play_file(SoundFile.LASER)          # Touch attack.
# ev3.speaker.play_file(SoundFile.KUNG_FU)        # Crane attack.
# ev3.speaker.play_file(SoundFile.SNEEZING)
# ev3.speaker.play_file(SoundFile.HORN_2)