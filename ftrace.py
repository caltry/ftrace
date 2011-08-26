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

    You can ftrace a function by decorating it with @ftrace at definition, eg:

        @ftrace
        def foo():
            ...

    Note that you can also use ftrace by decorating it directly:

        foo = ftrace(foo)

    Also, if you're using certain decorators, such as the magic @classmethod
    and @staticmethod, you should have them execute _after_ ftrace, like so:

        @staticmethod
        @ftrace
        def foo(): ...

    or

        foo = staticmethod( ftrace( foo ) )

    TODO:
    - Make pretty
    """

    # Actions on variables that begin with `ftrace.' mean to do so at the class
    # scope. This allows state, such as call depth, to be persistent through
    # different function calls. See test.one() for an example.

    ftrace.indentation_string = "|  "
    if not hasattr( ftrace, "calldepth" ):
        ftrace.calldepth = 0

    def decoration( *args, **kwargs ):
        function_string = function.__name__ + "( " + str( args ) + " " + str( kwargs ) +  " )"
        print((ftrace.indentation_string * ftrace.calldepth) + function_string)

        # Use ftrace.calldepth to modify the variable at the class scope.
        ftrace.calldepth += 1
        retval = function( *args, **kwargs )
        ftrace.calldepth -= 1

        print((ftrace.indentation_string * ftrace.calldepth) +\
            function_string + " returns: " + str(retval))

        return retval

    # Preserve docstrings for the function we're decorating.
    decoration.__name__ = function.__name__
    decoration.__doc__ = function.__doc__

    return decoration
