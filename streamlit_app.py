import streamlit
streamlit.title('my kids are champions')
streamlit.title('breakfast menu')
streamlit.title('bread omlet')
streamlit.title('rice lunch')
streamlit.title('snack')
streamlit.header('kids favorates')
streamlit.text('pizza')
streamlit.text('biryani')
streamlit.text('avacado toast')
streamlit.header('🍕 kids make your own pizza🍕')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Pear','Plums'])



