import streamlit as st
import pandas as pd

st.set_page_config(page_title="Amazon Books Dashboard", layout="wide")
st.title("Amazon Bestselling Books")
st.caption("Explore book entries from 2009–2019 by genre, rating, price, and author.")

@st.cache_data
def load_books():
    return pd.read_csv("data/books.csv")

books = load_books().drop_duplicates()

# Sidebar filters
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Select year range",
    min_value=int(books["Year"].min()),
    max_value=int(books["Year"].max()),
    value=(int(books["Year"].min()), int(books["Year"].max())),
)

genres = sorted(books["Genre"].dropna().unique())
selected_genres = st.sidebar.multiselect(
    "Choose genres",
    options=genres,
    default=genres,
)

filtered = books[
    books["Year"].between(year_range[0], year_range[1])
    & books["Genre"].isin(selected_genres)
]

# Summary cards
col1, col2, col3 = st.columns(3)
col1.metric("Book entries", len(filtered))
col2.metric(
    "Average rating",
    f"{filtered['User Rating'].mean():.2f}" if len(filtered) else "—",
)
col3.metric(
    "Average price",
    f"${filtered['Price'].mean():.2f}" if len(filtered) else "—",
)

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Entries by genre")
    st.bar_chart(filtered["Genre"].value_counts())

with right:
    st.subheader("Average price by year")
    price_by_year = filtered.groupby("Year")["Price"].mean()
    st.line_chart(price_by_year)

st.subheader("Authors with the most entries")
st.bar_chart(filtered["Author"].value_counts().head(10))

st.subheader("Book data")
st.dataframe(filtered, use_container_width=True)