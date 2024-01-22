import math
import csv
import shutil

def score(book_row):
    avg_rating = float(book_row['Avg rating'])
    num_ratings = int(book_row['Number of Ratings'])
    return round(10 * (avg_rating - 3.7) + math.log10(num_ratings), 7)

def add_score_to_csv(csv_path):
    original_book_attributes = ['Title', 'Author', 'Avg rating', 'Number of Ratings', 'Year Published']
    with open(csv_path, 'r', newline='') as csvfile, open('./tmp.csv', 'w') as tmp:
        book_data_reader = csv.reader(csvfile)
        updated_csv = csv.writer(tmp)
        updated_csv.writerow(original_book_attributes + ['Score'])
        for i, row in enumerate(book_data_reader):

            if i == 0:
                continue

            book_dict = {attr: val for attr, val in zip(original_book_attributes, row)}
            row_score = score(book_dict)
            book_dict['Score'] = row_score

            updated_csv.writerow(book_dict.values())

    shutil.move('./tmp.csv', csv_path)
            