#!/usr/bin/env python3
print("Hello New York")
name = "esra"
print(name)
name = "esra"
color = "blue"
activity = "broomball"
print(name, color, activity)
animal = "cat"
print(name, color, activity, animal)
print(f'My name is: {name} andmy fav color is {color} and my fav activity is {activity} and lastly I love my {animal}.')

#try sys.argv from the command line
import sys
name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]
# now print a message to the screen
print('My name is',name,',my fav color is', color, ',my fav activiy is', activity, 'and I love', animal)
