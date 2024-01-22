import scraper
import ranker

def main():
    website_url = 'https://www.goodreads.com/shelf/show/personal-development'
    output_path = './book_data.csv'
    scraper.scan_shelf(website_url, 25, output_path)
    ranker.add_score_to_csv(output_path)

if __name__ == '__main__':
    main()