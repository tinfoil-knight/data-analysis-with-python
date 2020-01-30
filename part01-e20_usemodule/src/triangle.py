# Enter you module contents here
"""Helpful functions for operation on triangles."""

def hypothenuse(a, b):
    """Takes 2 Sides of a Right-Angled triangle as input
    and returns the length of its hypotenuse"""
    return (a**2 + b**2)**(0.5)

def area(a, b):
    """Takes 2 perpendicular sides of a triangle as input
    and returns the area"""
    return 0.5*a*b

__author__="Kunal K."
__version__="0.0.1"
