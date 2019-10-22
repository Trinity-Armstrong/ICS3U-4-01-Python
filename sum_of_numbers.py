#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: October 2019
# This is the sum of numbers program


def main():
    # This funtion runs the sum of numbers program

    # variables
    sum = 0
    counter = 1

    # input
    integer = int(input("Enter a positive integer: "))
    print("")

    # process
    while integer >= counter:
        sum = sum + counter
        counter += 1

    # output
    print("The sum of all numbers is", sum)


if __name__ == "__main__":
    main()
