import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
for i in range(3):
  streamlit.text(f'entry {i+1}')
