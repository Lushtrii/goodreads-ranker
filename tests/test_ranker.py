import unittest
import os
import shutil

from src.goodreadsranker import ranker

class TestRanker(unittest.TestCase):
    
    def test_score(self):
        book_row_to_score = {
        'Title': 'The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change',
        'Author': 'Stephen R. Covey',
        'Avg rating': 4.16,
        'Number of Ratings': 727556,
        'Year Published': 1988
        }
        expected_score = 10.4618664

        actual_score = ranker.score(book_row_to_score)
        self.assertAlmostEqual(expected_score, actual_score)

    def test_add_score_to_csv(self):
        test_data_path = './tests/book_data.csv'

        shutil.copy('./tests/expected_scrape_results.csv', test_data_path)

        ranker.add_score_to_csv(test_data_path)

        with open('./tests/expected_score.csv', 'r', newline='') as expected_csv, open('./tests/book_data.csv', newline='') as actual_csv:
            expected_lines = expected_csv.readlines()
            actual_lines = actual_csv.readlines()

            for expected_line, actual_line in zip(expected_lines, actual_lines):
                expected_line = expected_line.replace('\r\n', '')
                actual_line = actual_line.replace('\r\n', '')
                self.assertEqual(expected_line, actual_line)

        #Cleanup
        os.remove(test_data_path)
