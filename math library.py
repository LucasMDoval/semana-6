import random
import statistics


num_scores = 20  
min_score = 10
max_score = 50
test_scores = [random.randint(min_score, max_score) for _ in range(num_scores)]


mean_score = statistics.mean(test_scores)


std_deviation = statistics.stdev(test_scores)


above_mean_count = sum(score > mean_score for score in test_scores)


print("Generated Test Scores:", test_scores)
print("Mean Score:", mean_score)
print("Standard Deviation:", std_deviation)
print("Scores above the Mean:", above_mean_count)


