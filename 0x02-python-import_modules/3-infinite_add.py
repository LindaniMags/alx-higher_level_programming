#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    tot = 0
    for item in range(len(sys.argv) - 1):
        tot += int(sys.argv[item + 1])
    print("{}".format(tot))
