import control
import os
from colorama import init, Fore, Back, Style
init()

os.system('cls')
print(Style.BRIGHT + 'Привет, это простой консольный калькулято!\n'
      'Введи ему значения и выбери операцию. Вперед!\n')

control.buttun_click()
