import streamlit as st
from src.main import simulate_game
import time

st.title("Dashboard for Monty holl ")

number = st.number_input("Select your switch ", min_value=10, max_value=10000, value=100)

col1, col2 = st.columns(2)

col1.subheader("switch")
col2.subheader("without switch")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_no_switch = 0
wins_switch = 0

for i in range(number):
    number_wins_with_switching, number_simulate_game_without_switch = simulate_game(1)
    wins_no_switch += number_simulate_game_without_switch
    wins_switch += number_wins_with_switching

    chart1.add_rows([wins_switch / (i + 1)])
    chart2.add_rows([wins_no_switch / (i + 1)])

    time.sleep(0.05)
    


