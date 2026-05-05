# import os
#
# print("Welcome to bidding auction!")
# dict = {}
# maximum = 0
# highest_bidder = ""
# answer = "y"
# # name = input("Please enter your name: ")
# # dict[name] = float(input("Please enter your bid: "))
# #
# # answer = input("Are there other bidders? y/N ").lower()
#
# while answer != "n":
#     name = input("Please enter your name: ")
#     dict[name] = float(input("Please enter your bid: "))
#     answer = input("Are there other bidders? y/N ").lower()
#
#     print("\n" * 50)
#
#
# for entry in dict.keys():
#     if dict[entry] > maximum:
#         maximum = dict[entry]
#         highest_bidder = entry
#
#
#
#
# print(f"The highest bidder with ${round(maximum, 2)} is {highest_bidder}!")

from student import Student

def main():
    Student(input("What is your name? "), input("What is your house? "))

if __name__ == "__main__":
    main()