import os
import sys
from time import sleep


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def introduction(name, version, creator="Matheus Goulart"):
    print(f"{bcolors.OKGREEN}{name} {version} by {creator}{bcolors.ENDC}")


def debug(string):
    print(f"DEBUG: {bcolors.WARNING}{string}{bcolors.ENDC}")


def ask(string):
    print(f"{bcolors.OKCYAN}{string}{bcolors.ENDC}")


def statement(string):
    print(f"{bcolors.OKGREEN}{string}{bcolors.ENDC}")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def error(string):
    print(f"ERROR: {bcolors.FAIL}{string}{bcolors.ENDC}")


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def progress(done, total, length=20, string="", fill="█", empty=" "):

    # Calculate the percentage
    percent = (done / total) * 100

    # round to int
    percent = int(percent)

    # Calculate the amount of "hashes"
    hashes = fill * int(percent / 100 * length)

    # Calculate the amount of spaces
    spaces = empty * (length - len(hashes))

    # Print the progress bar

    print(
        f"|\r{bcolors.OKGREEN}{hashes}{bcolors.ENDC}{spaces}| {percent}%", end="\n")

    print(f"{bcolors.OKBLUE}{string}{bcolors.ENDC}")


def countdown(string, milliseconds):
    for i in range(milliseconds):
        clear()
        statement(string)
        statement(f"{(milliseconds - i)/1000}s")
        sleep(0.001)
    clear()
    return


def confirm(string, error_string):
    while True:
        choice = input(f"{bcolors.OKGREEN}[{string}(Y/n)]{bcolors.ENDC} ")
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            print(f"{bcolors.FAIL}{error_string}{bcolors.ENDC}")
