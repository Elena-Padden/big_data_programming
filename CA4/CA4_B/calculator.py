# This module contains ten mathematical functions, written for a scientific calculator


class Calculator(object):

# data types that can be used for parameters in different calculations 
    number_types = (int, long, float, complex)
    integer_number_types = (int, long)
    real_number_types = (int, long, float)

    def __apply_two_values_or_lists(self,fn,x,y):
        if isinstance(x,list) != isinstance(y,list):
            raise ValueError("Either both or neither parameters should be a list")
        if isinstance(x,list):
            return map(fn,x,y)
        else:
            return fn(x,y)


# calculate the factorial of the natural number n
# raises ValueError unless n is a whole number greater or equal to zero
    def factorial(self, lsn):
        def factorial(n):
            if (not isinstance(n, self.integer_number_types)
                    or n <0):
                    raise ValueError
            if n >1:
                    return n * factorial (n-1)
            return 1
        if isinstance(lsn,list):
            return map(factorial,lsn)
        else:
            return factorial(lsn)
       
# add numbers x and y and return the result
# raises ValueError unless x and y are numbers
    def add(self, x, y):
        def add(x,y):
            if not (isinstance(x, self.number_types)
                    and isinstance(y, self.number_types)):
                raise ValueError
            return x + y
        return self.__apply_two_values_or_lists(add,x,y)
            
# subtract number y from x and return the result
# raises ValueError unless x and y are numbers
    def subtract(self, x, y):
        def subtract(x,y):
            if not (isinstance(x, self.number_types)
                    and isinstance(y, self.number_types)):
                raise ValueError
            
            return x - y
        return self.__apply_two_values_or_lists(subtract,x,y)        
        
# multiply number x by y and return the result
# raises ValueError unless x and y are numbers
    def multiply(self, x, y):
        if not (isinstance(x, self.number_types)
                and isinstance(y, self.number_types)):
            raise ValueError

        return x * y

# divide number x by y and return the result
# raises ValueError if x or y are not numbers or y is zero 
    def divide(self, x, y):
        if (not (isinstance(x, self.number_types)
                and isinstance(y, self.number_types))
                or y == 0):
            raise ValueError

        return float(x)/y
        
# get square root of the number x and return the result
# raises ValueError unless x is a number
    def square_root(self, x):
        if not isinstance(x, self.number_types):
            raise ValueError
        
        return self.nth_root(x,2)
        
# get nth root of the number x and return the result
# raises ValueError if x or n are not numbers or n is zero 
    def nth_root(self, x, n):
        if (not (isinstance(x, self.number_types)
                and isinstance(n, self.number_types))
           or n==0):
            raise ValueError
            
        return x ** (1.0/n)
        
# get nth power of the number x and return the result
# raises ValueError unless x and n are numbers
    def power(self, x, n):
        if not (isinstance(x, self.number_types)
                and isinstance(n, self.number_types)):
            raise ValueError
            
        return x ** n

# get logarithm of the number x and return the result
# raises ValueError unless x is a real number
    def logarithm(self, x):
        from math import log
        
        if not (isinstance(x, self.real_number_types)):
            raise ValueError

        return log(x, 10)

# get reciprocal of x and return the result
# raises ValueError if x is not a number or if x is zero
    def reciprocal(self, x):
        if (not (isinstance(x, self.number_types))
        or x == 0):
            raise ValueError
               
        return x ** (-1)        
 
        
        
        
        
        
        



