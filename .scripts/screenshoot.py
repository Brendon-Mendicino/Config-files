#!/bin/python3

import os
from re import X
import time
from queue import Queue
from threading import Thread, Lock
from pynput.keyboard import Key, Listener


STARTING_DIR = '/home/brendon/uni/appunti'
SCREENSHOT_DIR = '/home/brendon/Pictures'
SEC_IN_A_MIN = 60

locations = {
    'ele': '/home/brendon/uni/appunti/elap/img',
    'con': '/home/brendon/uni/appunti/controlli/img',
    'rel': '/home/brendon/uni/tirocinio/relazione/img',
    'arch': '/home/brendon/uni/magistrale/architettura/appunti/img',
    'data2': '/home/brendon/uni/magistrale/data2/appunti/img',
    'reti2': '/home/brendon/uni/magistrale/reti2/appunti/img',
    'security': '/home/brendon/uni/magistrale/security/appunti/img',
}


images = sorted(os.listdir(SCREENSHOT_DIR))

image_queue = Queue()


def synchronized(func):
    func.__lock__ = Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func



@synchronized
def function_lock(func, *args, **kws):
    func(*args, **kws)


def print_location_list():
    print('Available locations:')

    hashtag_seiling = '#' * 60
    print(hashtag_seiling)
    for i, loc in enumerate(list(locations.keys()), start=1):
        print('#' + ' ' * (len(hashtag_seiling) - 2) + '#')

        location_with_number = f'{i:02}. {loc}'
        print(f'# {location_with_number}' + ' ' * (len(hashtag_seiling) - len(location_with_number) - 3) + '#')

    print('#' + ' ' * (len(hashtag_seiling) - 2) + '#')
    print(hashtag_seiling)
    print()


is_location_set = False
selected_location = ''

def ask_for_location_to_move():
    global is_location_set
    global selected_location

    if is_location_set:
        return

    while True:
        print_location_list()

        location = input(f'Select a location: ')
        if location not in locations.keys():
            print('Wrong location!')
            continue

        is_location_set = True
        selected_location = location

        return



def print_listening_str(timing, new):
    if new:
        print('\rlistening         ', end='')
    elif timing == 0:
        print('\rlistening         ', end='')
    elif timing == 1:
        print('\rlistening .       ', end='')
    elif timing == 2:
        print('\rlistening . .     ', end='')
    elif timing == 3:
        print('\rlistening . . .   ', end='')
    elif timing == 4:
        print('\rlistening . . . . ', end='')


def move_image(image):
    global selected_location

    while True:
        print(f'({image})')
        new_name = input('New name: ')

        while input(f"are you sure you want to move '{new_name}' -> '{selected_location}'? [y/n] ") != 'y':
            break

        if selected_location in locations.keys():
            os.system(f"mv -v '{SCREENSHOT_DIR}/{image}' '{locations[selected_location]}/{new_name}'")
        else:
            print(f'Wrong location name! {selected_location}')

        return


def on_image_added_listener(listener):
    global is_location_set
    new_images = set()

    while True:
        new_images.update(set(os.listdir(SCREENSHOT_DIR)).difference(images))
        old_images = set()

        for image in new_images:
            if is_location_set:
                function_lock(listener, image)
                old_images.add(image)

        new_images.difference_update(old_images)

        time.sleep(1)


@synchronized
def on_key_press(key):
    global is_location_set
    global selected_location

    if key == Key.esc:
        if is_location_set:
            selected_location = ''
            is_location_set = False
        else:
            os._exit(0)


def listen_for_new_images():
    initial_time = time.time()
    timing = -1
    new = True

    def key_listener():
        with Listener(
            on_press=on_key_press
        ) as listener:
            listener.join()

    Thread(target=key_listener).start()

    Thread(target=on_image_added_listener, args=(move_image, )).start()

    while True:
        if (time.time() - initial_time) > 300 * SEC_IN_A_MIN:
            exit()

        function_lock(ask_for_location_to_move)

        time.sleep(1)



def move_from_picture_dir():
    print('#' * (max([len(x) for x in images]) + 4))
    for i, image_name in enumerate(images):
        print()
        print(f' {i}. {image_name}')

    print()
    print('#' * (max([len(x) for x in images]) + 4))

    img_to_move = images[int(input('Choose the file you want to move: '))]
    ask_for_location_to_move()


def main():
    menu_choises = {
        'l': listen_for_new_images,
        'm': move_from_picture_dir,
    }

    answer = ""
    while True:
        print("--------------------------------------------")
        answer = input("Choose 'listen mode' (l) or 'move mode' (m): ")

        if answer not in menu_choises.keys():
            continue

        menu_choises[answer]()

        break


if __name__ == "__main__":
    main()
