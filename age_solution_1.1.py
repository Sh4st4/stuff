# -*- coding: utf-8 -*-

name = input('Enter a name')
age = int(input ('Enter the age'))

import datetime
now = datetime.datetime.now()

mid_result = 100 - age
end_result = (now.year) + mid_result
end_result = str(end_result)

print(name + ', you will turn 100 years old in ' + end_result)
