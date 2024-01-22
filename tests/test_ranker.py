import unittest

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
        expected_score = 10.461866

        actual_score = ranker.score(book_row_to_score)
        self.assertAlmostEqual(expected_score, actual_score)

    def test_add_score_to_csv(self):
        pass
