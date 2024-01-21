import requests
from bs4 import BeautifulSoup
import re
import csv

# Returns string
def get_webpage_html(url):
    r = requests.get(url)
    return r.text

# String -> ListOfBookDicts
def parse_data(response_html):
    books = []
    book_attributes = ['Title', 'Author', 'Avg rating', 'Number of Ratings', 'Year Published']

    #Soupify
    soup = BeautifulSoup(response_html, 'html.parser')
    #For each book entry, construct book dict
    results = soup.find_all(class_ ='elementList')

    for book_element in results:
        book_dict = dict.fromkeys(book_attributes)
        book_title = book_element.find(class_ = 'bookTitle')

        # book_element must not be a book entry
        if (book_title == None):
            continue
        
        #Strip format of book from title. E.g. (Kindle Edition)
        book_title = re.sub(r' \([\w\s]+\)', '', book_title.text)

        book_dict['Title'] = book_title
        book_dict['Author'] = book_element.find(class_ = 'authorName').text

        sub_text = book_element.select('span.greyText.smallText')[0].text
        avg_rating, num_ratings, year = extract_sub_text(sub_text)
        num_ratings = num_ratings.replace(',', '')

        # Not a big deal if year data is missing from book, but other attributes are crucial for ranking
        if (avg_rating == None or num_ratings == None):
            continue
        
        book_dict['Avg rating'] = float(avg_rating)
        book_dict['Number of Ratings'] = int(num_ratings)
        book_dict['Year Published'] = int(year) if year else None

        books.append(book_dict)

    return books

def extract_sub_text(sub_text):

    avg_rating_regex = re.compile('avg rating (?P<avg_rating>\d.\d\d)')
    num_rating_regex = re.compile('(?P<num_ratings>\d{1,3}(,\d{3})*) ratings')
    year_regex = re.compile('published (?P<year>\d{4})')

    avg_rating_match = avg_rating_regex.search(sub_text)
    num_ratings_match = num_rating_regex.search(sub_text)
    year_match = year_regex.search(sub_text)
    
    avg_rating = avg_rating_match.group('avg_rating') if avg_rating_match else None
    num_ratings = num_ratings_match.group('num_ratings') if num_ratings_match else None
    year = year_match.group('year') if year_match else None

    return avg_rating,num_ratings,year


#Return list of books
    
# TODO
def write_to_csv(data):
    pass
