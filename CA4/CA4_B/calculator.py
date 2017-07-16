class Calculator(object):
    """
    This module contains ten mathematical functions, written for
    a scientific calculator that can be applied to single values or lists
    """
    # data types that can be used for parameters in different calculations
    number_types = (int, long, float, complex)
    integer_number_types = (int, long)
    real_number_types = (int, long, float)

    def __apply_two_values_or_lists(self, fn, x_data, y_data):
        """
        Applies function to two values. If x_data or y_data is a list, uses
        each value from the list and returns a list of the results.
        :param fn: function that calculates something from x and y values
        :param x_data: single value or list for the x-parameter
        :param y_data: single value or list for the y-parameter
        :return: returns result of function fn or list of results of fn
        """
        if isinstance(x_data, list):
            if isinstance(y_data, list):
                return map(fn, x_data, y_data)
            else:
                return map(
                    lambda one_from_x: fn(one_from_x, y_data),
                    x_data)

        else:
            if isinstance(y_data, list):
                return map(
                    lambda one_from_y: fn(x_data, one_from_y),
                    y_data)
            else:
                return fn(x_data, y_data)

    def __apply_value_or_list(self, fn, x_data):
        """
        Applies function to one value. If x_data is a list, uses
        each value from the list and returns a list of the results.
        :param fn: function that calculates something from x value.
        :param x_data: single value or list for the x-parameter
        :return: returns result of function fn or list of results of fn
        """
        if isinstance(x_data, list):
            return map(fn, x_data)
        else:
            return fn(x_data)

    # calculate the factorial of the natural number n
    # raises ValueError unless n is a whole number greater or equal to zero
    def factorial(self, lsn):
        def factorial(n):
            if (not isinstance(n, self.integer_number_types)
               or n < 0):
                raise ValueError
            if n > 1:
                return n * factorial(n - 1)
            return 1
        return self.__apply_value_or_list(factorial, lsn)

    # add numbers x and y and return the result
    # raises ValueError unless x and y are numbers
    def add(self, x_data, y_data):
        def add(x, y):
            if not (isinstance(x, self.number_types)
                    and isinstance(y, self.number_types)):
                raise ValueError
            return x + y

        return self.__apply_two_values_or_lists(add, x_data, y_data)

    # subtract number y from x and return the result
    # raises ValueError unless x and y are numbers
    def subtract(self, x_data, y_data):
        def subtract(x, y):
            if not (isinstance(x, self.number_types)
                    and isinstance(y, self.number_types)):
                raise ValueError

            return x - y

        return self.__apply_two_values_or_lists(subtract, x_data, y_data)

    # multiply number x by y and return the result
    # raises ValueError unless x and y are numbers
    def multiply(self, x_data, y_data):
        def multiply(x, y):
            if not (isinstance(x, self.number_types)
                    and isinstance(y, self.number_types)):
                raise ValueError

            return x * y

        return self.__apply_two_values_or_lists(multiply, x_data, y_data)

    # divide number x by y and return the result
    # raises ValueError if x or y are not numbers or y is zero
    def divide(self, x_data, y_data):
        def divide(x, y):
            if (not (isinstance(x, self.number_types)
                     and isinstance(y, self.number_types))
               or y == 0):
                raise ValueError

            return float(x) / y

        return self.__apply_two_values_or_lists(divide, x_data, y_data)

    # get square root of the number x and return the result
    # raises ValueError unless x is a number
    def square_root(self, x_data):
        def square_root(x):
            if not isinstance(x, self.number_types):
                raise ValueError

            return self.nth_root(x, 2)

        return self.__apply_value_or_list(square_root, x_data)

    # get nth root of the number x and return the result
    # raises ValueError if x or n are not numbers or n is zero
    def nth_root(self, x_data, n_data):
        def nth_root(x, n):
            if (not (isinstance(x, self.number_types)
                     and isinstance(n, self.number_types))
               or n == 0):
                raise ValueError

            return x ** (1.0 / n)

        return self.__apply_two_values_or_lists(nth_root, x_data, n_data)

    # get nth power of the number x and return the result
    # raises ValueError unless x and n are numbers
    def power(self, x_data, n_data):
        def power(x, n):
            if not (isinstance(x, self.number_types)
                    and isinstance(n, self.number_types)):
                raise ValueError

            return x ** n

        return self.__apply_two_values_or_lists(power, x_data, n_data)

    # get logarithm of the number x and return the result
    # raises ValueError unless x is a real number
    def logarithm(self, x_data):
        def logarithm(x):
            from math import log

            if not (isinstance(x, self.real_number_types)):
                raise ValueError

            return log(x, 10)
        return self.__apply_value_or_list(logarithm, x_data)

    # get reciprocal of x and return the result
    # raises ValueError if x is not a number or if x is zero
    def reciprocal(self, x_data):
        def reciprocal(x):
            if (not (isinstance(x, self.number_types))
               or x == 0):
                raise ValueError

            return x ** (-1)
        return self.__apply_value_or_list(reciprocal, x_data)
