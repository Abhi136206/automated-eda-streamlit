# Step 1: Create the list of scores
scores = [85, 90, 78, 92, 88, 76, 95, 89]

# Step 2: Append a new score (80) to the list
scores.append(80)
print("Scores after appending 80:", scores)

# Step 3: Remove the lowest score from the list
lowest_score = min(scores)
scores.remove(lowest_score)
print("Scores after removing the lowest score:", scores)

# Step 4: Calculate and print the average score
average_score = sum(scores) / len(scores)
print("Average score:", average_score)

# Step 5: Sort the list in descending order and print the sorted list
scores.sort(reverse=True)
print("Scores sorted in descending order:",scores)