# Function to check if a report is safe
def is_safe_report(report):
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Check if difference is out of range
        if abs(diff) not in [1, 2, 3]:  # Ensure the difference is between 1 and 3
            return False

        # Check if not all increasing or all decreasing
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    # The report is safe if either all increasing or all decreasing

    return increasing or decreasing


# Read data from input file
reports = []
with open("day2_input.txt", "r") as file:
    for line in file:
        #line-->7 6 4 2 1
        # Convert each line of numbers to a list of integers

        reports.append(list(map(int, line.split())))

        #line.split()-->If line = 7 6 4 2 1-->["7", "6", "4", "2", "1"]
        #map(int, line.split())-->["7", "6", "4", "2", "1"]-->[7, 6, 4, 2, 1]
        #list(map(int, line.split()))-->[7, 6, 4, 2, 1]
        # list() function converts the map object into a list.
        #reports.append(list(map(int, line.split())))-->[[7, 6, 4, 2, 1]]

#reports = [list(map(int,line.strip().split())) for line in open("day2_input.txt").readlines()]




# Count the number of safe reports
safe_count = 0

for report in reports:

    if is_safe_report(report):

        safe_count += 1

print(f"Number of safe reports: {safe_count}")

#Part_2
def is_safe_with_one_removal(report):
    # Check if we can make the report safe by removing one level
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]  # Remove one element
        if is_safe_report(new_report):
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report) or is_safe_with_one_removal(report):
            safe_count += 1
    return safe_count


# Count and print how many reports are safe
print(f"Number of safe reports after one removal:{count_safe_reports(reports)}")