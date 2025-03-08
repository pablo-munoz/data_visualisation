import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import time
import random

st.title("Airline Passengers Analysis: Which Year Had the Highest Traffic?")


question = "Which year had the highest total number of airline passengers?"
st.subheader(question)

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSPXm7zEdLojSaqt6ZSswfx5mFEWqKXTGAD1jG07K5wsP-WEQT9wlRNV8a1N6vWkY3nxxZsyuIqPu9J/pub?output=csv"
flights_df = pd.read_csv(sheet_url)
# Prepare data: aggregate total passengers per year
yearly_passengers = flights_df.groupby('year')['passengers'].sum().reset_index()


if 'chart_type' not in st.session_state:
    st.session_state.chart_type = None
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'chart_displayed' not in st.session_state:
    st.session_state.chart_displayed = False

# Button to randomly select and show one of the two charts
if not st.session_state.chart_displayed:
    if st.button("Show a Chart"):  # first button
        # Randomly pick chart A or B
        st.session_state.chart_type = random.choice(['A', 'B'])

        st.session_state.start_time = time.time()  
        st.session_state.chart_displayed = True
        

# If a chart has been selected and should be displayed:
if st.session_state.chart_displayed and st.session_state.chart_type:
    # Display chart
    if st.session_state.chart_type == 'A':
        st.write("**Chart A: Line Chart of Passenger Growth Over Years**")
        fig = px.line(yearly_passengers, x='year', y='passengers', title="Total Passengers per Year (Line Chart)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("**Chart B: Bar Chart of Total Passengers per Year**")
        fig = px.bar(yearly_passengers, x='year', y='passengers', title="Total Passengers per Year (Bar Chart)")
        st.plotly_chart(fig, use_container_width=True)
    
    # second button to end the question and measure response time
    if st.button("I answered your question"):
        end_time = time.time()
        # Calculate response time in secs
        response_time = end_time - st.session_state.start_time
        # Display the response time
        st.success(f"Your response time: {response_time:.2f} seconds.")
    
