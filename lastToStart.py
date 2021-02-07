# Activity Selection Last-to-Start Greedy Algorithm Implementation
# By: Kyle Huang

from pprint import pprint
# Function to process input file
# returns list where each row is file row
def process_file():
    activities = []
    with open('act.txt') as infile:
        activities = [row.rstrip() for row in infile]
    return activities


# Function to process data from file
# Splits activities into list of activity sets
# Returns list of activity sets
def process_data(activities):
    # init activity set
    act_set = []
    i = 0

    while i < len(activities):
        t = int(activities[i])
        row = []
        for j in range(i + 1,  i + t + 1):
            # get each individual activity
            elem = activities[j].split()
            for m in range(0, 3):
                elem[m] = int(elem[m])
            row.append(elem)
        i += t + 1
        act_set.append(row)
    return act_set


# Last to start algorithm implementation
# Input: activities list of lists
def last_to_start(activities):
    # extract start and finish from activities
    start = [row[1] for row in activities]
    finish = [row[2] for row in activities]

    # total number of activities
    n = len(start)
    # Array to store optimal solution
    a = []
    a.append(activities[0][0])
    i = 0

    for j in range(1, n):
        if start[i] >= finish[j]:
            a.insert(0, activities[j][0])
            i = j
    return a


# Driver code
if __name__=="__main__":
    aa = process_data(process_file())

    for s in aa:
        # Sort the activities by finish time in decreasing order
        s.sort(key=lambda x: x[2], reverse=True)
        sol = last_to_start(s)
        print("Number of activities selected = ", len(sol))
        print("Activities: %s %s"% (" ".join(map(str, sol)), "\n"))




