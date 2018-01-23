import math
def polysum(n,s):
    '''
    Takes the number of sides and the length of those sides of a regular polygon.
    Returns the perimiter squared added to the area rounded to 4 decimals
    n: Number of Sides
    s: Length of The Sides
    returns: Sum of Area and Perimeter Squared
    '''
    # YCode
    area = (.25 * n * s * s) / (math.tan(math.pi/n))
    perimeter = s * n
    return round(area + perimeter**2,4)