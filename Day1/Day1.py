data = [line.strip() for line in open("day1_input.txt").readlines()]

list1 = sorted([int(d.split()[0]) for d in data])
list2 = sorted([int(d.split()[1]) for d in data])

total = sum(abs(a - b) for a, b in zip(list1, list2))
print(f"total distance: {total}")

#part_2
from collections import Counter


def calculate_similarity_score(left_list, right_list):
    # Count occurrences in the right list
    right_count = Counter(right_list)

    # Calculate similarity score
    score = sum(num * right_count[num] for num in left_list)
    return score


# extract  left list and right list from input file
data = [line.strip() for line in open("day1_input.txt").readlines()]

left_list = sorted([int(d.split()[0]) for d in data])
right_list = sorted([int(d.split()[1]) for d in data])


# Calculate and print the score
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity Score: {similarity_score}")
