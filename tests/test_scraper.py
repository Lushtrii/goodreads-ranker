import unittest

from src.goodreadsranker import scraper

class TestScraper(unittest.TestCase):

    def test_parse_data(self):
        self.maxDiff = None
        expected_output_examples = [
            {'Title': 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones',
            'Author': 'James Clear',
            'Avg rating': 4.36,
            'Number of Ratings': 796219,
            'Year Published': 2018},

            {'Title': 'The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change',
            'Author': 'Stephen R. Covey',
            'Avg rating': 4.16,
            'Number of Ratings': 727556,
            'Year Published': 1988},

            {'Title': 'How to Win Friends and Influence People',
            'Author': 'Dale Carnegie',
            'Avg rating': 4.22,
            'Number of Ratings': 952522,
            'Year Published': 1936},

            {'Title': 'The Subtle Art of Not Giving a F*ck: A Counterintuitive Approach to Living a Good Life',
            'Author': 'Mark Manson',
            'Avg rating': 3.90,
            'Number of Ratings': 1068551,
            'Year Published': 2016},
        ]

        num_examples = len(expected_output_examples)
        
        with open('./tests/goodreads-page-sample.html', 'r') as f:
            html_data = f.read()
            output = scraper.parse_data(html_data)

            self.assertEqual(output[:num_examples], expected_output_examples)

if __name__ == '__main__':
    unittest.main()
