import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(__file__).parent / "data" / "books.csv"
books = pd.read_csv(file_path)

print("The first 5 rows:")
print(books.head())

# Check and clean the dataset
print("\nShape (rows, columns):")
print(books.shape)

print("\nBook information:")
books.info()

print("\nMissing values per column:")
print(books.isna().sum())

print("\nNumber of duplicate rows:")
print(books.duplicated().sum())

clean_book = books.drop_duplicates()

print("\nShape after removing duplicates:")
print(clean_book.shape)

# Compare genres
print("\nNumber of entries by genre:")
print(clean_book["Genre"].value_counts())

print("\nAverage rating and price by genre:")
print(clean_book.groupby("Genre")[["User Rating", "Price"]].mean().round(2))

print("\n10 authors with the most entries:")
print(clean_book["Author"].value_counts().head(10))

print("\nAverage rating and price by year:")
print(clean_book.groupby("Year")[["User Rating", "Price"]].mean().round(2))

print("\nBooks rated 4.9 or higher:")
high_rated = clean_book.loc[
    clean_book["User Rating"] >= 4.9,
    ["Name", "Author", "User Rating", "Year"]
].sort_values("User Rating", ascending=False).head(10)
print(high_rated)

# Chart: entries by genre
clean_book["Genre"].value_counts().plot(
    kind="bar",
    color=["steelblue", "orange"]
)
plt.title("Bestseller entries by genre")
plt.xlabel("Genre")
plt.ylabel("Number of entries")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart: average price by year
clean_book.groupby("Year")["Price"].mean().plot(
    kind="line",
    marker="o",
    figsize=(9, 5)
)
plt.title("Average book price by year")
plt.xlabel("Year")
plt.ylabel("Average price")
plt.tight_layout()
plt.show()