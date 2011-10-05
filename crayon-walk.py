"""A random walk simulation to create a pleasing image, inspired by:
http://www.flickr.com/photos/collincl365/6198991611/in/pool-28845821@N00/

"""
from random import choice, gauss
from turtle import *

numturts = 10
mean = 40
sd = 10

def fwd(turt):
    turt.fd(max(20, gauss(mean, sd)))

def rgt(turt):
    turt.rt(90)
    turt.fd(max(10, gauss(20, 5)))
    turt.lt(90)
    turt.fd(max(20, gauss(mean, sd)))

def lft(turt):
    lt(90)
    fd(max(10, gauss(20, 5)))
    rt(90)
    fd(max(20, gauss(mean, sd)))

def stay(turt):
    pass

choices = [fwd, rgt, lft, stay]
turts = [Turtle() for i in xrange(numturts)]

# TODO: Setup code. (setup, speed, tracer, width, color, etc.)
# TODO: Position each turtle in turts.

for i in xrange(10):
    for turt in turts:
        move = choice(choices)
        move()

update()
