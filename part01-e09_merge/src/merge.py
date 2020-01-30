#!/usr/bin/env python3

# Not you K.
def merge(list1, list2):

    if not list1:
        return list2
    elif not list2:
        return list1

    merged_list = []

    i = 0
    j = 0

    for k in range(len(list1) + len(list2)):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            if i < len(list1) - 1:
                i += 1
            else:
                merged_list += list2[j:]
                break
        else:
            merged_list.append(list2[j])
            if j < len(list2) - 1:
                j += 1
            else:
                merged_list += list1[i:]
                break

    return merged_list


def main():
    pass

if __name__ == "__main__":
    main()
