# Developed by MIT 6.034

from point_api import Point

################################################################################
# Note: Each function we require you to fill in has brief documentation        # 
# describing what the function should input and output.                        #
################################################################################


#### Warmup ####################################################################

def is_even(x):
    "If x is even, returns True; otherwise returns False"
 
    Raise NotImplementedError

def decrement(x):
    """Given a number x, returns x - 1 unless that would be less than
    zero, in which case returns 0."""
    Raise NotImplementedError

def cube(x):
    "Given a number x, returns its cube (x^3)"
    Raise NotImplementedError


#### Iteration #################################################################

def is_prime(x):
    """Given a number x, returns True if it is prime; otherwise returns False--
    assuming 2 is the first prime number"""
    Raise NotImplementedError

def primes_up_to(x):
    """Given a number x, returns an in-order list of all primes up to and including x--
    hint: you can use the is_prime function you just created"""
    Raise NotImplementedError


#### Built-in data types #######################################################

def remove_from_string(string, letters):
    """Given a string and a list of individual letters, returns a new string
    which is the same as the old one except all occurrences of those letters
    have been removed from it."""
    Raise NotImplementedError

def compute_string_properties(string):
    """Given a string of lowercase letters, returns a tuple containing the
    following three elements:
        0. The length of the string
        1. A list of all the characters in the string (including duplicates, if
           any), sorted in REVERSE alphabetical order
        2. The number of distinct characters in the string (hint: use a set)
    """
    Raise NotImplementedError

def tally_letters(string):
    """Given a string of lowercase letters, returns a dictionary mapping each
    letter to the number of times it occurs in the string."""
    Raise NotImplementedError


#### Objects and APIs: Copying and modifing objects ############################

def sum_of_coordinates(point):
    """Given a 2D point (represented as a Point object), returns the sum
    of its X- and Y-coordinates."""
    Raise NotImplementedError

def get_neighbors(point):
    """Given a 2D point (represented as a Point object), returns a list of the
    four points that neighbor it in the four coordinate directions. Uses the
    "copy" method to avoid modifying the original point."""
    Raise NotImplementedError


#### SURVEY ####################################################################

# How much programming experience do you have, in any language?
#     A. No experience (never programmed before this lab)
#     B. Beginner (just started learning to program, e.g. took one programming class)
#     C. Intermediate (have written programs for a couple classes/projects)
#     D. Proficient (have been programming for multiple years, or wrote programs for many classes/projects)
#     E. Expert (could teach a class on programming, either in a specific language or in general)

PROGRAMMING_EXPERIENCE = None


# How much experience do you have with Python?
#     A. No experience (never used Python before this lab)
#     B. Beginner (just started learning, e.g. took 6.0001)
#     C. Intermediate (have used Python in a couple classes/projects)
#     D. Proficient (have used Python for multiple years or in many classes/projects)
#     E. Expert (could teach a class on Python)

PYTHON_EXPERIENCE = None
