# Initialize the count
count = 0

# Open the file and read each line
with open("input.txt", 'r') as f:
    for line in f:
        # Strip leading and trailing whitespace from the line
        line = line.strip()

        # Split the line into the two ranges
        range1, range2 = line.split(',')

        # Parse the ranges into tuples containing the start and end values
        range1 = tuple(map(int, range1.split('-')))
        range2 = tuple(map(int, range2.split('-')))

        # Check if range1 fully encapsulates range2 and increment the count if it does
        if (range1[0] in range(range2[0], range2[1]+1) or range1[1] in range(range2[0], range2[1]) or range2[0] in range(range1[0], range1[1]+1) or range2[1] in range(range1[0], range1[1]+1)):
            count += 1

# Print the count
print(count)

