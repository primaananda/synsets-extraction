#created by prima ananda 10 may 2018
import re

def preprocessing():
    dicts = []
    with open('tesaurus.txt') as file:
        lines = file.readline()
        while lines:
            dicts.append(lines.rstrip())
            lines = file.readline()
    for x in dicts:
        print x

def main():
    pre = preprocessing()
    print pre

main()