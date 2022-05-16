import sys
from termios import TCIOFLUSH, tcflush
from time import sleep
from double_linked_list import DoubleLinkedList
import os
import pathlib
import keyboard


def clear(title="SUPER DUPER ULTRA FILE VIEWER"):
    tcflush(sys.stdin, TCIOFLUSH)
    os.system('cls' if os.name == 'nt' else 'clear')
    delimeter = "=" * len(title)
    print(f"|{title}|\n|{delimeter}|\n")


chosen_path = '.'

while True:
    clear()

    chosen_path = input("Select a directory to work with ('\q' to exit): ")
    if chosen_path == '\q':
        break

    workspace = pathlib.Path(chosen_path).absolute()

    if not workspace.exists():
        os.mkdir(workspace)

    if not workspace.is_dir():
        raise Exception("Couldn't find directory, file found")

    listDir = os.listdir(workspace)
    files = DoubleLinkedList()

    for file in listDir:
        path = pathlib.Path(os.path.join(workspace, file))
        try:
            content = path.read_text()
        except:
            content = "[WRONG FILE ENCODING]"

        if path.is_file():
            files.append({
                "title": file,
                "content": content
            })

    opt = 0
    while opt != -1:
        clear()

        index = 0
        node = files.first
        while node:
            print(str(index + 1) + ". " + node.data["title"])
            node = node.next
            index += 1

        opt = input("\nSelect a file to start editing (0 to go back): ")
        opt = int(opt) - 1

        if opt < 0:
            break

        viewing = files.at(opt)
        key = None
        prevKey = None

        while viewing != None:
            clear(viewing.data["title"])
            print(viewing.data["content"])
            print("\n\nUse <- and -> to move around ('\q' to exit)")

            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name

                if key == 'left':
                    viewing = viewing.prev if viewing.prev != None else viewing
                if key == 'right':
                    viewing = viewing.next if viewing.next != None else viewing

                if prevKey == '\\' and key == 'q':
                    clear()
                    viewing = None
                    event = None
                    sleep(0.1)

                prevKey = key
