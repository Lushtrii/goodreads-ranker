import unittest

import os

from src.goodreadsranker import scraper

class TestScraper(unittest.TestCase):

    def test_quality_filter_book_with_few_reviews(self):
        book_to_score = {
        'Title': 'Very New Book',
        'Author': 'John Doe',
        'Avg rating': 4.16,
        'Number of Ratings': 12,
        'Year Published': 2024
        }

        self.assertFalse(scraper.quality_filter(book_to_score))

    def test_quality_filter_book_with_bad_reviews(self):
        book_to_score = {
        'Title': 'Very Controversial Book',
        'Author': 'John Doe',
        'Avg rating': 3.6,
        'Number of Ratings': 1563203,
        'Year Published': 2024
        }

        self.assertFalse(scraper.quality_filter(book_to_score))

    def test_quality_filter_few_and_bad_reviews(self):
        book_to_score = {
        'Title': 'Very Bad Book',
        'Author': 'John Doe',
        'Avg rating': 2.7,
        'Number of Ratings': 12,
        'Year Published': 2024
        }

        self.assertFalse(scraper.quality_filter(book_to_score))

    def test_quality_filter_good_book(self):
        book_to_score = {
        'Title': 'Best Book',
        'Author': 'John Doe',
        'Avg rating': 4.37,
        'Number of Ratings': 10543,
        'Year Published': 2024
        }

        self.assertTrue(scraper.quality_filter(book_to_score))
    
    def test_get_webpage_html(self):
        #Page may change, so can't test for exact html.
        #Just check if link is still good (i.e. doesn't throw an exception).
        website_url = 'https://www.goodreads.com/shelf/show/personal-development'
        scraper.get_webpage_html(website_url)
            
    def test_extract_sub_text(self):
        text = '''<span class="greyText smallText">
                avg rating 4.36 —
                796,219 ratings  —
                published 2018
              </span>'''
        
        actual_avg_rating, actual_num_ratings, actual_published_year = scraper.extract_sub_text(text)
        self.assertEqual(actual_avg_rating, '4.36')
        self.assertEqual(actual_num_ratings, '796,219')
        self.assertEqual(actual_published_year, '2018')
        
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

    def test_write_to_csv(self):
        book_list = [
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
        scraper.write_to_csv(book_list, './tests/book_data.csv')
        with open('./tests/expected_scrape_results.csv', 'r', newline='') as expected_csv, open('./tests/book_data.csv', newline='') as actual_csv:
            expected_lines = expected_csv.readlines()
            actual_lines = actual_csv.readlines()

            for expected_line, actual_line in zip(expected_lines, actual_lines):
                expected_line = expected_line.replace('\r\n', '')
                actual_line = actual_line.replace('\r\n', '')
                self.assertEqual(expected_line, actual_line)

        #Cleanup
        os.remove('./tests/book_data.csv')

        
if __name__ == '__main__':
    unittest.main()
