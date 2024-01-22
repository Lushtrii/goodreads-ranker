import math
import csv

def score(book_row):
    avg_rating = book_row['Avg rating']
    num_ratings = book_row['Number of Ratings']
    return 10 * (avg_rating - 3.7) + math.log10(num_ratings)

def add_score_to_csv(csv_path):
    pass