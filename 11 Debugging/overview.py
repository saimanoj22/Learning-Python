#Debugging

# There are generally two methods
#   i)looking at logging and assertions
#   ii)using a debugger

# Raising Exceptions
'''     • raise keyword
        • call to the Exception() function
        • a string with a helpful message passed ti the Exception() function
'''
'''
When Python encounters an error, it produces a treasure trove of error information
called the traceback. The traceback includes the error message, the
line number of the line that caused the error, and the sequence of the function
calls that led to the error. This sequence of calls is called the call stack.
'''

import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# traceback.format_exc helps to collect all exceptions in a file, while keeping the program running

# Assertions
'''
An assertion is a sanity check to make sure your code isn’t doing something
obviously wrong.
    • The assert keyword
    • A condition (that is, an expression that evaluates to True or False)
    • A comma
    • A string to display when the condition is False
If you run a Python script with python -O myscript.py instead of python myscript.py, Python will skip assert statements.
'''

# Logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
'''
The nice thing about log messages is that you’re free to fill your program
258 Chapter 11
with as many as you like, and you can always disable them later by adding
a single logging.disable(logging.CRITICAL) call.
'''
'''
Logging levels - five
--------------------------------------------------------------------------------------
Level             Logging function                Description
--------------------------------------------------------------------------------------
DEBUG               logging.debug()         The lowest level. Used for small details.
                                            Usually you care about these messages
                                            only when diagnosing problems.

INFO                logging.info()          Used to record information on general
                                            events in your program or confirm that
                                            things are working at their point in the
                                            program.

WARNING             logging.warning()       Used to indicate a potential problem
                                            that doesn’t prevent the program from
                                            working but might do so in the future.

ERROR               logging.error()         Used to record an error that caused the
                                            program to fail to do something.

CRITICAL            logging.critical()      The highest level. Used to indicate a
                                            fatal error that has caused or is about
                                            to cause the program to stop running
                                            entirely.
-------------------------------------------------------------------------------------
'''
# Logging to a File
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
'''
The log messages will be saved to myProgramLog.txt.
'''