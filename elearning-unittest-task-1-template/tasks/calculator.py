import math


class Calculator:
    """
    Constructor.
    """

    def __init__(self):
        pass

    def sum(self, value_1, value_2):
        """
        Sum method - given two numbers.

        :param value_1: the value of first

        :param value_2: the value of second

        :return: the addition
        """
        return value_1 + value_2

    def multiply(self, value_1, value_2):
        """
        Multiply method - given two numbers.

        :param value_1: the value of first

        :param value_2: the value of second

        :return: reference name the multiplication of the two
        """
        return value_1 * value_2

    def subtract(self, value_1, value_2):
        """
        Subtract method - given two numbers.

        :param value_1: the value of first

        :param value_2: the value of second

        :return: the value of first value minus the second
        """
        return value_1 - value_2

    def divide(self, value_1, value_2):
        """
        Divide method - given two numbers.

        :param value_1: the value of first

        :param value_2: the value of second

        :return: the value of first value divided by the second
        """
        if value_2 != 0:
            return value_1 / value_2

    def sqrt(self, value_1):
        """
        Sqrt is an inbuilt function that returns.

        :param value_1: the value of first

        :return: the square root of any number
        """
        return float('%.2f' % math.sqrt(value_1))

    def pi(self, value_1):
        """
        The degree value to be converted into radians.

        :param value_1: the value of first

        :return:  if x is passed as a parameter in degrees,
        then the function (radians(x)) returns the radian value of that angle
        """
        return float('%.2f' % math.radians(value_1))
