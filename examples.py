from ftrace import ftrace

@ftrace
def foo( num = 10 ):
    """
    Used for testing functions with zero or one arguments, using default
    assignment. Also great for testing values pased by keyword.
    """
    if num > 0:
        foo( num - 1)
    return num

@ftrace
def foobar( const, num = 10 ):
    """
    Used for testing calls that can have multiple (or singular) parameters and
    for setting parameters by name.
    """
    if num > 0:
        foobar( const, num - 1 )
    return const

@ftrace
def one( num = 10 ):
    """
    Demonstrates recursive calls between two functions.
    """
    if num > 0:
        two( num - 1 )
    return num

@ftrace
def two( num = 10 ):
    """
    See one().
    For a good time, try removing @ftrace from either declaration and see what
    happens.
    """
    if num > 0:
        one( num - 1 )
    return num

@ftrace
def qsort( unsorted_list ):
    """
    Quicksort
    """
    if len( unsorted_list ) < 2:
        return unsorted_list
    
    pivot = unsorted_list[0]
    pivot_count = 0
    smaller = list()
    larger = list()

    for element in unsorted_list:
        if element == pivot:
            pivot_count += 1
        elif element < pivot:
            smaller.append(element)
        else:
            larger.append(element)
    
    return qsort(smaller) + ([pivot] * pivot_count) + qsort(larger)

class test():
    @ftrace
    def method(self):
        """
        An object method.
        """
        return

    @classmethod
    @ftrace
    def cls_method(cls):
        """
        A class method.
        """
        return

    @staticmethod
    @ftrace
    def static_method():
        """
        A static method.
        """
        
