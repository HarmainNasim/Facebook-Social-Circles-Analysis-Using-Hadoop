"""mapper.py"""
import sys

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    line = " ".join(line.split())
    split_lines = line.split(" ", 2)
    filename= split_lines[0]
    circle_name = split_lines[1]
    edges = [int(edge.strip()) for edge in split_lines[2].split(" ")]
    print("{} {} {} {}".format(filename, circle_name, len(edges), split_lines[2]))
