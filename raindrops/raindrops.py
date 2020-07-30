"""Fizzbuzz code with raindrops"""

# first try
# def convert(number):
#     # create an empty string to add raindrops to
#     sound = ''
#     # create conditionals to go through each modulo
#     if number % 3 == 0:
#         sound += "Pling"
#     if number % 5 == 0:
#         sound += "Plang"
#     if number % 7 == 0:
#         sound += "Plong"
#     # if sound is empty because it doesn't have factor's return number as string
#     if sound == '':
#         return str(number)
#     return sound

# Second Try
# rain_drop_dict = {
#     "Pling": 3,
#     "Plang": 5,
#     "Plong": 7
# }


# def convert(number, dict=rain_drop_dict):
#     return_value = ''
#     for key, value in dict.items():
#         if number % value == 0:
#             return_value += key
#     if return_value == '':
#         return str(number)
#     return return_value


# test1 = convert(15, rain_drop_dict)
# print(test1)


# Third time's the charm
RULES = [
    ["Pling", 3],
    ["Plang", 5],
    ["Plong", 7]
]

def convert(num, arr=RULES):
    filtered = [rain_drop[0] for rain_drop in arr if num % rain_drop[1] == 0]
    if filtered:
        return "".join(filtered)
    return str(num)

test1 = convert(1)
print(test1)