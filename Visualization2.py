import streamlit as st
import plotly.express as px
import pandas as pd
import io
# Load your retail sales data
retail_data = pd.read_csv("https://raw.githubusercontent.com/carolistical/visualization2/main/retail_sales_data.csv")

# Create a Streamlit app
st.header('Bar Chart - Retail Sales Data')
df = pd.DataFrame(retail_data)

#show data checkbox
if st.checkbox("Show data"):
    st.write(df)

#plot barchart checkbox
if st.checkbox("Plot Barchart"):
    # Create a slider to select a month
    selected_month = st.slider('select a month', min_value=1, max_value=12)

    # Filter the DataFrame for the selected month
    filtered_df = df[df['month'] == selected_month]

    # Calculate total revenue per category
    category_revenue = filtered_df.groupby('Category')['Revenue'].sum().reset_index()

    # Create the bar chart with an f string so that the selected month is dynamic
    bar = px.bar(category_revenue, x='Category', y='Revenue',color='Category', title=f'Bar Chart for Month {selected_month}', labels={'Revenue': 'Total Revenue'})

    # Show the bar chart
    st.plotly_chart(bar)




