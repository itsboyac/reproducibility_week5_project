"""Note that if you use poetry environment, you should use 'poetry run' before each command to ensure it runs in the correct environment.
"""

get-data:
	poetry run python src/fetch_data.py

scrape:
	poetry run python src/scrape_books.py

clean:
	poetry run python src/clean_books.py   # optional cleaning step

train:
	poetry run python src/classify.py

all: get-data scrape clean train

