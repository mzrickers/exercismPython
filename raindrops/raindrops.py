"""Fizzbuzz code with raindrops"""

def convert(number):
    # create an empty string to add raindrops to
    sound = ''
    # create conditionals to go through each modulo
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    # if sound is empty because doesn't have factor's return number as string
    if sound == '':
        return str(number)
    return sound

