import re

def extract_and_sum_multiplications_from_file(filename):
    # Read the contents of the file
    with open(filename, 'r') as file:
        corrupted_data = file.read()

    # Define the regular ex pattern for valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches in the corrupted data using the regex pattern
    matches = re.findall(pattern, corrupted_data)

    # Initialize a variable to accumulate the sum of the multiplications
    total_sum = 0

    # Process each match
    for match in matches:
        # Extract the numbers from the match (they are strings, so convert to integers)
        num1 = int(match[0])
        num2 = int(match[1])

        # Multiply and add to the total sum
        total_sum += num1 * num2

    return total_sum


# Call the function with the input file and print the result
filename = "day3_input.txt"  # Name of your input file
result = extract_and_sum_multiplications_from_file(filename)
print("Total sum of valid multiplications:", result)

#Part_2
import re

def extract_and_sum_multiplications_from_file(filename):

    # Read the contents of the file
    with open(filename, 'r') as file:
        corrupted_data = file.read()

        # Define regex patterns for valid instructions
    valid_pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

    #     # Extract all matches from the corrupted data
    all_matches = re.findall(valid_pattern, corrupted_data)

    # Initial state: mul instructions enabled
    is_mul_enabled = True
    total = 0

    # Process each match
    for matches in all_matches:
        if matches == "do()":
            is_mul_enabled = True
        elif matches == "don't()":
            is_mul_enabled = False
        elif matches.startswith("mul") and is_mul_enabled:
            valid_matches = re.findall(r"mul\((\d+),(\d+)\)",matches)
            total += sum(int(x)*int(y) for x,y in valid_matches)
    return total


#Test the function with a sample memory string
filename = "day3_input.txt"  # Replace with your actual file path
result = extract_and_sum_multiplications_from_file(filename)
print("Total sum of valid do/don't multiplications:", result)
