#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, start):
        self.start = start
    
    def write(self, string):
        print(f"{self.start}{string}")


def main():
    pass

if __name__ == "__main__":
    main()
