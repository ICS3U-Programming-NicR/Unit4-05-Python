#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: April 20 2022
# Find the sum of numbers


def main():
    while True:
        # Get inputs
        tot_num_str = input("How many numbers would you like to add together: ")
        # try catch
        try:
            tot_num = int(tot_num_str)
            if tot_num < 0:
                print("The total amount cannot be negative")
                continue
            else:
                sum_equation = ""
                sum = 0
                counter = 0
                while True:
                    num_as_string = input("what number would you like to add: ")
                    try:
                        num = int(num_as_string)
                        if num > 0:
                            counter += 1
                            sum = num + sum
                            print("{} added to total sum".format(num))
                            if counter == 1:
                                sum_equation = num_as_string
                            else:
                                sum_equation = "{} + {}".format(
                                    sum_equation, num_as_string
                                )
                        else:
                            print("your number cannot be 0")
                            continue
                    except:
                        print("your number has to be an integer")
                        continue
                    if counter >= tot_num:
                        break
                print("{} = {}".format(sum_equation, sum))
        except:
            print("your total number has to be an int")
            continue


if __name__ == "__main__":
    main()
