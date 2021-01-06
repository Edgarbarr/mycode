#!/usr/bin/env python3

def triangleMaker(number):
    triangle = ""
    for star in range(number):
        line = ""
        for numOfStar in range(star+1):
            line+="*"
        triangle+="\n"+line
    for star in range(number - 1,0,-1):
        line=""
        for numOfStar in range(star):
            line+="*"
        triangle+="\n"+line
    print(triangle)
triangleMaker(5)

