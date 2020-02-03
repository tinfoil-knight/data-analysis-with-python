#!/usr/bin/env python3
import re
def file_extensions(filename):
    f = open(filename, "r")
    lines = f.readlines()
    noext = []
    exts = {}
    for line in lines:
        try:
            re.match(r"(.*)\.(\w+)", line).groups()[1]
        except:
            noext.append(line.strip("\n"))
        else:
            tupleitem = re.match(r"(.*)\.(\w+)", line).groups()
            key = tupleitem[1]
            value = tupleitem[0]
            if key in exts:
                exts[key].append(f"{value}.{key}")
            else:
                exts[key] = [f"{value}.{key}"]
    f.close()
    return (noext, exts)

def main():
    x = file_extensions("src/filenames.txt")
    result = [f"{len(x[0])} files with no extension"]
    for key in sorted(x[1]):
        result.append(f"{key} {len(x[1][key])}")
    print("\n".join(result))
    

if __name__ == "__main__":
    main()
