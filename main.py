#!/usr/bin/env python3

import shutil
import time
import webbrowser

import keyboard

BG_BLACK = '\033[40m';
FG_ORANGE = '\033[33m'
BOLD_TEXT = '\033[1m'
END_COLOR = '\033[0m'
ASCII_IMAGE_PATH = './ascii'

DELAY = 1000 / 11

def main():
    next_event = fetch_events()

    while True:
        clear_screen()
        display_logo()
        display_next_event(next_event)
        handle_keyboard_input()
        time.sleep(DELAY / 1000)

def handle_keyboard_input():
    if keyboard.is_pressed('q'):
        clear_screen()
        exit(0)

def fetch_events():
    # TODO: Buscar de algum outro modo
    return {
        'name': 'Esquenta DevOps Days Rio',
        'address': 'LeWagon - Ipanema',
        'date': '22 de Agosto às 19:00hrs'
    }

def display_next_event(event):
    terminal_columns = shutil.get_terminal_size().columns

    print('\n')
    print(f"TECH IN RIO\t techinrio.com\n".center(terminal_columns))
    print(f"Pŕoximo evento:\t{event['name']}".center(terminal_columns-2))
    print(f"{event['date']}".center(terminal_columns), end="")
    print(f"@ {event['address']}".center(terminal_columns), end="\n\n")

    print("aperte q para sair".center(terminal_columns))

def clear_screen():
    print('\033c', end='')

def display_logo():
    terminal_columns = shutil.get_terminal_size().columns
    terminal_rows = shutil.get_terminal_size().lines

    with open(ASCII_IMAGE_PATH) as file:
        content = file.readlines()

        vertical_padding = (terminal_rows - len(content)) // 2

        print("\n\n")

        step = 0
        for line in content:
            padding = (terminal_columns - len(line)) // 2

            # Pre art
            print(' ' * (padding), end='')

            # During art
            for char in line.strip()+'\n':
                print(f'\033[33m{char}{END_COLOR}', end='')
                step+=1

            # Post art
            step += 1

if __name__ == '__main__':
    main()
