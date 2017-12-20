# -*- coding: utf-8 -*-

number = int(input('Gimme a number to check'))
check = int(input('Gimme a number to divide by'))

if number % 4 == 0:
    print('The numba is a multiple of four')
elif number % 2 == 0:
    print('The numba is even')
else:
    print('The numba is odd')

if number % check == 0:
    print(number, 'divides evenly by', check)
else:
    print(number, "doesn't divide evenly by", check)