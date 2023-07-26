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
streamlit.dataframe(my_fruit_list)
