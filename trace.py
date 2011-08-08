#!/usr/bin/env python2

# Author: David Larsen <dcl9934@cs.rit.edu>
# Date: Mon, 08 Aug 2011 05:23:39 -0400
# License: Public Domain


"""
Function decorator for tracing recursive calls.

Includes the @trace.trace decorator and several example functions.
"""

class trace():
    """
    Function decorator for tracing recursive calls.

    You can trace a function by decorating it with @trace at defintion, as in foo().
    Note that you can also use trace by decorating it directly:

    foo = trace(foo)

    But recursive calls to foo will not be traced, because they refer to the old
    defintion of foo. This is not a problem with the @ decoration technique.

    TODO:
    - Make pretty
    - Fix docstrings in pydoc. (Dynamicaly generating anonymous functions seems
      to do the trick. I just hope that I can keep my data private.) Closures?
    """

    calldepth = 0
    indentation_string = "|  "

    def __init__( self, function ):
            self.f = function
            self.__doc__ = function.__doc__

    def __call__( self, *args, **kwargs ):
        function_string = self.f.__name__ + "( " + str( args ) + " " + str( kwargs ) +  " )"
        print str(trace.indentation_string * trace.calldepth) + function_string

        # Use trace.calldepth to modify the variable at the class scope.
        trace.calldepth += 1
        retval = self.f( *args, **kwargs )
        trace.calldepth -= 1

        print str(trace.indentation_string * trace.calldepth) + function_string +\
            " returns: " + str(retval)

        return retval

@trace
def foo( num = 10 ):
    """
    Used for testing functions with zero or one arguments, using default
    assignment. Also great for testing values pased by keyword.
    """
    if num > 0:
        foo( num - 1)
        return num

@trace
def foobar( const, num = 10 ):
    """
    Used for testing calls that can have multiple (or singular) parameters and
    for setting parameters by name.
    """
    if num > 0:
        foobar( const, num - 1 )
        return const

@trace
def one( num = 10 ):
    """
    Demonstrates recursive calls between two functions.
    """
    if num > 0:
        two( num - 1 )
        return num

@trace
def two( num = 10 ):
    """
    See one().
    For a good time, try removing @trace from either declaration and see what
    happns.
    """
    if num > 0:
        one( num - 1 )
        return num
