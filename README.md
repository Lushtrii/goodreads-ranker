# goodreads-ranker

## Project description

This project scrapes and ranks self-improvement books from Goodreads, assigning each book a score based on its average rating and number of reviews. The goal is to highlight high-quality books that might be overlooked by traditional Goodreads sorting. The final ranked list is saved as a CSV file, filtering out books with an average rating below 3.7 or fewer than 200 ratings.

Through this project, I've discovered many interesting books I hadn't come across before, successfully expanding my to-read list.

### How this project ranks books
The scoring function ranks books using the formula:

`score = round(10 * (Average rating - 3.7) + log10(Number of ratings), 7)`
- Books with a **higher rating** get a boost.
- Books with **more reviews** get a boost.
- Highly rated books with very few ratings are **penalized** to avoid overvaluing new/unknown books.
- 
## Results
If you're interested in the results, you can find the output CSV file in this repository [here](https://github.com/Lushtrii/goodreads-ranker/blob/main/example_data/scored_book_data.csv).
