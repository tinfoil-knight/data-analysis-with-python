#!/usr/bin/env python3

def extract_numbers(s):
    nums = []
    for word in s.split():
        try:
            nums.append(int(word))
        except:
            try:
                nums.append(float(word))
            except:
                pass
    return nums
            

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
