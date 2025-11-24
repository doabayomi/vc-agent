#!/usr/bin/python3
def stop():
    pass

def move_foward(distance):
    pass

def turn_left(angle):
    pass

def turn_right(angle):
    pass

def ring_buzzer():
    pass

COMMAND_MAP = {
    'forward': move_foward,
    'left': turn_left,
    'right': turn_right,
    'stop': stop,
    'alarm': ring_buzzer
}

def execute_command_set(commands_set: str):
    """Execute a returned set of commands from a ChatGPT prompt"""
    commands = commands_set.splitlines()
    for command in commands:
        keyword, argument = command.split(' ')
        func = COMMAND_MAP.get(keyword) 
        # TODO: use JSON instead
        if func:
            func(int(argument))
        else:
            raise Exception(f"Command set consists of invalid command {keyword}")
