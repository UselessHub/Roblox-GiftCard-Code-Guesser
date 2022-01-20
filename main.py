from colorama import Fore, init
from time import sleep
import os
import platform
import random
import string
import time
import sys
from random import choice

init()  

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def printTitle():
    print(f""" 
{Fore.RED}██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░██████╗░███████╗███╗░░██╗
{Fore.RED}██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔════╝░██╔════╝████╗░██║
{Fore.RED}██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██║░░██╗░█████╗░░██╔██╗██║
{Fore.RED}██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ██║░░╚██╗██╔══╝░░██║╚████║
{Fore.RED}██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚██████╔╝███████╗██║░╚███║
{Fore.RED}╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝\n{Fore.GREEN}                         Created by Useless{Fore.RESET}\n\n""")

def show2():
    print(f"{Fore.RED} Thanks for Using (MADE BY USELESS)")
    input()
    startMenu()

def show1():
    print(f"{Fore.RED}[1]{Fore.RESET} Fast Mode\n{Fore.RED}[2] {Fore.RESET}Fastest mode (could generate a bit less than the number of codes you want)\n{Fore.RED}[3] {Fore.RESET}Progress Mode (slowest)")
    c = int(input(f'> {Fore.RED}'))
    if c == 1:
        clear()
        show11()
    if c == 2:
        clear()
        show12()
    if c == 3:
        clear()
        show13()
    if c not in [1,2,3]:
        print(f'{Fore.YELLOW}Invalid Option!')
        sleep(2)
        clear()
        printTitle()
        show1()

def show11():
        print(f'{Fore.RED}How many codes would you like to generate{Fore.RESET}')
        c = int(input(f'> {Fore.RED}'))
        print(f'{Fore.RESET}')
        clear()
        startTime = time.strftime("%H:%M:%S ", time.localtime())
        print(f'Process started at: {Fore.LIGHTBLUE_EX}{startTime}{Fore.RESET}')
 
        with open('roblox.txt', 'a+') as f:
            for i in range(0, c):
                f.flush()
                code = choice(string.digits) + choice(string.digits) + choice(string.digits) + ' ' + choice(string.digits) + choice(string.digits) + choice(string.digits) + ' ' + choice(string.digits) + choice(string.digits) + choice(string.digits) + choice(string.digits)
                f.write(code + '\n')
            
        endTime = time.strftime("%H:%M:%S ", time.localtime())
        print('Process ended at: ' + Fore.LIGHTBLUE_EX + endTime + Fore.RESET, end='')
        print(f'\n{Fore.GREEN}Succesfully generated {c} codes{Fore.RESET}')

        input()
        startMenu()
    
def show12():
        print(f'{Fore.RED}How many codes would you like to generate{Fore.RESET}')
        c = int(input(f'> {Fore.RED}'))
        print(f'{Fore.RESET}')
        clear()
        startTime = time.strftime("%H:%M:%S ", time.localtime())
        print(f'Process started at: {Fore.LIGHTBLUE_EX}{startTime}{Fore.RESET}')
        with open('roblox.txt', 'a+') as f:
            for i in range(0, c):
                code = choice(string.digits) + choice(string.digits) + choice(string.digits) + ' ' + choice(string.digits) + choice(string.digits) + choice(string.digits) + ' ' + choice(string.digits) + choice(string.digits) + choice(string.digits) + choice(string.digits)
                f.write(code + '\n')
        endTime = time.strftime("%H:%M:%S ", time.localtime())
        print('Process ended at: ' + Fore.LIGHTBLUE_EX + endTime + Fore.RESET, end='')
        print(f'\n{Fore.GREEN}Succesfully generated {c} codes{Fore.RESET}')

        input()
        startMenu()

def show13():
        print(f'{Fore.RED}How many codes would you like to generate{Fore.RESET}')
        c = int(input(f'> {Fore.RED}'))
        print(f'{Fore.RESET}')
        clear()
        startTime = time.strftime("%H:%M:%S ", time.localtime())
        print(f'Process started at: {Fore.LIGHTBLUE_EX}{startTime}{Fore.RESET}[⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀]') 
        
        tenth = c//10
        with open('roblox.txt', 'a+') as f:
            for i in range(0, c):
                f.flush()
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
                code = choice(string.digits) + choice(string.digits) + choice(string.digits) + ' ' + choice(string.digits) + choice(string.digits) + choice(string.digits) + ' ' + choice(string.digits) + choice(string.digits) + choice(string.digits) + choice(string.digits)
                f.write(code + '\n')
                if i == tenth:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⠀⠀⠀⠀⠀⠀⠀⠀⠀]')
                if i == tenth*2:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⠀⠀⠀⠀⠀⠀⠀⠀]')
                if i == tenth*3:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⠀⠀⠀⠀⠀⠀⠀]')
                if i == tenth*4:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⬛⠀⠀⠀⠀⠀⠀]')
                if i == tenth*5:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⬛⬛⠀⠀⠀⠀⠀]')
                if i == tenth*6:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⬛⬛⬛⠀⠀⠀⠀]')
                if i == tenth*7:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⬛⬛⬛⬛⠀⠀⠀]')
                if i == tenth*8:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⬛⬛⬛⬛⬛⠀⠀]')
                if i == tenth*9:
                    clear()
                    print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
                    print('[⬛⬛⬛⬛⬛⬛⬛⬛⬛⠀]')  
            clear()

        print('Process started at" ' + Fore.LIGHTBLUE_EX + startTime + Fore.RESET, end='')
        endTime = time.strftime("%H:%M:%S ", time.localtime())
        print('\nProcess ended at: ' + Fore.LIGHTBLUE_EX + endTime + Fore.RESET, end='')
        print(f'\n{Fore.GREEN}Succesfully generated {c} codes{Fore.RESET}')

        input()
        startMenu()

def startMenu():
    clear()
    printTitle()
    print(f'{Fore.RED}[1]{Fore.RESET} Generator\n{Fore.RED}[2]{Fore.RESET} Help')
    c = int(input('> '))
    if c == 1:
        clear()
        printTitle()
        show1()

    if c == 2:
        clear()
        printTitle()
        show2()

    if c not in [1, 2]:
        print(f'{Fore.YELLOW}Invalid option!')
        sleep(2)
        startMenu()

startMenu()
