
# 1. Documentation

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


# 1. Fancier Output Formatting

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

import math
print(f'The value of pi is approximately {math.pi:.3f}.')



