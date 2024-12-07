data = [line.strip() for line in open("day1_input.txt").readlines()]

list1 = sorted([int(d.split()[0]) for d in data])
list2 = sorted([int(d.split()[1]) for d in data])

total = sum(abs(a - b) for a, b in zip(list1, list2))
print(f"total distance: {total}")

#part_2
#We import Counter from Python's collections module.
#Counter is a dictionary-like class that counts occurrences of elements in a list.
from collections import Counter

#defining the function
#We define a function named calculate_similarity_score that takes two lists as arguments: left_list and right_list.
def calculate_similarity_score(left_list, right_list):
    # Count occurrences in the right list
    right_count = Counter(right_list)
#We create a Counter object from right_list, storing how often each number appears.
#Example: right_list = [4, 3, 5, 3, 9, 3] → right_count = {3: 3, 4: 1, 5: 1, 9: 1}

   # Calculate similarity score
    score = sum(num * right_count[num] for num in left_list)
    '''
We calculate the similarity score using a list comprehension:
For each num in left_list, we multiply num by its occurrence count in right_count.
If a number doesn't exist in right_count, its count defaults to 0.
We sum these values to get the total score.
Example:

left_list = [3, 4, 2, 1, 3, 3]
Calculations:
3 * 3 = 9 (since 3 appears 3 times in right_list)
4 * 1 = 4 (4 appears once)
2 * 0 = 0 (2 is not in right_list)
1 * 0 = 0 (1 is not in right_list)
3 * 3 = 9 (3 appears 3 times)
3 * 3 = 9 (3 appears 3 times)    
    '''
#returnig the result
    return score


# extract  left list and right list from input file
data = [line.strip() for line in open("day1_input.txt").readlines()]

left_list = sorted([int(d.split()[0]) for d in data])
right_list = sorted([int(d.split()[1]) for d in data])


# Calculate and print the score
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity Score: {similarity_score}")
