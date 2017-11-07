import math

def longest_side(a,b):

    """
    Function to find the length of the longest side of a right triangle.

    :arg a:Side a of the the triangle 

    :arg b: Side b of the longest side c as float 

    """

    return math.sqrt(a*a + b*b)

if __name__ == '__main__':

#   print(longest_side.__doc__)
    print(longest_side(4,5))
