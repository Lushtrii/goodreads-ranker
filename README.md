# goodreads-ranker
This project scrapes and ranks self-improvment books from goodreads.com and outputs the results as a csv.

I like reading self-improvement books, so I often look through Goodreads to either find the best of the best or look for books that have come out in the last few years that haven't gotten enough attention. Goodreads doesn't sufficiently help with this goal, and I find that its list system isn't very easy to navigate through. I attempt to solve this problem using some statistics that Goodreads assigns to each book based on user feedback, particularly, average rating and the number of ratings. My project scrapes goodreads.com's self-help section (pretending to be a logged-in user), gives the book a score, and finally outputs a csv file containing all the scraped data plus the newly created score. It also filters out books that have an average rating of < 3.7, or if they have less than 200 ratings to create a more quality set of data. 

The results of this project have led me to learn about many interesting-looking books that I have not seen before, and have added to my to-read list as a result, so I consider this project a success for my goals.

## How this project ranked books
The scoring function of the project is exactly this:

`score = round(10 * (Average rating - 3.7) + log_10(Number of ratings), 7)`

which I found is pretty good at lowering the score of higly rated books with a low number of ratings, as well as books that aren't highly rated, but have been heavily read and reviewed. I am more interested in a book with an average rating of 4.3 and 3,000 reviews than I am in a book with a 3.8 but 1,000,000 reviews, so this score function tries to reflect that.

If you are interested in the results of this project, I've included the output csv in this repository [here](https://github.com/Lushtrii/goodreads-ranker/blob/main/example_data/scored_book_data.csv).


## Features I hope to add in the future:

* Making the score function output nicer numbers and become less reliant on floating point numbers. Perhaps giving the book a score out of 100, while ideally filtering out any book with a score less than 75.

* Add a Goodreads url column in the csv to allow for easy navigation to each book.

* Could make this project more usable for others and add instructions for how to use it. Things like being able to set flags for changing the shelf to scrape, or the output path without examining the code itself. Perhaps even give it a GUI.

* Should probably look into using Enums for the dictionary keys to ensure consistency.


