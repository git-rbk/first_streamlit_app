import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞 Idli and Sambar')
streamlit.text('🐔 Boiled Eggs')
streamlit.text('🥑 Avacado')
streamlit.text('🥗 Upma')
streamlit.text('🥣 Ghavanaa')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page
streamlit.dataframe(my_fruit_list)
