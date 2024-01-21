import scraper

def main():
    html = scraper.get_webpage_html()
    scraper.parse_data(html)

if __name__ == '__main__':
    main()