# functions
import math

from variables import area


def greet():
    print("Hello,functions")


def area_circle(radius):
    result = 22 / 7 * radius ** 2
    result = round(result)
    print(result)


def volume_cylinder(radius, height, precision=2):
    volume = 22 / 7 * radius ** 2 * height
    volume = round(volume, precision)
    print(f" Radius is {radius}, Height is {height}, volume is {volume}")


def area_triangle(a, b, c):
    """Calculates the area of a triangle and then returns the results"""
    # s = (a + b + c) / 2
    #    area = (s * (s - a) * (s - b) * (s - c))
    #     area = math.sqrt(area)
    #        print(area)
    #   return area



def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result

# print(factorial(5))


def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

#variables args
# print(add_numbers(10, 4, 4))

#cash Ksh3000
def no_word(word):
    text = "ksh3000"
    words = text.split()
    numbers = list(filter(str.isdigit, words))
    cleaned_text = ' '.join(numbers)
    print(cleaned_text)


# use a function == call a function

# area_triangle(20, 25, 30)


# volume_cylinder(11, 35, 2)
# volume_cylinder(height=21, radius=5, precision=3) #nmed params


# area_circle(7)
# area_circle(169)
# area_circle


# greet()
