#!/usr/bin/env python2

# Author: David Larsen <dcl9934@cs.rit.edu>
# Date: Mon, 08 Aug 2011 05:23:39 -0400
# License: Public Domain


"""
Function decorator for tracing recursive calls.

Includes the @trace.ftrace decorator and several example functions.

TODO:
- Implement unftrace() -- could be tricky...
"""

def ftrace( function ):
    """
    Function decorator for tracing recursive calls.

    You can ftrace a function by decorating it with @ftrace at defintion, as in
    foo().
    Note that you can also use ftrace by decorating it directly:

    foo = ftrace(foo)

    But recursive calls to foo will not be ftraced, because they refer to the
    old defintion of foo. This is not a problem with the @ decoration
    technique.

    Also, if you're using certain decorators, such as the magic @classmethod
    and @staticmethod, you should have them exicute _after_ ftrace, like so:

    @staticmethod
    @ftrace
    def foo(): ...

    or

    foo = staticmethod( ftrace( foo ) )

    TODO:
    - Make pretty
    - Gracefully handle @classmethod and @staticmethod
    """

    ftrace.indentation_string = "|  "
    if not hasattr( ftrace, "calldepth" ):
        ftrace.calldepth = 0

    def decoration( *args, **kwargs ):
        function_string = function.__name__ + "( " + str( args ) + " " + str( kwargs ) +  " )"
        print str(ftrace.indentation_string * ftrace.calldepth) + function_string

        # Use ftrace.calldepth to modify the variable at the class scope.
        ftrace.calldepth += 1
        retval = function( *args, **kwargs )
        ftrace.calldepth -= 1

        print str(ftrace.indentation_string * ftrace.calldepth) + function_string +\
            " returns: " + str(retval)

        return retval

    # Preserve docstrings for the function we're decorating.
    decoration.__name__ = function.__name__
    decoration.__doc__ = function.__doc__

    return decoration

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
        return
