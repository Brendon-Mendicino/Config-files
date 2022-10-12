#!/bin/python3

import os
import time

images = sorted(os.listdir("/home/brendon/Pictures/"))

locations = {
    'ele': '/home/brendon/uni/appunti/elap/img',
    'con': '/home/brendon/uni/appunti/controlli/img',
    'rel': '/home/brendon/uni/tirocinio/relazione/img'
}

SEC_IN_A_MIN = 60


def ask_for_location_to_move(img):
    while True:
        print('Available locations:')

        print('#' * max([len(x) for x in list(locations.keys())]) * 2)
        for i, loc in enumerate(list(locations.keys())):
            print()
            print(f'# {i+1}. {loc}')

        print()
        print('#' * max([len(x) for x in list(locations.keys())]) * 2)
        print()

        location = input(f'Where? ({img}): ')
        new_name = input('New name: ')

        while input('are you sure? ') != 'y':
            new_name = input('New name: ')

        if set(locations.keys()).issuperset([location]):
            os.system(f"mv -v '/home/brendon/Pictures/{img}' '{locations[location]+'/'+new_name}'")
            break

        else:
            print('Wrong location!')
            print(set(locations.keys()))


def print_listening_str(timing, new):
    if new:
        print('listening           ', end='')
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


def listen_for_new_images():
    initial_time = time.time()
    timing = -1
    new = True

    while True:
        if (time.time() - initial_time) > 30 * SEC_IN_A_MIN:
            exit()

        print_listening_str(timing, new)
        time.sleep(1)

        new = False
        timing = (timing + 1) % 5

        new_images = set(os.listdir("/home/brendon/Pictures/")
                         ).difference(images)
        for image in new_images:
            new = True
            timing = 0
            ask_for_location_to_move(image)


def move_from_picture_dir():
    print('#' * (max([len(x) for x in images]) + 4))
    for i, image_name in enumerate(images):
        print()
        print(f' {i}. {image_name}')

    print()
    print('#' * (max([len(x) for x in images]) + 4))

    img_to_move = images[int(input('Choose the file you want to move: '))]
    ask_for_location_to_move(img_to_move)


def main():
    menu_c = {
        'l': listen_for_new_images,
        'm': move_from_picture_dir,
    }

    answer = ""
    while True:
        print("--------------------------------------------")
        answer = input("Choose 'listen mode' (l) or 'move mode' (m): ")

        if not set(menu_c.keys()).issuperset([answer]):
            continue

        menu_c[answer]()

        break


if __name__ == "__main__":
    main()
