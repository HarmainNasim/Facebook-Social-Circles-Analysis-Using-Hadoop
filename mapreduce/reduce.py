"""reducer.py"""
import sys

cur_max_circle = None
cur_max_edge_count = 0
cur_max_edges = []
max_filename = None
all_circles = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    file_name, circle_name, edge_count, edges = line.split(" ", 3)

    edges_int = [int(x) for x in edges.split(" ")]

    all_circles.append((file_name, circle_name, edges_int))

    if int(edge_count) > cur_max_edge_count:
        cur_max_circle = circle_name
        cur_max_edge_count = int(edge_count)
        cur_max_edges = edges_int
        max_filename = file_name
# Approach 1: using set intersection (duplicates won't be counted)
cur_most_similar_circle = None
cur_most_similar_circle_edge_count = 0
cur_most_similar_circle_edges = []

for circle in all_circles:
    file_name = circle[0]
    circle_name = circle[1]
    circle_edges = circle[2]

    if file_name != max_filename:
        intersected_edges = list(set(cur_max_edges) & set(circle_edges))

        if len(intersected_edges) > cur_most_similar_circle_edge_count:
            cur_most_similar_filename = file_name
            cur_most_similar_circle = circle_name
            cur_most_similar_circle_edge_count = len(intersected_edges)
            cur_most_similar_circle_edges = intersected_edges
print("data of the user with largest circle :")
print("UserName : " + max_filename)
print("Circle : " + cur_max_circle)
print("Count of nodes :" + str(cur_max_edge_count))
print("List of nodes :" , cur_max_edges)

print("---------------")

#print("Approach 1")
print("data of the user with most similarity with the largest circle :")
print("UserName : " + cur_most_similar_filename)
print("Circle : " + cur_most_similar_circle)
print("Count of similar nodes :" + str(cur_most_similar_circle_edge_count))
print("List of nodes :" , cur_most_similar_circle_edges)

